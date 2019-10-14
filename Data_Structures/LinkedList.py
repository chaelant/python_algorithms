"""
Singly Linked List Implementation
"""

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self, initial):
        self.head = Node(initial)

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def insertAtTail(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

        return True

    def insertAtHead(self, data):
        new_node = Node(data)
        curr = self.head
        self.head = new_node
        self.head.next = curr
        return True

    def insertAfterVal(self, target, data):
        curr = self.head
        new_node = Node(data)

        while curr.next and curr.val != target:
            curr = curr.next

        if curr.val == target:
            tmp = curr.next
            curr.next = new_node
            new_node.next = tmp
            return True
        else:
            return False

    def insertBeforeVal(self, target, data):
        curr = self.head
        new_node = Node(data)
        prev = None

        while curr.next and curr.val != target:
            prev = curr
            curr = curr.next

        if curr.val == target:
            prev.next = new_node
            new_node.next = curr
            return True
        else:
            return False

    def removeVal(self, target):
        curr = self.head
        prev = None
        while curr.next and curr.val != target:
            prev = curr
            curr = curr.next

        if curr.val == target:
            prev.next = curr.next
            curr.next = None
            return True
        else:
            return False


linked = LinkedList(5)
linked.insertAtTail(7)
linked.insertAtTail(8)
linked.insertAtHead(4)
linked.insertAtHead(2)
linked.insertAfterVal(5, 6)
linked.insertBeforeVal(4, 3)
linked.traverse()
linked.removeVal(8)
linked.traverse()



    

    

    
