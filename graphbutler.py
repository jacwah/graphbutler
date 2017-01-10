#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

"""Represents the graph of a mathematical function.

When defining a graph, subclass this class and provide an x and y numpy array."""
class Graph(object):
    title = None

    """Draw the graph to a matplotlib figure."""
    def draw_to(self, figure):
        figure.suptitle(self.title)
        axes = figure.gca()
        axes.plot(self.x, self.y)

    """Draw the graph in a GUI frontend through pyplot."""
    def show(self):
        figure = plt.figure()
        self.draw_to(figure)
        plt.show()

if __name__ == "__main__":
    class SineGraph(Graph):
        title = "Sine curve"
        x = np.arange(0.0, 10.0, 0.01)
        y = np.sin(x)

    SineGraph().show()
