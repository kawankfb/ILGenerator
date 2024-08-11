def add_child(node, new_child):
    if node.children is None:
        node.children = [].append(new_child)
    else:
        node.children.append(new_child)


class AST:
    def __init__(self):
        self.root = None
        self.current_number = 0

    def traverse_ast(self, root_node):
        traversal = []
        if len(root_node.children) > 0:
            for child in root_node.children:
                traversal.extend(self.traverse_ast(child))
        node_dict = dict()
        node_dict['label'] = root_node.value
        traversal.append(node_dict)
        return traversal

    class TreeNode:
        def __init__(self, value, children, number):
            self.value = value
            self.children = children
            self.number = number

    def make_node(self, value, children):
        tree_node = self.TreeNode(value, children, self.current_number)
        self.current_number += 1
        return tree_node
