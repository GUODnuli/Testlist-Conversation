class TreeNode:
    def __init__(self, id: str, title: str, step: str, result: str, level: int):
        self.id = id
        self.title = title
        self.step = step
        self.result = result
        self.level = level
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)