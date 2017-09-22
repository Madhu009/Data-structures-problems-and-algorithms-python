from Node import Node


class LinkedList(object):

    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None
        self.length = 0

    # O(n) # O(1) if tail is there
    def insertend(self, new_node):
        new_node = Node(new_node)
        print("new node is getting added", new_node.data)

        if self.head == None:
            self.head = new_node
            self.length += 1
        else:
            temp = self.head

            while temp.get_next() != None:
                temp = temp.get_next()

            temp.set_next(new_node)
            new_node.set_prev(temp)
            self.length += 1

    # O(1)
    def insertbefore(self, new_node):
        new_node = Node(new_node)
        print("new node is getting added before head", new_node.data)

        if self.head == None:
            self.head = new_node
            self.length += 1
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
            self.length += 1

    # O(n)
    def insertposition(self, new_node, position):
        if position > self.length + 1:
            raise ValueError("The position exceeds the length")
        if position == 1:
            raise Exception("The head is present there")

        new_node = Node(new_node)

        print("new node is adding at {} : {}".format(position, new_node.data))

        temp = self.head
        for i in range(position - 2):
            temp = temp.get_next()

        new_node.set_prev(temp)
        new_node.set_next(temp.get_next())

        if temp.get_next()!=None:
            temp.get_next().set_prev(new_node)
        temp.set_next(new_node)

        self.length += 1

    # O(1)
    def deletehead(self):
        curr = self.head.data

        self.head = self.head.get_next()
        self.head.set_prev(None)
        self.length -= 1
        print("current head {} is deleted new head is :{} ".format(
            curr, self.head.data))

    # O(n)
    def deleteposition(self, position):

        if position > self.length:
            raise ValueError("The position exceeds the length")
        if position == 1:
            self.deletehead()
            return 0

        temp = self.head
        for i in range(position - 1):
            temp = temp.get_next()

        print("deleting the node at {} : {}".format(
            position, temp.data))

        temp.get_prev().set_next(temp.get_next())
        if temp.get_next() != None:
            temp.get_next().set_prev(temp.get_prev())

        self.length -= 1

    # O(n)
    def deletematched(self, data):
        temp = self.head
        if temp.data == data:
            self.deletehead()
            return

        while temp != None:

            if temp.data == data:

                print("deleting the matched node :{}".format(data))

                temp.get_prev().set_next(temp.get_next())
                if temp.get_next() != None:
                    temp.get_next().set_prev(temp.get_prev())

                self.length -= 1
                return

            temp = temp.get_next()

        if temp == None:
            print("data is not found")

    # O(n)
    def getposition(self, data):
        temp = self.head
        if temp.data == data:
            return 1
        pos = 2
        while temp.get_next() != None:
            if temp.get_next().data == data:
                return pos
            pos += 1
            temp = temp.get_next()

        if temp.get_next() == None:
            print("data is not found")
            return None

    # O(n)
    def printlist(self):
        temp = self.head
        print('*' * 50)
        print("Current linked list is ")
        print("header is ", temp.data)
        print("[", end=" ")

        while temp != None:
            print(temp.data, end=" ")
            reversetemp=temp
            temp = temp.get_next()
        print("]")
        self.printreverselist(reversetemp)

    def printreverselist(self,temp):
        print("[", end=" ")
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.get_prev()
        print("]")
