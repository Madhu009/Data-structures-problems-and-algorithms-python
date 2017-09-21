class Node(object):

    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.next = None

    def set_data(self,data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self,next_node):
        self.next = next_node

    def get_next(self):
        return self.next
