import torch
import torch.nn.functional as F
import random
# import copy
import time
import matplotlib.pyplot as plt
# import numpy as np
# from sklearn import cluster
import networkx as nx
# from numba import jit, cuda


from simulator.NN_correlation_matrix.Reaction import Reaction
from simulator.NN_correlation_matrix.Gan_NN_Matrix_simulator import Generator
from simulator.NN_correlation_matrix.GeneratorStructureFactory import GeneratorStructureFactory
from simulator.NN_correlation_matrix.ResultProcessor import ResultProcessor
from simulator.NN_correlation_matrix.ResultSaver import ResultSaver

gan_model_global = None #variable to make setting of model easier


def show_matrix(t):
    # img = img / 2 + 0.5     # unnormalize
    plt.title('correlation matrix')
    npimg = t.cpu().numpy()
    plt.imshow(npimg, cmap="Greys")
    #plt.show()


def show_graph(t, threshold=0.9, pos_color="b", neg_color="r"):
    t = t.cpu()
    apos = torch.threshold(t, threshold, 0).numpy()
    gpos = nx.from_numpy_matrix(apos)

    aneg = torch.threshold(t.neg(), threshold, 0).numpy()
    gneg = nx.from_numpy_matrix(aneg)

    pos = nx.spring_layout(gpos)

    nx.draw_networkx(gpos, pos=pos, with_labels=False, node_size=2, edge_color=pos_color, node_color="black", alpha=0.2)
    nx.draw_networkx(gneg, pos=pos, with_labels=False, node_size=2, edge_color=neg_color, node_color="black", alpha=0.2)

    # nx.draw_networkx_edges(gneg,pos,
    #                            with_labels=False,
    #                            edge_color='r',
    #                            width=1.0,
    #                            alpha=0.1
    #                         )
    # nx.draw_networkx_edges(gpos,pos,
    #                            with_labels=False,
    #                            edge_color='b',
    #                            width=1.0,
    #                            alpha=0.2
    #                         )

    # plt.axis('off')
    plt.title('correlation network')
    #plt.show()


def print_reactions(reactions):
    original = (reactions.get_reactions_tensor() * 10).int()
    original = [repr(t) for t in list(original)]
    original.sort()
    for i in original:
        print(i)


def generate_reaction_def(sub_count, prod_count, metabolites, low=0, high=1):
    """
    returns a tupple (substrate, product) of sub_count substrates randomly drawn from metabolites
    and prod_count products randomly drawn from metabolites
    ???such that substrates and products are mutually exclusive.???
    """
    m = set(metabolites)
    sub = set(random.sample(m, sub_count))
    prod = set(random.sample(m, prod_count))
    return ([random.uniform(low, high) if i in sub else 0.0 for i in m],
            [random.uniform(low, high) if i in prod else 0.0 for i in m])





# class MultiReaction(torch.nn.Module):
#     def __init__(self, rcount, metabolites, scount=2, pcount=2, step=0.0001, low=0.0, high=1.0, substrates=None,
#                  products=None):
#         super(MultiReaction, self).__init__()
#         self._reactions = torch.nn.ModuleList()
#         for i in range(rcount):
#             if substrates == None:
#                 sub, prod = generate_reaction_def(scount, pcount, metabolites, low, high)
#             else:
#                 sub, prod = substrates, products
#             sub = torch.Tensor(sub).to(device)  # so far there is no self.device in pytorch Modules
#             prod = torch.Tensor(prod).to(device)  # so far there is no self.device in pytorch Modules
#             r = Reaction(sub, prod, step=step)
#             self._reactions.append(r)
#
#     def forward(self, x):
#         # random.shuffle(self._reactions)
#         for m in self._reactions:
#             x = m(x)
#         return x
#
#     def get_reactions_tensor(self):
#         rslt = [r.get_def_tensor().unsqueeze(dim=0) for r in self._reactions]
#         rslt = torch.cat(rslt, dim=0)
#         return rslt

