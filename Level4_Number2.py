class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
class LinkedList:
    def __init__(self):
        self.head = None

    def sum_of_lastN_nodes(self, point, lNodes):
        current = self.head
        sum = 0

        while current is not None:
            if current.value == point:
                count = 0
                temp = current.next

                while temp is not None:
                    sum += temp.value
                    count += 1

                    if count == lNodes:
                        break

                    temp = temp.next

            current = current.next

        return sum


node1 = Node(5)
node2 = Node(10)
node3 = Node(6)
node4 = Node(4)
node5 = Node(1)
node6 = Node(12)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

linkedlist = LinkedList()
linkedlist.head = node1
print(linkedlist.sum_of_lastN_nodes(6, 3))