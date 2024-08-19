import tools
from time import time
from typing import List, Tuple, Union
from random_network import RandomNetwork


def plot(title: str, data: List[Tuple[int, int]]):
    """
    Generates random networks based on the specified number and edges, computes the degree distribution of each network,
    and then plots all degree distribution into a single plot.

    :param title: plot title
    :param data: list of (n, m) pairs, where n is the number of nodes and m is the number of edges
    """
    plot_data = []                                                          # type: List[List[Union[int, float]]]
    plot_legend = []                                                        # type: List[str]

    print(title + ':')
    for n_nodes, n_edges in data:
        # Note: Here we make use of formatted strings, which will automatically insert and format variables within the
        # curly brackets. The ":," after the variables means that commas should be inserted as thousands-indicators.
        # For example, if n_nodes = 3456, then the string will format the number as 3,456.
        print(f'\tnodes: {n_nodes:,}, edges: {n_edges:,}')

        # build the random network
        start = time()
        network = RandomNetwork(n_nodes, n_edges)
        # Note: The ":.2f" after the time differential means that it will round the number to 2 decimal places.
        print(f'\t--> generated random network in {time() - start:.2f}s')

        # compute the normalised degree distribution histogram
        start = time()
        plot_data.append(network.normalized_degree_distribution())
        plot_legend.append('r: {0:,}/{1:,}'.format(n_nodes, n_edges))
        print(f'\t--> computed degree distribution in {time() - start:.2f}s')

        # build the histogram of the Poisson distribution
        start = time()
        plot_data.append(tools.poisson_histogram(n_nodes, n_edges, network.max_degree()))
        plot_legend.append('p: {0:,}/{1:,}'.format(n_nodes, n_edges))
        print(f'\t--> computed Poisson distribution in {time() - start:.2f}s')

    tools.plot_distribution_comparison(plot_data, plot_legend, title)


# This if-statement "guards" the function calls below it. With it, the two function calls are only executed when this
# file is executed as a script. Without it, the two function calls would be executed every time this file is imported,
# e.g. to make use of the plotting function above somewhere else. In this assignment we are not doing that, but it is
# still good practice to always "guard" function calls this way.
if __name__ == '__main__':
    plot('Plot 1', [(50, 100), (500, 1000), (5000, 10000), (50000, 100000)])
    plot('Plot 2', [(20000, 5000), (20000, 17000), (20000, 40000), (20000, 70000)])