class MultiReaction_new(torch.nn.Module):
    def __init__(self, rcount, metabolites, scount=2, pcount=2, step=0.0001, low=0.0, high=1.0, substrates=None,
                 products=None):
        super(MultiReaction_new, self).__init__()
        self._reactions = torch.nn.ModuleList()
        global gan_model_global
        self._generator = Generator(m_count, reactions_count, gan_model_global)
        self._is_generated = True
        for i in range(rcount):
            if substrates == None:
                if i == 0:
                    self._generator.clear_output_layer()
                #sub, prod = generate_reaction_def(scount, pcount, metabolites, low, high)
                sub, prod = self._generator.get_reactions_tensor(i)
            else:
                sub, prod = substrates[i], products[i]
                self._is_generated = False
            sub = torch.Tensor(sub).to(device)  # so far there is no self.device in pytorch Modules
            prod = torch.Tensor(prod).to(device)  # so far there is no self.device in pytorch Modules
            # sub = torch.as_tensor(sub).to(device) #uncommon this to use GPU. Common up
            # prod = torch.as_tensor(prod).to(device)
            r = Reaction(sub, prod, step=step)
            self._reactions.append(r)

    def forward(self, x):
        # random.shuffle(self._reactions)
        if self._is_generated:
            self._reactions =  torch.nn.ModuleList()
            self._generator.clear_output_layer()
            for i in range(reactions_count):
                sub, prod = self._generator.get_reactions_tensor(i)
                sub = torch.Tensor(sub).to(device)
                prod = torch.Tensor(prod).to(device)
                # sub = torch.as_tensor(sub).to(device) #uncommon this to use GPU. Common up
                # prod = torch.as_tensor(prod).to(device)
                r = Reaction(sub, prod, step=step).to(device)
                self._reactions.append(r)

        for m in self._reactions:
            x = m(x)
        return x

    def get_reactions_tensor(self):
        rslt = [r.get_def_tensor().unsqueeze(dim=0) for r in self._reactions]
        rslt = torch.cat(rslt, dim=0)
        return rslt


def pearson_r(x, y):
    vx = x - torch.mean(x)
    vy = y - torch.mean(y)

    rx = torch.rsqrt(torch.sum(vx ** 2))
    ry = torch.rsqrt(torch.sum(vy ** 2))

    s = torch.sum(vx * vy)
    cost = s * rx * ry
    return cost


def correlation_matrix(b):
    vb = b - torch.mean(b, dim=0)
    mr = torch.rsqrt(torch.sum(vb ** 2, dim=0))
    mr = mr.unsqueeze(dim=0)
    corr = torch.mm(vb.t(), vb) * torch.mm(mr.t(), mr)
    #corr.requires_grad_() #uncommon to use GPU
    return corr

# class Process(torch.nn.Module):
#     def __init__(self, rcount, metabolites, scount=2, pcount=2, low=0.0, high=1.0, substrates=None, products=None,
#                  step=0.0001, iterations=100):
#         super(Process, self).__init__()
#         self._mr = MultiReaction(rcount, metabolites, scount=scount, pcount=pcount, step=step, low=low, high=high,
#                                  substrates=substrates, products=products)
#         self._iterations = iterations
#
#     def forward(self, x):
#         iterations_for_sample = torch.randint(low=0, high=self._iterations, size=(minibatch_size,), device=device,
#                                               requires_grad=False)
#         for i in range(self._iterations):
#             doit = (iterations_for_sample > i).float()
#             doit = doit.unsqueeze(dim=1)
#             doit = torch.cat([doit] * m_count, dim=1)
#             y = self._mr(x)
#             x = y * doit + x * (1 - doit)
#
#         c = correlation_matrix(x)
#         c = c - torch.eye(m_count).to(device)
#         return x, c
#
#     def get_reactions_tensor(self):
#         return self._mr.get_reactions_tensor()

class Process_new(torch.nn.Module):
    def __init__(self, rcount, metabolites, scount=2, pcount=2, low=0.0, high=1.0, substrates=None, products=None,
                 step=0.0001, iterations=100):
        super(Process_new, self).__init__()
        # self._mr = MultiReaction(rcount, metabolites, scount=scount, pcount=pcount, step=step, low=low, high=high,
        #                          substrates=substrates, products=products)

        #self._mr = Generator(m_count*2, None)
        self._mr = MultiReaction_new(rcount, metabolites, scount=scount, pcount=pcount, step=step, low=low, high=high,
                                  substrates=substrates, products=products)
        self._iterations = iterations

    def forward(self, x):
        iterations_for_sample = torch.randint(low=0, high=self._iterations, size=(minibatch_size,), device=device,
                                              requires_grad=False)
        for i in range(self._iterations):
            doit = (iterations_for_sample > i).float()
            doit = doit.unsqueeze(dim=1)
            doit = torch.cat([doit] * m_count, dim=1)
            y = self._mr(x)
            x = y * doit + x * (1 - doit)

        c = correlation_matrix(x)
        # c = c - torch.eye(m_count).to(device)
        return x, c

    def get_reactions_tensor(self):
         return self._mr.get_reactions_tensor()



