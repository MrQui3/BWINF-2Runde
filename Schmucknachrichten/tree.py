from collections import deque


class Tree:
    def __init__(self, number_of_possible_children, parent, ebene):
        self.number_of_possible_children = number_of_possible_children
        self.children = []
        self.ebene = ebene
        self.is_leaf = True
        self.data_structure = None
        self.queue = deque([self])
        self.parent = parent

    def add_child(self, min_ebene):
        """ Fügt einen neuen Knoten auf der untersten, noch nicht vollen Ebene ab `min_ebene` ein. """
        queue = [self]  # Jedes Mal eine neue Queue für die Breitensuche
        while queue:
            node = queue.pop(0)  # Nächstes Element aus der Liste nehmen (FIFO-Prinzip)

            # Falls wir die gewünschte Ebene erreicht haben, prüfen, ob wir hier einfügen können
            if node.ebene >= min_ebene and len(node.children) < node.number_of_possible_children:
                new_child = Tree(node.number_of_possible_children, ebene=node.ebene + 1, parent=node)
                node.children.append(new_child)
                node.is_leaf = False  # Ist kein Blatt mehr

                # Setze is_right_sibling auf True, wenn der Knoten nicht das erste Kind ist
                if len(node.children) > 1:
                    new_child.is_right_sibling = True

                return new_child  # Erfolgreich eingefügt, also abbrechen

            # Falls kein Platz mehr im aktuellen Knoten ist, die Kinder für die nächste Runde speichern
            queue.extend(node.children)

    def get_size(self):
        if self.is_leaf:
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
        if self.data_structure is None and self.is_leaf:
            self.data_structure = Data(value, self.ebene, commonness)
            return True

    def evaluate_tree(self):
        a = 0
        for child in self.children:
            a += child.evaluate_tree()
        if self.is_leaf:
            try:
                a += self.data_structure.commonness * self.ebene
            except:
                print("fehler")
                print(self)
        return a

    def insert_new_node(self, number):
        if self.is_leaf:
            self.is_leaf = False
            for i in range(number):
                self.children.append(Tree(self.number_of_possible_children, self, self.ebene + 1))
        else:
            self.children[0].insert_new_node(number)

    def delete_node(self, tree_object):
        self.data_structure = None
        if tree_object == self:
            self.is_leaf = True
            self.children = []
        for child in self.children:
            child.delete_node(tree_object)

    def get_highest_value(self, last_value):
        if self.is_leaf and self.parent.parent is not None:
            return self.data_structure.commonness * self.ebene, self.parent

        a = last_value
        to_delete = None
        for child in self.children:
            if child.get_highest_value(last_value)[0] > a:
                a, to_delete = child.get_highest_value(last_value)
        return a, to_delete

    def check_if_root_is_valid(self):

        if len(self.children) > self.number_of_possible_children:
            print(len(self.children))
            print(self.number_of_possible_children)
        for child in self.children:
            child.check_if_root_is_valid()


class Data:

    def __init__(self, value, ebene, commonness):
        self.value = value
        self.ebene = ebene
        self.commonness = commonness
