import gensim.models.doc2vec as doc
import os
import random
import networkx as nx


def getDegreeLabelledGraph(G, rangetoLabels):
    G.remove_edges_from(G.selfloop_edges())
    degreeDict = G.degree(G.nodes())
    # print(degreeDict)
    # labelDict = {}
    for node in degreeDict._nodes:
        val = 0
        if float(nx.number_of_edges(G)) != 0:
            val = degreeDict[node] / float(nx.number_of_edges(G))
        G.nodes[node]["MyDegree"] = inRange(rangetoLabels, val)
    # G = nx.relabel_nodes(G, labelDict)
    return G


def inRange(rangeDict, val):
    for key in rangeDict:
        if key[0] < val and key[1] >= val:
            return rangeDict[key]


def subGraphsCreator(subGraphs_list):
    rangetoLabels = {(-1, 0.05): 'z', (0.05, 0.1): 'a', (0.1, 0.15): 'b', (0.15, 0.2): 'c',
                     (0.2, 0.25): 'd',
                     (0.25, 0.5): 'e', (0.5, 0.75): 'f', (0.75, 1.0): 'g'}
    graphs = []
    for subgraph in subGraphs_list:
        graphs.append(getDegreeLabelledGraph(subgraph, rangetoLabels))
    return graphs
