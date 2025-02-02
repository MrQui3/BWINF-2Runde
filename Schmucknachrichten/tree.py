from collections import deque
class Tree:
    def __init__(self, number_of_possible_children, ebene=0):
        self.number_of_possible_children = number_of_possible_children
        self.children = []
        self.ebene = ebene
        self.data = True
        self.data_structure = None
        self.which_child = 0

    def add_child(self):
        """ Fügt einen neuen Knoten auf der untersten Ebene ein. """
        queue = deque([self])  # Starte mit der Wurzel
        while queue:
            node = queue.popleft()  # Nehme das nächste Element aus der Queue

            if len(node.children) < node.number_of_possible_children:
                # Falls Platz für ein neues Kind, füge es hier hinzu
                new_child = Tree(node.number_of_possible_children, node.ebene + 1)
                node.children.append(new_child)
                node.data = False  # Der Knoten ist nun kein Blatt mehr
                return new_child  # Gib das neue Blatt zurück

            # Falls der Knoten voll ist, überprüfe seine Kinder
            queue.extend(node.children)

    def get_size(self):
        if self.data:
            return 1
        return sum(child.get_size() for child in self.children)

    def pre_order(self):
        print(self.ebene, len(self.children))
        for child in range(len(self.children)):
            self.children[child].pre_order()

    def fill_tree_data(self, value, commonness):
        for child in self.children:
            if child.fill_tree_data(value, commonness):
                return True
        if self.data_structure is None and self.data:
            self.data_structure = Data(value, self.ebene, commonness)
            return True

    def evaluate_tree(self):
        a = 0
        for child in self.children:
            a += child.evaluate_tree()
        if self.data:
            a += self.data_structure.commonness*self.ebene
        return a


class Data:

    def __init__(self, value, ebene, commonness):
        self.value = value
        self.ebene = ebene
        self.commonness = commonness
