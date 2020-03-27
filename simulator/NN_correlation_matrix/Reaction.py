import torch
import torch.nn.functional as F
import random
import copy
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn import cluster
import networkx as nx

class Reaction(torch.nn.Module):
    def __init__(self, sub, prod, eps=1e-20, step=0.0001):
        super(Reaction, self).__init__()
        self._sub = sub.clone()#torch.nn.Parameter(sub.clone())
        self._prod = prod.clone()#torch.nn.Parameter(prod.clone())
        self._step = step
        self._eps = eps

    def forward(self, x):
        y = x
        x = x / self._sub  # required sub
        x = 1 - 1 / x  # the chance to collect all required substrates
        x = F.relu(x)  # nullify negative prob
        x = x.prod(dim=1, keepdim=True)  # total prob to collect all required substrates
        x = x * self._step
        x = y + x * (self._prod - self._sub)
        return x

    def get_def_tensor(self):
        s = torch.unsqueeze(self._sub, 0)
        p = torch.unsqueeze(self._prod, 0)
        return torch.cat((s, p), dim=0)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Reaction(\n\tsub={},\n\t prod={})".format(self._sub, self._prod)