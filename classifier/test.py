import classifier.preprocessing as pre

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


import classifier.graph_creator as gc

gc_obj = gc.graph_creator(corr_matrix_path="C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier"
                                           "\\data\\CorrMaxtrix\\CorrMatrix_out_2001_fruit_pericarp_metabolite.xlsx",
                          subGraphs_dir_path= "C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier"
                                              "\\data\\labeled_data\\2001\\trainset")
gc_obj.crete()