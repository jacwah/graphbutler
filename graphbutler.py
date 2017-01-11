#!/usr/bin/env python

import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

"""Represents the graph of a mathematical function.

When defining a graph, subclass this class and provide an x and y numpy array."""
class Graph(object):

    """Draw the graph to a matplotlib figure."""
    def draw_to(self, figure):
        figure.suptitle(self.title)
        axes = figure.gca()

        if isinstance(self.y, Parameterized):
            for (y, label) in self.y:
                axes.plot(self.x, y, label=label)
            axes.legend()
        else:
            axes.plot(self.x, self.y)

    """Draw the graph in a GUI frontend through pyplot."""
    def show(self):
        figure = plt.figure()
        self.draw_to(figure)
        plt.show()

    """Return the path where the graph will be saved by save()."""
    def path(self, dir):
        fn = reduce(lambda val, name: val or getattr(self, name, None),
            ("filename", "title"), None) or self.__class__.__name__

        if not fn.lower().endswith(".svg"):
            fn += ".svg"

        return os.path.join(dir, fn)

    """Save the graph to the file system."""
    def save(self, dir):
        path = self.path(dir)
        print("Saving graph to %s" %path)

        self.draw_to(plt.figure())
        plt.savefig(path)

"""A parameterized dependent variable.

Use to graph multiple slight variations of the same function together."""
class Parameterized(object):
    def __init__(self, name, template, values):
        self.name = name
        self.template = template
        self.values = values

    def __iter__(self):
        self.index = 0
        return self

    def next(self):
        try:
            value = self.values[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return self.template(value), "%s = %s" %(self.name, value)

if __name__ == "__main__":
    def sine_graph():
        g = Graph()
        g.x = np.arange(0.0, 10.0, 0.01)
        g.y = Parameterized("A", lambda A: A * np.sin(g.x), (1, 2, 3))
        g.title = "Sine wave"

        return g

    sine_graph().save(".")
