from collections import deque, defaultdict


class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.parent = None

    def __repr__(self):
        return str(self.val)

    def to_array(self):
        output = []
        queue = deque()
        queue.appendleft((self, 0))
        while queue:
            node, level = queue.pop()

            if len(output) < level+1:
                output.append([])

            output[level].append(node.val)
            for child in node.children:
                if child is not None:
                    queue.appendleft((child, level+1))
        return output

    def to_string(self):
        return "\n".join([" ".join([str(val) for val in level]) for level in self.to_array()])

    def height(self, height=0):
        height += 1
        child_heights = []
        for child in self.children:
            child_heights.extend([child.height(height)] if child is not None else [])
        child_heights.append(height)
        return max(child_heights)


class BinaryNode(Node):
    LEFT = 0
    RIGHT = 1

    def __init__(self, val=None):
        super().__init__(val)
        self.children.extend([None, None])

    @property
    def left(self):
        return self.children[self.LEFT]

    @left.setter
    def left(self, node):
        if node:
            node.parent = self
        self.children[self.LEFT] = node

    @property
    def right(self):
        return self.children[self.RIGHT]

    @right.setter
    def right(self, node):
        if node:
            node.parent = self
        self.children[self.RIGHT] = node

    def in_order(self, result=None):
        if result is None:
            result = []
        if self.left:
            self.left.in_order(result)
        result.append(self.val)
        if self.right:
            self.right.in_order(result)
        return result

    @staticmethod
    def from_array(source):
        if not source:
            return None

        targets = [BinaryNode(source[0])]  # initialise root node

        p_s = 1  # source pointer
        p_t = 0  # target pointer
        child_idx = BinaryNode.LEFT

        while p_s < len(source):
            if source[p_s] is not None:
                node = BinaryNode(source[p_s])
            else:
                node = None
            targets.append(node)

            if targets[p_t] is not None:
                if node:
                    node.parent = targets[p_t]
                targets[p_t].children[child_idx] = node

            if child_idx == BinaryNode.RIGHT:
                p_t += 1
            child_idx ^= 1  # toggle left/right
            p_s += 1

        return targets[0]
