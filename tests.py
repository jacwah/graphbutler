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
