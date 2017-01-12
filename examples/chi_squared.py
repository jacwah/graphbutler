import numpy as np
from scipy.stats import chi2
from graphbutler import recipe, save_all, Graph, Parameterized

@recipe
def chi_squared_pdf():
    g = Graph()
    g.title = "Chi-squared probability density"
    g.x = np.arange(0.0, 9.0, 0.01)

    def y(k):
        y = chi2.pdf(g.x, k)
        # Value threshold because k=1 is unbounded
        y[y > 0.5] = np.nan
        return y

    g.y = Parameterized("k", y, (1, 2, 3, 5, 9))
    return g

if __name__ == "__main__":
    # chi_squared_pdf().show()
    save_all(format="png")
