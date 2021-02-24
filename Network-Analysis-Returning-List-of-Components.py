# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:00:35 2021

@author: arnou
"""
import networkx as nx
#from nxviz import CircosPlot
import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt

from itertools import count
import warnings

warnings.filterwarnings('ignore')

df2011 = pd.read_csv('https://raw.githubusercontent.com/myvioletrose/data620_team/master/assignment/week_4/high-school-social-network2011.txt',
                 sep='\t',
                 header=None,
                 names=['t', 'i', 'j','Ci','Cj'])

attributes2011 = pd.read_csv('http://www.sociopatterns.org/wp-content/uploads/2015/09/metadata_2011.txt',
                  sep='\t',
                  header=None,
                  names=['node', 'dept','gender'])



# edge2011
edge2011 = df2011.loc[:,'t':'j'].groupby(['i', 'j']).count().reset_index()
edge2011.columns = ['student_id1', 'student_id2', 'freq']



# undirected graph
undirected_G = nx.Graph()

# adding edges to graph 
for idx in edge2011.index:    
    p1 = edge2011.loc[idx]['student_id1'].item()
    p2 = edge2011.loc[idx]['student_id2'].item()
    w = edge2011.loc[idx]['freq'].item()
    undirected_G.add_edge(p1, p2, weight = w)    



sorted(nx.connected_components(undirected_G), key = len, reverse=True)