import unittest
import os
import graphbutler

class GraphPathTest(unittest.TestCase):
    def setUp(self):
        self.graph = graphbutler.Graph()

    def test_no_name_raises(self):
        with self.assertRaisesRegexp(AttributeError, "Graph must have filename or recipe."):
            self.graph.path(".")

    def test_with_dir(self):
        self.graph.filename = "graph.svg"
        self.assertEqual(self.graph.path(os.path.join("a", "b")), os.path.join("a", "b", "graph.svg"))

    def test_no_extension(self):
        self.graph.filename = "graph"
        self.assertEqual(self.graph.path("."), os.path.join(".", "graph.svg"))

class GraphRecipePathTest(unittest.TestCase):
    def test_from_recipe(self):
        @graphbutler.recipe
        def graph_recipe_test():
            return graphbutler.Graph()

        self.assertEqual(graph_recipe_test().path("."), os.path.join(".", "graph_recipe_test.svg"))

class ParameterizedTest(unittest.TestCase):
    def setUp(self):
        template = lambda a: 2 * a
        values = range(3)
        self.param = graphbutler.Parameterized("a", template, values)

    def test_values(self):
        results = [res for res, _ in self.param]
        self.assertEqual([0, 2, 4], results)

    def test_labels(self):
        labels = [label for _, label in self.param]
        self.assertEqual(["a = 0", "a = 1", "a = 2"], labels)
