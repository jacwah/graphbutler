import os
import functools
import matplotlib.pyplot as plt

# See http://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D
LINE_OPTIONS = {
    "linewidth": 2
}

"""Represents the graph of a mathematical function.

When defining a graph, subclass this class and provide an x and y numpy array."""
class Graph(object):

    def __init__(self):
        self.axes_options = {}

    """Draw the graph to a matplotlib figure."""
    def draw_to(self, figure):
        try:
            figure.suptitle(self.title)
        except AttributeError:
            pass

        axes = figure.gca(**self.axes_options)

        if isinstance(self.y, Parameterized):
            for (y, label) in self.y:
                axes.plot(self.x, y, label=label, **LINE_OPTIONS)
            axes.legend()
        else:
            axes.plot(self.x, self.y, **LINE_OPTIONS)

    """Draw the graph in a GUI frontend through pyplot."""
    def show(self):
        figure = plt.figure()
        self.draw_to(figure)
        plt.show()
        plt.close()

    """Return the path where the graph will be saved by save()."""
    def path(self, dir, format="svg"):
        try:
            fn = getattr(self, "filename", None) or self.recipe.__name__
        except AttributeError:
            raise AttributeError("Graph must have filename or recipe.")

        extension = "." + format.lower()
        if not fn.lower().endswith(extension):
            fn += extension

        return os.path.join(dir, fn)

    """Save the graph as an SVG file."""
    def save(self, dir, format="svg"):
        path = self.path(dir, format=format)
        print("Saving graph to %s" %path)

        self.draw_to(plt.figure())
        plt.savefig(path)
        plt.close()

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

recipes = set()

"""Decorator for graph recipes.

Use this decorator to register recipes with save_all."""
def recipe(func):
    @functools.wraps(func)
    def wrapper():
        graph = func()
        graph.recipe = wrapper
        return graph

    recipes.add(wrapper)
    return wrapper

"""Save all recipes as SVG files."""
def save_all(dir=None, format="svg"):
    if dir is None:
        dir = os.getcwd()

    for recipe in recipes:
        recipe().save(dir, format=format)
