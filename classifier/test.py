import classifier.preprocessing as pre

pre_obj = pre.Preprocessing("C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier\\data\\metabolic_profile_xls\\2001_fruit_pericarp_metabolite.xlsx",
                  "C:\\Users\\idanf\\PycharmProjects\\metabolic_pathways_new\\classifier\\data\\metabolic_profile_output_repro")
pre_obj.fillNaToMean()
pre_obj.saveFile()