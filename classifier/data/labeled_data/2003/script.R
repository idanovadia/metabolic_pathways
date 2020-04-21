## some short explanations
## three networks for three seasons: 2001, 2003, and 2004

## trainset: positive instances which correspond to tomato pathways found in each network: 169
## trainset: negative instances which correspond to metacyc pathways found in each network: 163
##-----note: only 85 were chosen randomly for trainset, the rest were allocated to test set----#
## trainset: negative instances:random pathways of lengths 2 to 18 which that were defined to be
##      found in all three networks: 85
## testset: pathways that were found in other plants but not in tomato: 33 


## the three networks
write.csv(as.matrix(as_adjacency_matrix(tom.01.graph)),'tomato_2001_network.csv')
write.csv(as.matrix(as_adjacency_matrix(tom.03.graph)),'tomato_2003_network.csv')
write.csv(as.matrix(as_adjacency_matrix(tom.04.graph)),'tomato_2004_network.csv')

# tomato pathways within networks - positive instances trainset
network_list <- IL.2004.pathways  # change variables here for each run, i.e. IL.2001.pathways, IL.2003.pathways, IL.2004.pathways
network <- tom.04.graph  # change variables here for each run, i.e. tom.01.graph, tom.03.graph, tom.04.graph
netw_name <-  'trainset_tomatocycpathway_2004_' # change variables here for each run, see above

count <- 0
for(i in overlap.ind){   # overlap.ind is a variable that was created before
    count <- count + 1
    n_n <- paste(netw_name,as.character(network_list[[i]]$pathway),'_',count,'.csv',
                 sep="")
    snx <- match(tolower(network_list[[i]]$overlap),tolower(V(network)$names))
    write.csv(as.matrix(as_adjacency_matrix(induced.subgraph(network,snx ))),n_n)
}
    
    
# trainset of random pathways
network_list <- random.pathway.list
network <- tom.04.graph  # change variables here for each run, i.e. tom.01.graph, tom.03.graph, tom.04.graph
netw_name <- 'random_pathway_2004'  # change variables here for each run, see above

for(i in 1:length(network_list)){
    n_n <- paste(netw_name,"_",i,".csv",sep="")
    snx <- match(tolower(network_list[[i]]$random_metabolites),tolower(V(network)$names))
    write.csv(as.matrix(as_adjacency_matrix(induced.subgraph(network,snx ))),n_n)
}

# metacyc pathways within networks - negative instances trainset
# object: synced.tomato.non.tomato.list

network_list <- synced.tomato.non.tomato.metacyc.list
network <- tom.04.graph  # change variables here for each run, i.e. tom.01.graph, tom.03.graph, tom.04.graph
netw_name <- 'trainset_metacycpathway_2004_' # change variables here for each run, see above

for(i in 1:length(network_list)){
    n_n <- paste(netw_name,as.character(network_list[[i]][[1]][[1]]$pathway),'_',i,'.csv',
                 sep="")
    snx <- match(tolower(network_list[[i]][[1]][[1]]$overlap),tolower(V(network)$names))
    write.csv(as.matrix(as_adjacency_matrix(induced.subgraph(network,snx ))),n_n)
}

# plant pathways that were not find in tomato - testset
# object: synced.tomato.non.tomato.list

network_list <- synced.tomato.non.tomato.list
network <- tom.04.graph  # change variables here for each run, i.e. tom.01.graph, tom.03.graph, tom.04.graph
netw_name <- 'testset_pathway_2004_' # change variables here for each run, see above

for(i in 1:length(network_list)){
    n_n <- paste(netw_name,as.character(network_list[[i]][[1]][[1]]$pathway),'_',i,'.csv',
                 sep="")
    snx <- match(tolower(network_list[[i]][[1]][[1]]$overlap),tolower(V(network)$names))
    write.csv(as.matrix(as_adjacency_matrix(induced.subgraph(network,snx ))),n_n)
}

