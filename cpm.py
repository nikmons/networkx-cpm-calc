from __future__ import division
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

from matplotlib.patches import Rectangle

import pandas as pd
import random
import string
import csv

COLORS = ["Red", "Green", "Cyan", "Green", "Pink", "Grey", "White", "Yellow"]
SIZE = range(1, 20)

pos = {"Y1": (10,20), "Y2": (20, 10), "Y3": (20,20), "Y4": (20,30), "Y5": (30, 0), "Y6": (30, 10), "Y7": (30, 25), "Y8": (40, 5), "Y9": (50, 15), "Y10": (60, 15)}
#node_attrs = dict.fromkeys(pos.keys())
node_attrs = {key:{} for key in pos.keys()}
edges = [("Y1","Y2"),("Y1","Y3"),("Y1","Y4"),("Y2","Y5"),("Y2","Y6"),("Y3","Y7"),("Y4","Y7"),("Y5","Y8"),("Y6","Y8"),
        ("Y7","Y9"),("Y8","Y9"),("Y9","Y10")]

attrs = ["color", "size", "name", "desc"]

data = pd.read_csv("data.csv")
print(data)

node_data = {x:{} for x in data.iloc[:,0]}
# for r in data.iloc[0:data.shape[1]-1]:
#     print(r)

print(data.iloc[0:5])

for index,row in data.iterrows():
    key = row["Task"]
    for r in row.items():
        node_data[key][r[0]] = r[1]
            
data = data.replace({pd.np.nan: None})
print(node_data)

for key,val in node_attrs.items():
    for att in attrs:
        if att == "color":
            node_attrs[key][att] = str(random.choice(COLORS))
        elif att == "size":
            node_attrs[key][att] = str(random.choice(SIZE))
        elif att == "name":
            node_attrs[key][att] = key
        elif att == "desc":
            node_attrs[key][att] = "".join([random.choice(string.ascii_letters) for i in range(10)])
        else:
            pass

#print(node_attrs)

f, ax = plt.subplots(1,1, figsize=(8,5))
G = nx.DiGraph()

G.add_nodes_from(pos.keys())
G.add_edges_from(edges)

#nx.draw_networkx_nodes(G,pos=nx.spring_layout(G))
#nx.draw_networkx_edges(G,pos=nx.spring_layout(G))
#sorted({"\n".join(x for v in node_attrs.itervalues() for x in v)})
#print(val for key,val in node_attrs.items())

flat_dict = {}
for key,val in node_attrs.items():
    flat_dict[key] = "\n".join(str(x) for x in node_attrs[key].values())
#print(flat_dict)

node_colors = {}
for key,val in node_attrs.items():
    #print(key, val)
    node_colors[key] = val['color']

color_map = []
for key,val in node_attrs.items():
    color_map.append(val['color'])
#print(flat_dict)
#
#nx.draw(G, pos, labels=flat_dict,node_color=color_map)
nx.draw_networkx_nodes( \
    G, pos, node_size=1500, node_color=color_map, alpha=0.4, \
    node_shape='s')

nx.draw_networkx_labels(G, pos, labels=flat_dict, font_size=8)

nx.draw_networkx_edges(G, pos)

#ax.add_patch(Rectangle((0.25,0.25), 0.5, 0.5, linewidth=1, edgecolor='b', facecolor='none'))
plt.show()
