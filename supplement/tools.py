import math
from typing import List
import matplotlib.pyplot as plt


def plot_distribution_comparison(histograms: List[List[float]], legend: List[str], title: str):
    
    # Check if histograms and legend are empty
    if not histograms:
        raise ValueError("Histograms list is empty.")
    if not legend:
        raise ValueError("Legend list is empty.")

    # Check if the number of histograms matches the number of legend entries
    if len(histograms) != len(legend):
        raise ValueError("Number of histograms does not match the number of legend entries.")

    # Determine the length of the longest histogram
    max_length = max(len(hist) for hist in histograms)

    # Extend the shorter histograms
    for i in range(len(histograms)):
        while len(histograms[i]) < max_length:
            histograms[i].append(0.0)  # Extend with zeros

    # Plot histograms
    for hist in histograms:
        plt.plot(range(len(hist)), hist, marker='x')

    # Set axis labels
    plt.xlabel('Degree')
    plt.ylabel('Probability')

    # Finish the plot
    plt.legend(legend)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def poisson(k: int, lamb: float) -> float:
    
    if k < 0:
        raise ValueError("k must be a non-negative integer.")
    if lamb <= 0:
        raise ValueError("λ must be positive.")

    # Initialize the result
    result = 1.0

    # Calculate e^-λ
    exp_neg_lambda = math.exp(-lamb)
    result *= exp_neg_lambda

    # Calculate λ^k
    lambda_power_k = lamb ** k
    result *= lambda_power_k

    # Calculate k!
    factorial_k = math.factorial(k)
    result /= factorial_k

    return result

def poisson_histogram(n_nodes: int, n_edges: int, max_degree: int) -> List[float]:
    
    # Calculate lambda from the numbers of nodes and number of edges
    lamb = (2 * n_edges) / n_nodes

    # Initialize the histogram list
    histogram = []

    # Compute the Poisson distribution for all k in the range [0, max_degree]
    for k in range(max_degree + 1):
        # Compute P(k) using the Poisson distribution formula
        poisson_prob = poisson(k, lamb)
        histogram.append(poisson_prob)

    return histogram