# import numpy as np
# import sklearn.cluster as cluster

def compare_tensor_sets(s1,s2):
    """
    s1 and s2 are lists of tensors of the same size and shape.
    the comparison is performed in a greedy manner where the frist element of s1 is compared to all elements of s2,
    the minimal MSE is recorded, and the respective element of s2 is removed. The second element of s1 is compared
    to the remaining elements of s2 and so on.
    @return the average of the minimal MSE values for all elements of s1.
    """
    s1 = list(s1)
    s2 = list(s2)
    rcount = len(s1)
    assert(rcount==len(s2))
    rslt = 0.0
    while len(s1)>0:
        i = s1.pop()
        mses = torch.Tensor([F.mse_loss(i,j) for j in s2])
        j = mses.argmin()
        del s2[j]
        rslt+=mses[j]
    return rslt / rcount

m_count =20#50#200 #8 #size of metabolic profile
reactions_count = 20#50#2 #50
dataset_size = 20#50#10#1
minibatch_size = 400#10#100 #number of random initial substrates
sub_min = 2
sub_max = 2.01
epochs = 50#200
step = 0.5
iterations = 100
s_count=3
p_count=3
result_saver = None #removed to function so results won't get restarted for no reason

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#device = "cpu"
print("Device is " + str(device))


def create_random_reactions(reactions_count, metabolic_count):
    substrates = []
    products = []
    for i in range(reactions_count):
        #substrate = random.sample(range(2), metabolic_count)
        substrate = [random.randrange(0, 2, 1) for i in range(metabolic_count)]
        #product = random.sample(range(2), metabolic_count)
        product = [random.randrange(0, 2, 1) for i in range(metabolic_count)]
        substrates.append(substrate)
        products.append(product)
    return substrates, products


def create_dataset(data_size):
    metabolites = range(m_count)

    # testing 1 reaction - no common in input/output
    # reactions = Process_new(reactions_count, metabolites,
    #                         # scount=s_count, pcount=p_count,
    #                         # low=1.0,high=1.0
    #                         substrates=[[1, 1, 1, 0, 0, 0, 0, 0]],
    #                         products=[[0, 0, 0, 1, 1, 1, 0, 0]],
    #                         step=step, iterations=iterations,
    #                         ).to(device)

    # testing 1 reaction - one common in input/output
    # reactions = Process_new(reactions_count, metabolites,
    #                         # scount=s_count, pcount=p_count,
    #                         # low=1.0,high=1.0
    #                         substrates= [[1, 1, 1, 0, 0, 0, 0, 0]],
    #                         products=   [[0, 1, 0, 1, 1, 1, 0, 0]],
    #                         step=step, iterations=iterations,
    #                         ).to(device)

    #testing 2 reactions - no common in input/output
    # reactions = Process_new(reactions_count, metabolites,
    #                         # scount=s_count, pcount=p_count,
    #                         # low=1.0,high=1.0
    #                         substrates=[[1, 1, 1, 0, 0, 0, 0, 0],   [0, 1, 1, 0, 0, 0, 0, 1]],
    #                         products=[  [0, 0, 0, 1, 1, 1, 0, 0],   [1, 0, 0, 1, 1, 1, 0, 0]],
    #                         step=step, iterations=iterations,
    #                         ).to(device)

    # testing x reactions - random reactions
    subs, prods = create_random_reactions(reactions_count, m_count)
    reactions = Process_new(reactions_count, metabolites,
                            # scount=s_count, pcount=p_count,
                            # low=1.0,high=1.0
                            substrates=subs,
                            products=prods,
                            step=step, iterations=iterations,
                            ).to(device)

    print_reactions(reactions)

    # creation of dataset(?)
    with torch.no_grad():
        dataset = []
        for i in range(data_size):
            batch_x = torch.Tensor(size=(minibatch_size, m_count)).to(device)
            batch_x.uniform_(sub_min, sub_max)
            print(batch_x)
            ym, yc = reactions(batch_x)
            print(ym)
            dataset.append((batch_x, yc))
            if i % 1 == 0:
                print("batch {}: {}".format(i, yc.size()))
                print(yc.min())
                print(yc.max())
                show_matrix(yc)
                show_graph(yc, threshold=0.3)

    return dataset, reactions

