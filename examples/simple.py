import numpy as np
from graphbutler import recipe, Graph, save_all

@recipe
def sine_wave():
    g = Graph()
    g.x = np.arange(0.0, 10.0, 0.01)
    g.y = np.sin(g.x)
    return g

if __name__ == '__main__':
    save_all()
