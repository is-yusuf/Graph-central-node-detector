# Bigwig Network Finder

This Python repository contains code to generate a directed graph (DiGraph) using NetworkX and identify a "bigwig" node in it. A "bigwig" node is one that all other nodes point to, but it points to no one (or just one other node, if specified). The graph is visualized using Matplotlib.

## Features

- **Graph Generation**: Generates a directed graph with `n` nodes and random edges.
- **Bigwig Identification**: Identifies the "bigwig" node in the graph, if it exists.
- **Visualization**: Uses Matplotlib to visualize the generated graph.

## How It Works

1. `generate(n, ruinit)`: Generates a directed graph with `n` nodes. One node is randomly selected as the "bigwig" node, and all other nodes point to it. Additional random edges are added with a 20% probability. Optionally, the "bigwig" node can point to one other node if `ruinit` is set to `True`.

2. `find_bigwig(adj_matrix)`: Takes the adjacency matrix of the graph and identifies the "bigwig" node by checking the incoming and outgoing edges.

3. The main loop generates the graph, identifies the "bigwig", and visualizes it using Matplotlib.

## Dependencies

- NetworkX
- Matplotlib
- NumPy
- Python's random and collections modules

## Usage

Run the script to generate a graph with 25 nodes and identify the "bigwig" node in it.
