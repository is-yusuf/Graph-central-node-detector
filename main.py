import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque

b = 0 
def generate(n,ruinit):
    global b 
    b = int(random.random()*n )
    G = nx.DiGraph()

    G.add_nodes_from(range(1, n))

    for i in range(n):
        if i == b:
            continue
        G.add_edge(i, b)

    for i in range(n):
        if i == b:
            continue
        for j in range(n):
            if j == b:
                continue
            if i != j and random.random() < 0.2:  
                G.add_edge(i, j)


    lucky_ruiner = int(random.random()*n ) 
    while lucky_ruiner == b:
        lucky_ruiner = int(random.random()*n ) 
    ruinit and G.add_edge(b, lucky_ruiner)
    adj_matrix = nx.to_numpy_array(G, nodelist=sorted(G.nodes()))


    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700, font_size=18)
    return adj_matrix


def find_bigwig(adj_matrix):
    n = len(adj_matrix)
    
    u = 1
    v = 0
    
    while u < n:
        if adj_matrix[u][v]:
            u += 1
        else:
            v = u
            u += 1
    
    for i in range(n):
        if i == v :
            continue
        if adj_matrix[v][i]:
            print(f"{v} can't be because {i}")
            return False
        if not adj_matrix[i][v]:
            print(f"{v} can't be because {i}")
            return False
    return v
    

counts = []
for i in range (1):
    ruined = round(random.random(),0)
    ruined = 1 
    adj_matrix = generate(25,ruined)

    result = find_bigwig(adj_matrix)
    counts.append(result)

    if (result and ruined) or (result and (result !=  b)) :
        print("supposed to be:", b ,ruined)
        print("Bigwig node:", result)
    plt.show()


