class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


class LinkedList():
    def __init__(self):

        # head of list
        self.head = None

    def push(self, head_ref, data):

        new_node = Node(data)
        new_node.down = head_ref
        head_ref = new_node

        return head_ref

    def printList(self):

        temp = self.head
        while (temp != None):
            print(temp.data, end=" ")
            temp = temp.down

        print()

    # An utility function to merge two sorted linked lists
    def merge(self, a, b):

        if (a == None):
            return b

        if (b == None):
            return a

        result = None

        if (a.data < b.data):
            result = a
            result.down = self.merge(a.down, b)
        else:
            result = b
            result.down = self.merge(a, b.down)

        result.right = None
        return result

    def flatten(self, root):

        if (root == None or root.right == None):
            return root

        root.right = self.flatten(root.right)

        # now merge
        root = self.merge(root, root.right)

        return root


L = LinkedList()

''' 
Let us create the following linked list
                       7
                       ^
                       |
            10 -> 1 -> 3 -> 9
                 |     |     
                 V     V     
                 8     4  -> 5
                 |          
                 V          
            2 <- 6         



'''
L.head = L.push(L.head, 9);
L.head = L.push(L.head, 3);
L.head = L.push(L.head, 2);
L.head = L.push(L.head, 1);

L.head.right = L.push(L.head.right, 7);
L.head.right = L.push(L.head.right, 4);
L.head.right.right = L.push(L.head.right.right, 8);
L.head.right.right = L.push(L.head.right.right, 5);

L.head.right.right.right = L.push(L.head.right.right.right, 10);
L.head.right.right.right = L.push(L.head.right.right.right, 6);

# flatten the list
L.head = L.flatten(L.head);

L.printList()