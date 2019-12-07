import pytest
from contextlib import ExitStack as does_not_raise
from collections import defaultdict


class Node:
    def __init__(self):
        self.dependencies = set()
        self.dependents = set()


class Graph:
    def __init__(self):
        self.nodes = defaultdict(Node)

    def add_edge(self, val, dependency=None):
        if dependency is not None:
            self.nodes[val].dependencies.add(dependency)
            self.nodes[dependency].dependents.add(val)
        else:
            self.nodes[val]  # initialise key with empty type


class Solution:
    def get_build_order(self, projects, dep_array):
        """
        Given a list of projects and a list of project dependencies (d, p), where project p
        is dependant on project d, return a valid build order.

        :param projects: A list of projects
        :param dep_array: A list of dependencies
        :return: A list in a valid build order
        """
        graph = self.build_graph(projects, dep_array)
        return self.get_build_order_from_graph(graph)

    def build_graph(self, projects, dep_array):
        graph = Graph()
        for project in projects:
            graph.add_edge(project)

        for dependency, project in dep_array:
            graph.add_edge(project, dependency)

        return graph

    def add_nodes_with_no_dependencies(self, build_order, projects, graph):
        for project in projects:
            if len(graph.nodes[project].dependencies) == 0:
                build_order.append(project)

    def get_build_order_from_graph(self, graph):
        build_order = []
        self.add_nodes_with_no_dependencies(build_order, graph.nodes.keys(), graph)

        for i in range(len(graph.nodes.keys())):
            if len(build_order) <= i:
                return None

            project = build_order[i]
            for dependent_project in graph.nodes[project].dependents:
                # Remove 'project' as dependencies from dependents
                if project in graph.nodes[dependent_project].dependencies:
                    graph.nodes[dependent_project].dependencies.remove(project)

            # Add any of those dependants to the build order that now have not dependencies
            self.add_nodes_with_no_dependencies(build_order, graph.nodes[project].dependents, graph)

        return build_order


testdata = [
    (
        (
            ['a', 'b', 'c', 'd', 'e', 'f'],
            [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
         ),
        ['e', 'f', 'b', 'a', 'd', 'c'],
        does_not_raise()
    ),
    (
        (
            ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            [('f', 'c'), ('f', 'a'), ('f', 'b'), ('c', 'a'), ('b', 'a'), ('a', 'e'), ('b', 'e'), ('d', 'g')]
        ),
        ['d', 'f', 'g', 'b', 'c', 'a', 'e'],
        does_not_raise()
    ),
    (
        (
            ['a', 'b', 'c'],
            [('a', 'b'), ('b', 'c'), ('c', 'a')]
        ),
        None,
        does_not_raise()
    ),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_build_order(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
