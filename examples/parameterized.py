import numpy as np
from graphbutler import recipe, save_all, Graph, Parameterized

@recipe
def sine_waves():
    g = Graph()
    g.x = np.arange(0.0, 10.0, 0.01)
    g.y = Parameterized("A", lambda A: A * np.sin(g.x), (0.5, 1, 2))
    return g

if __name__ == '__main__':
    sine_waves().show()
