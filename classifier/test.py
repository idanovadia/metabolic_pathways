# pre_obj = pre.Preprocessing("C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier\\data\\metabolic_profile_xls\\2001_fruit_pericarp_metabolite.xlsx",
#                   "C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier\\data\\metabolic_profile_output_repro")
# pre_obj.fillNaToMean()
# pre_obj.saveFile()


# import classifier.correlation_matrix_creator as corr
#
# corr_obj = corr.CorrMaxtrix(
#     "C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier\\data\\metabolic_profile_output_repro\\out_2001_fruit_pericarp_metabolite.xlsx"
#     , "C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier\\data\\CorrMaxtrix")
# corr_obj.corr()
# corr_obj.saveFile()


# import classifier.graph_creator.graph_creator as gc
#
# gc_obj = gc.Graph_Creator(corr_matrix_path="C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier"
#                                            "\\data\\CorrMaxtrix\\CorrMatrix_out_2001_fruit_pericarp_metabolite.xlsx",
#                           subGraphs_dir_path= "C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier"
#                                               "\\data\\labeled_data\\2001\\trainset")
# gc_obj.create()
#
# import classifier.sub2vec.sub2vec as s2v
import networkx as nx
# G = nx.Graph()
# s2v_obj = s2v.Sub2Vec()
# G.add_edges_from([("a", "e"), ("a", "c"), ("a", "d"), ("c", "b"), ("b", "e"), ("e", "d")])
# rw_graph = s2v_obj.randomWalk(G)
# import classifier.sub2vec.doc2vec as d2v
#
# a = [["a","b","c","d"],["b","k","r","t"],["c","d","f","e"],["e","k","r","y"],["g","h","c","d"]]
# d2v_obj = d2v.Doc2Vec(a)
# d2v_obj.Doc2Vec()

G1 = nx.fast_gnp_random_graph(20, 0.5)
G2 = nx.fast_gnp_random_graph(20, 0.3)
G3 = nx.fast_gnp_random_graph(20, 0.7)
G4 = nx.fast_gnp_random_graph(20, 0.8)
G5 = nx.fast_gnp_random_graph(20, 0.5)
G6 = nx.fast_gnp_random_graph(20, 0.6)

path = "C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier\data\\test_random_walk_files\\"

nx.write_gml(G1, path + "test1.gml.gz")
nx.write_gml(G2, path + "test2.gml.gz")
nx.write_gml(G3, path + "test3.gml.gz")
nx.write_gml(G4, path + "test4.gml.gz")
nx.write_gml(G5, path + "test5.gml.gz")
nx.write_gml(G6, path + "test6.gml.gz")



