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


    def add_child(self):
        """ Fügt einen neuen Knoten auf der untersten, noch nicht vollen Ebene ein. """
        while self.queue:
            parent = self.queue[0]  # Immer der erste Knoten in der Queue bekommt das neue Kind

            # Falls Platz für ein Kind ist, füge es hier hinzu
            if len(parent.children) < parent.number_of_possible_children:
                new_child = Tree(parent.number_of_possible_children, parent, parent.ebene + 1)
                parent.children.append(new_child)
                parent.is_leaf = False  # Eltern-Knoten ist jetzt kein Blatt mehr

                # Das neue Kind wird zur Queue hinzugefügt (potenzieller zukünftiger Eltern-Knoten)
                self.queue.append(new_child)

                # Falls der aktuelle Eltern-Knoten jetzt voll ist, entfernen wir ihn aus der Queue
                if len(parent.children) == parent.number_of_possible_children:
                    self.queue.popleft()

                return new_child

        # Falls alle Kinder voll sind, erweitere das erste Kind
        return self.children[0].add_child()

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
        if self.is_leaf:
            if self.parent.children[0] != self:
                return self.data_structure.commonness * self.ebene, self.parent

        a = last_value
        to_delete = None
        for child in self.children:
            if child.get_highest_value(last_value)[0] > a:
                a, to_delete = child.get_highest_value(last_value)
        return a, to_delete




class Data:

    def __init__(self, value, ebene, commonness):
        self.value = value
        self.ebene = ebene
        self.commonness = commonness
