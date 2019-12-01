class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.to_array())

    def __eq__(self, other):
        this = self
        while this is not None and other is not None:
            if this.val != other.val:
                return False
            this = this.next
            other = other.next

        if this is not None or other is not None:
            return False

        return True

    @staticmethod
    def from_array(arr):
        dummy = Node()
        p = dummy
        for elem in arr:
            p.next = Node(elem)
            p = p.next
        return dummy.next

    def to_array(self):
        arr = []
        p = self
        while p is not None:
            if len(arr) > 100:
                arr.append('...')
                break
            arr.append(p.val)
            p = p.next
        return arr

    def end(self):
        p = self
        while p.next is not None:
            p = p.next
        return p