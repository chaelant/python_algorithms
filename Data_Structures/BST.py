"""
Binary Search Tree Implementation
"""

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, initial):
        self.root = Node(initial)

    def insertValue(self, data, r=None):
        if r is None:
            r = self.root
            
        if r.val == data:
            return False

        if data < r.val:
            if r.left:
                return self.insertValue(data, r.left)
            else:
                r.left = Node(data)
                return True
        else:
            if r.right:
                return self.insertValue(data, r.right)
            else:
                r.right = Node(data)
                return True

    def inOrderTraverse(self, r=None):
        if r is None:
            r = self.root

        # when you hit a leaf - base case (you will ALWAYS hit a leaf at some
        # point in a binary tree) (assuming it's a tree and not a general graph)
        if r.left is None and r.right is None:
            print(r.val)
        elif r.left and not r.right:
            self.inOrderTraverse(r.left)
            print(r.val)
        elif r.right and not r.left:
            print(r.val)
            self.inOrderTraverse(r.right)
        else:
            self.inOrderTraverse(r.left)
            print(r.val)
            self.inOrderTraverse(r.right)

    def preOrderTraverse(self, r=None):
        if r is None:
            r = self.root

        if r.left is None and r.right is None:
            print(r.val)
        elif r.left and not r.right:
            print(r.val)
            self.preOrderTraverse(r.left)
        elif r.right and not r.left:
            print(r.val)
            self.preOrderTraverse(r.right)
        else:
            print(r.val)
            self.preOrderTraverse(r.left)
            self.preOrderTraverse(r.right)

    def postOrderTraverse(self, r=None):
        if r is None:
            r = self.root

        if r.left is None and r.right is None:
            print(r.val)
        elif r.left and not r.right:
            self.postOrderTraverse(r.left)
            print(r.val)
        elif r.right and not r.left:
            self.postOrderTraverse(r.right)
            print(r.val)
        else:
            self.postOrderTraverse(r.left)
            self.postOrderTraverse(r.right)
            print(r.val)

    def levelOrderTraverse(self):
        queue = [self.root]
        traversal = []

        while queue:
            current = queue.pop(0)
            if current.left and current.right:
                queue.append(current.left)
                queue.append(current.right)
                traversal.append(current.val)
            elif current.left:
                queue.append(current.left)
                traversal.append(current.val)
            elif current.right:
                queue.append(current.right)
                traversal.append(current.val)
            else:
                traversal.append(current.val)

        return traversal
            
    def inOrderTraverse_Iterative(self):
        stack = []
        current = self.root

        while True:
            if current: 
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.val)
                current = current.right
            else:
                break

    def preOrderTraverse_Iterative(self):
        q = []
        current = self.root

        while True:
            if current: 
                q.append(current)
                current = current.left
            elif q:
                current = q.pop(0)
                print(current.val)
                current = current.right
            else:
                break

    def postOrderTraverse_Iterative(self):
        stack = []
        current = self.root

        while True:
            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left

            current = stack.pop()

            if len(stack) > 0 and current.right and stack[-1] == current.right:
                stack.pop()
                stack.append(current)
                current = current.right
            else:
                print(current.val)
                current = None

            if (len(stack) <= 0):
                break
            
    def findNode(self, target, r=None):
        if r is None:
            r = self.root

        if r.val == target:
            return r
        elif target > r.val:
            if r.right:
                return self.findNode(target, r.right)
            else:
                return None
        else:
            if r.left:
                return self.findNode(target, r.left)
            else:
                return None

    def findParent(self, target, r=None):
        if r is None:
            r = self.root

        if r.right.val == target:
            return r
        elif r.left.val == target:
            return r
        else:
            if target > r.val:
                return self.findParent(target, r.right)
            else:
                return self.findParent(target, r.left)

    def deleteNode(self, target):
        p = self.findNode(target)

        if not p:
            return 'Error: Element does not exist in the tree'


        if not p.right and not p.left:  # p is a leaf
            
            if p == self.root:
                self.root = None
                return None
            
            parent = self.findParent(target)
            if parent.left == p:
                parent.left = None
                return None
            else:
                parent.right = None
                return None
        elif p.left and not p.right:  # p has a left child

            if p == self.root:
                self.root = p.left
                return None
            
            parent = self.findParent(target)
            
            if parent.left == p:
                parent.left = p.left
            else:
                parent.right = p.left
                
        elif p.right and not p.left:  # p has a right child

            if p == self.root:
                self.root = p.right
                return None
            
            parent = self.findParent(target)
            if parent.left == p:
                parent.left = p.right
                return None
            else:
                parent.right = p.right
                return None
        else:  # has two children
            to_swap = p.left

            while to_swap.right:  # find the largest value in the left subtree
                to_swap = to_swap.right

            parent = self.findParent(to_swap.val)
            
            if parent.left == to_swap:
                p.val = to_swap.val
                parent.left = None
                return None
            else:
                p.val = to_swap.val
                parent.right = None
                return None

    def depth(self, r=None):
        if r is None:
            r = self.root

        if not r.left and not r.right:
            return 0
        else:
            if r.left and r.right:
                level = 1 + self.depth(r.left)
                level = 1 + self.depth(r.right)
            elif r.left:
                level = 1 + self.depth(r.left)
            else:
                level = 1 + self.depth(r.right)

        return level
                
    
"""
representation of:

            5
        3       7
     1    4   6    8
     
"""


bst = BST(5)
bst.insertValue(7)
bst.insertValue(3)
bst.insertValue(4)
bst.insertValue(6)
bst.insertValue(1)
bst.insertValue(8)

print('==In-Order Traversal==') # should yield: 1, 3, 4, 5, 6, 7, 8
print('Recursive')
bst.inOrderTraverse()
print('Iterative')
bst.inOrderTraverse_Iterative()

print('==Pre-Order Traversal==')
print('Recursive')
bst.preOrderTraverse()  # should yield: 5, 3, 1, 4, 7, 6, 8
print('Iterative')
bst.preOrderTraverse_Iterative()

print('==Post-Order Traversal==')
print('Recursive')
bst.postOrderTraverse()  # should yield: 1, 4, 3, 6, 8, 7, 5
print('Iterative')
bst.postOrderTraverse_Iterative()



