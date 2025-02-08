import math
from collections import deque
from typing import List, Tuple, Any, Dict


class Tree:
    def __init__(self, number_of_possible_children, parent, ebene, children_cost, cost):
        self.number_of_possible_children = number_of_possible_children
        self.children = []
        self.ebene = ebene
        self.is_leaf = True
        self.data_structure = None

        self.parent = parent
        self.children_cost = children_cost
        self.cost = cost

    def get_smallest_cost(self, current_min_cost, required_cost):
        # Get node with the smallest cost and open children spots
        if required_cost < self.cost < current_min_cost and len(self.children) < self.number_of_possible_children:
            return self.cost, self

        min_cost = current_min_cost
        best_node = None

        for child in self.children:
            child_cost, child_node = child.get_smallest_cost(min_cost, required_cost)

            if child_cost < min_cost:
                min_cost = child_cost
                best_node = child_node
        return min_cost, best_node

    def add_child(self, required_cost):
        cost, node = self.get_smallest_cost(math.inf, required_cost)

        if node.is_leaf:
            node.is_leaf = False
            node.children.append(Tree(self.number_of_possible_children, node, node.ebene+1, self.children_cost, cost+self.children_cost[0]))
            node.children.append(Tree(self.number_of_possible_children, node, node.ebene+1, self.children_cost, cost+self.children_cost[1]))
        else:
            node.children.append(Tree(self.number_of_possible_children, node, node.ebene+1, self.children_cost, cost+self.children_cost[len(node.children)]))

    def get_size(self) -> int:
        if self.is_leaf:
            return 1
        return sum(child.get_size() for child in self.children)

    def evaluate_tree(self) -> int:
        a = 0
        for child in self.children:
            a += child.evaluate_tree()
        if self.is_leaf:
            a += self.data_structure.commonness * self.cost
        return a

    def delete_node(self, tree_object):
        self.data_structure = None
        if tree_object == self:
            self.is_leaf = True
            self.children = []
        for child in self.children:
            child.delete_node(tree_object)

    def get_highest_value(self, last_value) -> Tuple[int, Any]:
        if self.is_leaf and self.parent.parent is not None:
            return self.data_structure.commonness * self.cost, self.parent

        a = last_value
        to_delete = None
        for child in self.children:
            if child.get_highest_value(last_value)[0] > a:
                a, to_delete = child.get_highest_value(a)
        return a, to_delete

    def create_chain(self) -> List[int]:
        return (self.parent.create_chain() + [self.parent.children.index(self)]) if self.parent else []

    def return_graph(self) -> Dict:
        result = {}
        if self.is_leaf:
            result[self.data_structure.value] = self.create_chain()

        for child in self.children:
            result.update(child.return_graph())

        return result

    def get_highest_cost(self, last_value) -> Tuple[int, Any]:
        if self.is_leaf and self.data_structure is None:
            return self.cost, self

        min_cost = last_value
        node = None
        for child in self.children:
            child_cost, child_node = child.get_highest_cost(min_cost)

            if child_cost > min_cost:
                min_cost = child_cost
                node = child_node
        return min_cost, node

class Data:
    def __init__(self, value, commonness):
        self.value = value
        self.commonness = commonness
