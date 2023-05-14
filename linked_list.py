class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        node = self.head
        node = None

    def append(self, data):
        node = self.head

        if node is None:
            node = Node(data)
            return

        while node is not None:
            node = node.next
        node.next = Node(data)




























class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):

        if self.head is None:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def remove(self,target):
        node = self.head

        if node == target:
            node = node.next
            return

        previous = None
        while node is not None:
            if node.data == target:
                previous.next = node.next
            previous = node
            node = node.next
        
    def reverse(self):
        node = self.head
        previous = None

        while node is not None:
            link = node.next
            node.next = previous
            previous = node
            node = link
        self.head = previous

    
    def __str__(self):
        str1 = ""
        node = self.head
        while node is not None:
            str1 += str(node.data) + " --> "
            node = node.next
        return str1

    

var = Linked_list()
var.append(5)
var.append(8)
var.append(18)
var.append("afifi")
var.reverse()

print(var)


        
"""node = self.head
        previous = None

        while node is not None:
            next = node.next
            node.next = previous
            previous = node
            node = next
        self.head = previous"""
