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
# import networkx as nx
# G = nx.Graph()
# s2v_obj = s2v.Sub2Vec()
# G.add_edges_from([("a", "e"), ("a", "c"), ("a", "d"), ("c", "b"), ("b", "e"), ("e", "d")])
# rw_graph = s2v_obj.randomWalk(G)
import classifier.sub2vec.doc2vec as d2v

a = [["a","b","c","d"],["b","k","r","t"],["c","d","f","e"],["e","k","r","y"],["g","h","c","d"]]
d2v_obj = d2v.Doc2Vec(a)
d2v_obj.Doc2Vec()