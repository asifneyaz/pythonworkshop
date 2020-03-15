class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
        
s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.push('D')
print(s.get_stack())
s.pop()
print(s.get_stack())
s.pop()
print(s.get_stack())
s.push('C')
print(s.get_stack())