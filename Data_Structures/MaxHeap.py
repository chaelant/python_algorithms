"""
Max Heap implementation

"""

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.count = 1


class MaxHeap:
    def __init__(self, initial):
        self.root = Node(initial)

    def getAvailableParent(self):
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            if current.left and current.right:
                queue.append(current.left)
                queue.append(current.right)
            else:
                return current

    def findNode(self, target):
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            if current.val != target:
                if current.left:
                    if current.left.val == target:
                        return current.left
                    else:
                        queue.append(current.left)
                else:
                    return False

                if current.right:
                    if current.right.val == target:
                        return current.right
                    else:
                        queue.append(current.right)
                else:
                    return False
            else:
                return current

    def findParent(self, target):
        queue = [self.root]

        if self.root.val == target:
            return False
        
        while queue:
            current = queue.pop(0)
            if current.val != target:
                if current.left:
                    if current.left.val == target:
                        return current
                    else:
                        queue.append(current.left)
                else:
                    return False

                if current.right:
                    if current.right.val == target:
                        return current
                    else:
                        queue.append(current.right)
                else:
                    return False
            else:
                return current
    
    def bubbleUpNode(self, target):
        parent = self.findParent(target.val)
        
        if not parent:
            return target.val

        if target.val > parent.val:
            tmp = parent.val
            parent.val = target.val
            target.val = tmp
            return self.bubbleUpNode(parent)
        elif target.val < parent.val:
            return target.val


    def insertValue(self, data):
        # check if value already exists
        exists = self.findNode(data)
        
        if exists:
            exists.count += 1
            return exists.val
            
        
        next_slot = self.getAvailableParent()  # get the parent
        new_node = Node(data)
        if not next_slot.left:  # insert it into the next available, leftmost slot
            next_slot.left = new_node
        else:
            next_slot.right = new_node

        # gradually move up the tree until the parent is greater than the node
        # switching values along the way
        return self.bubbleUpNode(new_node)

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
        

    def getMax(self):
        return self.root.val
    


mx = MaxHeap(80)
mx.insertValue(60)
mx.insertValue(70)
mx.insertValue(50)
mx.insertValue(20)
mx.insertValue(40)
mx.insertValue(55)
mx.insertValue(90)
            
