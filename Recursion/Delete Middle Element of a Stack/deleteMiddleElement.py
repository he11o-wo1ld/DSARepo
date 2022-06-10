class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
        
    def deleteMiddleElement(self):
        if self.height is None:
            return
            
        k = (self.height // 2) + 1
        
        ans = self.helper(self.height, k)
        
        return ans
        
        
    def helper(s, k):
        if k == 1:
            return s
        
        temp = s.pop()
        s.pop()
        self.helper(self.hight, k-1)
        s.push(tmp)
        return s


S = Stack(None)

S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
S.print_stack()
S.deleteMiddleElement()
