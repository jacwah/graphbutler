#!/usr/bin/env python

import os
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

        if isinstance(self.y, tuple):
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
        print("Saving %s to %s" %(self.__class__.__name__, path))

        self.draw_to(plt.figure())
        plt.savefig(path)


if __name__ == "__main__":
    class SineGraph(Graph):
        title = "Sine curve"
        x = np.arange(0.0, 10.0, 0.01)
        y = (
            (1 * np.sin(x), "A = 1"),
            (2 * np.sin(x), "A = 2")
        )

    SineGraph().show()
