#!/usr/bin/env python

import os
import functools
import matplotlib.pyplot as plt

"""Represents the graph of a mathematical function.

When defining a graph, subclass this class and provide an x and y numpy array."""
class Graph(object):

    """Draw the graph to a matplotlib figure."""
    def draw_to(self, figure):
        try:
            figure.suptitle(self.title)
        except AttributeError:
            pass

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
        try:
            fn = getattr(self, "filename", None) or self.recipe.__name__
        except AttributeError:
            raise AttributeError("Graph must have filename or recipe.")

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

recipes = []

def recipe(func):
    @functools.wraps(func)
    def wrapper():
        graph = func()
        graph.recipe = wrapper
        return graph

    recipes.append(wrapper)
    return wrapper

def save_all(dir=None):
    if dir is None:
        dir = os.getcwd()

    for recipe in recipes:
        recipe().save(dir)

if __name__ == "__main__":
    import numpy as np

    @recipe
    def sine_graph():
        g = Graph()
        g.x = np.arange(0.0, 10.0, 0.01)
        g.y = Parameterized("A", lambda A: A * np.sin(g.x), (1, 2, 3))
        g.title = "Sine wave"

        return g

    save_all()
