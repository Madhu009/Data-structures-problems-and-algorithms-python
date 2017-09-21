from LinkedList import LinkedList

linkedlist = LinkedList()

linkedlist.insertend(10)
linkedlist.insertend(20)
linkedlist.insertend(30)
linkedlist.insertend(40)
linkedlist.insertbefore(5)
linkedlist.insertposition(50,6)
linkedlist.deletehead()
linkedlist.deleteposition(5)
linkedlist.deletematched(20)

position=linkedlist.getposition(50)
print(position)

linkedlist.printlist()

