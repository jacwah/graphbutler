import numpy as np
from scipy.stats import chi2
from graphbutler import recipe, save_all, Graph, Parameterized

@recipe
def chi_squared_pdf():
    g = Graph()

    g.title = "Chi-squared probability density"
    g.x = np.arange(0.0, 9.0, 0.01)

    g.y = Parameterized("k", lambda k: chi2.pdf(g.x, k), (1, 2, 3, 5, 9))
    # k=1 is unbounded
    g.y_max = 0.5

    return g

if __name__ == "__main__":
    # chi_squared_pdf().show()
    save_all(format="png")
