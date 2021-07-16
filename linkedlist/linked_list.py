
# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None
    # method for setting the data field of the node

    def set_data(self, data):
        self.data = data
    # method for getting the data field of the node

    def get_data(self):
        return self.data
    # method for setting the next field of the node

    def set_next(self, data):
        self.next = data
    # method for getting the next field of the node

    def get_next(self):
        return self.next
    # returns true if the node points to another node

    def has_next(self):
        return self.next is not None

# class for defining a linked list


class LinkedList:
     
    # initializing a list
    def __init__(self):
        self.length = 0
        self.head = None
         
    # method to add a node in the linked list
    def add_node(self, node):
        if self.length == 0:
            self.add_beg(node)
        else:
            self.add_last(node)
             
    # method to add a node at the beginning of the list with a data
    def add_beg(self, node):
        new_node = node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
         
    # method to add a node after the node having the data=data. The data of the new node is value2

    def add_after_value(self, data, node):
        new_node = node
        current_node = self.head
         
        while current_node.next is not None or current_node.data != data:
            if current_node.data == data:
                new_node.next = current_node.next
                current_node.next = new_node
                self.length = self.length + 1
                return
            else:
                current_node = current_node.next
                 
        print("The data provided is not present")
                 
    # method to add a node at a particular position
    def add_at_pos(self, pos, node):
        count = 0
        current_node = self.head
        previous_node = self.head
         
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while current_node.next is not None or count < pos:
                count = count + 1
                if count == pos:
                    previous_node.next = node
                    node.next = current_node
                    self.length += 1
                    return
                     
                else:
                    previous_node = current_node
                    current_node = current_node.next
         
    # method to add a node at the end of a list

    def add_last(self, node):
        current_node = self.head
         
        while current_node.next is not None:
            current_node = current_node.next
 
        new_node = node
        new_node.next = None
        current_node.next = new_node
        self.length = self.length + 1

    # method to delete the first node of the linked list

    def delete_beg(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1
     
    # method to delete the last node of the linked list
    def delete_last(self):
         
        if self.length == 0:
            print("The list is empty")
        else:
            current_node = self.head
            previous_node = self.head
             
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
                 
            previous_node.next = None
             
            self.length -= 1

    # method to delete a node after the node having the given data

    def delete_value(self, data):
        current_node = self.head
        previous_node = self.head
         
        while current_node.next is not None or current_node.data != data:
            if current_node.data == data:
                previous_node.next = current_node.next
                self.length -= 1
                return
                    
            else:
                previous_node = current_node
                current_node = current_node.next
                 
        print("The data provided is not present")
         
    # method to delete a node at a particular position

    def delete_at_pos(self, pos):
        count = 0
        current_node = self.head
        previous_node = self.head
 
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        # to delete the first position of the linked_list
        elif pos == 1:
            self.delete_beg()
            self.length -= 1
        else:        
            while current_node.next is not None or count < pos:
                count = count + 1
                if count == pos:
                    previous_node.next = current_node.next
                    self.length -= 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next
                     
    # returns the length of the list
    def get_length(self):
        return self.length
     
    # returns the first element of the list
    def get_first(self):
        if self.length == 0:
            print("The list is empty")
        else:
            return self.head.data
     
    # returns the last element of the list
    def get_last(self):
         
        if self.length == 0:
            print("The list is empty")
        else:
            current_node = self.head
             
            while current_node.next is not None:
                current_node = current_node.next
                 
            return current_node.data
     
    # returns node at any position
    def get_at_pos(self, pos):
        count = 0
        current_node = self.head
         
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while current_node.next is not None or count < pos:
                count = count + 1
                if count == pos:
                    return current_node.data
                else:
                    current_node = current_node.next
 
    # method to print the whole list

    def print_list(self):
        node_list = []
        current_node = self.head
        while current_node is not None:
            node_list.append(current_node.data)
            current_node = current_node.next
             
        print(node_list)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)



ll = LinkedList()
ll.add_node(node1)
ll.add_node(node2)
ll.add_node(node3)
ll.add_node(node4)
ll.add_node(node5)
ll.print_list()

node5.set_next = None
node4.has_next()
print(id(node1.next))
print(id(node2))
print(id(node3))
print(id(node2.next))
print(node1.has_next())