#dataset, reactions = create_dataset(dataset_size) #This line will create the *same* dataset for all experiments

class Test():

    #@jit(target="cuda")
    def run_tests(self):

        global result_saver
        result_saver = ResultSaver(minibatch_size, step, dataset_size, epochs, reactions_count)

        generator_structure_factory = GeneratorStructureFactory(m_count*2*reactions_count)
        structure_list = generator_structure_factory.get_structure_list()
        for structure in structure_list:
            name = structure.get_name()
            #gan_model = structure.get_model()
            print("\n****************************************")
            print("Running Test With Structure: " + name)
            print("**************************************** \n ")
            self.run_one_test(structure)
            print("\n****************************************")
            print("End of Test With Structure: " + name)
            print("**************************************** \n ")

        print("\n****************************************")
        print("Summary")
        print("**************************************** \n ")

        for structure in structure_list:
            name = structure.get_name()
            in_err_dict, out_err_dict = structure.get_score()
            #gan_model = structure.get_model()
            str_print = "Model: " + name + " \n"
            for i in range(reactions_count):
                str_print += '\t Reaction ' + str(i+1) + " - In Err: " + in_err_dict[i] + "%. Out Err: " + out_err_dict[i] + "% \n"
            print(str_print)

        #write_data_summary(structure_list)
        result_saver.write_data_summary(structure_list)

    #@jit(target="cuda")
    def run_one_test(self, gan_structure):
        dataset, reactions = create_dataset(dataset_size) #this line will create the dateset for each experiment
        gan_model = gan_structure.get_model()
        global gan_model_global
        gan_model_global = gan_model
        metabolites = range(m_count)

        model = Process_new(reactions_count, metabolites, scount=m_count, pcount=m_count, step=step, iterations=iterations)
        model = model.to(device)

        optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
        ##optimizer = torch.optim.Adadelta(model.parameters(), lr=1.0, rho=0.9, eps=1e-06, weight_decay=1.0)
        ##optimizer = torch.optim.Adagrad(model.parameters(), lr=0.01, lr_decay=0, weight_decay=0, initial_accumulator_value=0)
        # optimizer = torch.optim.Adamax(model.parameters(), lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
        # optimizer = torch.optim.ASGD(model.parameters(), lr=0.1, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0.01)
        # optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum=0.9, dampening=0, weight_decay=0, nesterov=False)

        ploss = 0.0
        rloss = 0.0
        with torch.no_grad():
            rt = reactions.get_reactions_tensor()
            r1 = model.get_reactions_tensor()
        T = time.time()
        loss_list = []
        for epoch in range(epochs):
            for x, y in dataset:
                rand_x = torch.Tensor(size=(minibatch_size, m_count))
                rand_x.uniform_(sub_min, sub_max)
                rand_x = rand_x.to(device)

                optimizer.zero_grad()

                #ym, yc = model(x)
                ym, yc = model(rand_x)
                loss = F.mse_loss(yc, y)
                #loss_list.append(loss) moved it down because when we had many datasets it didn't work - only works with one dataset
                loss.backward(retain_graph=True)
                optimizer.step()

                # print(y_pred)
                # print(y)
                # print(loss)

                with torch.no_grad():
                    r2 = model.get_reactions_tensor()
                    if (ploss > 0) and (loss.item() / ploss > 100):
                        print(r1)
                        print(r2)
                    ploss += float(loss.item())
                    rloss += float(compare_tensor_sets(rt, r2).item())
                    r1 = r2

            if epoch % 1 == 0:
                T = time.time() - T
                ploss = ploss / 1 / dataset_size
                rloss = rloss / 1 / dataset_size
                info_string = "{}\t time:{:2.3g} \t mse:{} \t p-loss:{} \t r-loss :{}".format(epoch, T,loss, ploss, rloss)
                #write_date_epoch(gan_structure, loss, ploss, rloss,epoch,T)
                result_saver.write_data_epoch(gan_structure, loss, ploss, rloss, epoch, T)
                #loss_list.append(loss)
                loss_list.append(ploss)
                print(info_string)
                if ploss < (10 ** (-20)):
                    print("stop")
                    break
                final_ploss = ploss
                ploss = 0.0
                rloss = 0.0
                T = time.time()

            if epoch == epochs-1: #last epoch
                #gan_structure.set_last_mse_loss(loss)
                gan_structure.set_last_mse_loss(final_ploss)
                #write_date_final_epoch(gan_structure, yc, y, loss_list)
                result_saver.write_date_final_epoch(gan_structure, yc, y, loss_list)
                result_saver.save_model(model, gan_structure)

        predicted = model.get_reactions_tensor()
        predicted = predicted.round().int()

        predict_for_cal = predicted #need this for my calculate_error function, the next line converts it for string for some reason
        predicted = [repr(t) for t in list(predicted)]
        predicted.sort()
        gan_structure.add_to_predicted_reactions_list(predict_for_cal)

        original = reactions.get_reactions_tensor().int()
        original_for_cal = original
        original = [repr(t) for t in list(original)]
        original.sort()
        gan_structure.add_to_original_reactions_list(original_for_cal)

        verdict = [x==y for x,y in zip(original, predicted)]
        print(verdict)

        for i in range(len(predicted)):
            print("reaction %d predicted: %r "%(i,original[i]==predicted[i]))
            print("original:")
            print(original[i])
            print("predicted:")
            print(predicted[i])


        self.calculate_error(original_for_cal, predict_for_cal, gan_structure)
        result_saver.save_reactions(gan_structure)

    def calculate_error(self, original, predicted, gan_structure):
        calc_in_error_dict = {}
        calc_out_error_dict = {}
        for j in range(reactions_count):
            error_in_input = 0
            error_in_output = 0
            for i in range(m_count):
                if(original[j][0][i] != predicted[j][0][i]):
                    error_in_input = error_in_input + 1

                if (original[j][1][i] != predicted[j][1][i]):
                    error_in_output = error_in_output + 1

            input_error = str( (error_in_input/m_count) * 100)
            out_error = str((error_in_output / m_count) * 100)
            print("Reaction " + str(j) + " - Error in input: " + input_error + "%. Error in output: " + out_error + "%")
            calc_in_error_dict[j] = input_error
            calc_out_error_dict[j] = out_error

        gan_structure.set_score(calc_in_error_dict, calc_out_error_dict)

    #create 2 random matrix and check the mse difference between them
    def two_random_matrix_test(self,iterations_num):
        global result_saver
        result_saver = ResultSaver(minibatch_size, step, dataset_size, epochs, reactions_count)
        sum = 0
        loss_list = []
        for i in range(iterations_num):
            dataset,_ = create_dataset(1)
            dataset2,_ = create_dataset(1)
            for x1, y1 in dataset:
                for x2, y2 in dataset2:
                    loss = F.mse_loss(y1, y2)
                    loss_item = loss.item()
                    sum += loss_item
                    loss_list.append(loss_item)
                    print("loss is " + str(loss_item))
                    result_saver.save_two_random(y1,y2,i, loss_item)

        average = sum / iterations_num
        sum_squared_diff = 0
        for loss in loss_list:
            sum_squared_diff += (average - loss) ** 2
        st_dev = sum_squared_diff / iterations_num
        print("Metabolices = " + str(m_count) + ". Reactions = " + str(reactions_count))
        print("Average loss is " + str(average))
        print("Standard deviation loss is " + str(st_dev))

    def export_to_classifier(self, model_name):
        result_processor = ResultProcessor(m_count, minibatch_size, sub_min, sub_max)
        model = torch.load(result_processor.get_saving_path() + "\\Saved Models\\" + model_name)
        model.eval()
        result_processor.set_model(model)
        result_processor.run_model()


if __name__ == "__main__":
    test = Test()
    test.run_tests()
    # test.two_random_matrix_test(100)
    test.export_to_classifier("11.pt")