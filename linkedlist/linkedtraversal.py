#
# |1|*|----->|2|*|----->|3|*|

#define Node class

class Node:
    #function to initalize node
    def __init__(self,data):
        self.data = data
        self.next = None

#define LinkedList class
class LinkedList:
    #function to initialize head
    def __init__(self):
        self.head = None

    #define a function to insert new node at the beginning
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #define a new function to insert a node after a given previous node
    def insert(self, prev_node, new_data):
        if prev_node is None:
            print('given previous node do not exist in linkedlist')
            return
        
        new_node = Node(new_data) #create new node
        new_node.next = prev_node.next #make next of new node as next of previous node
        prev_node.next = new_node #set next of previous node as the new node


    #define a new function to append data at the end.
    def append(self,new_data):
        new_node = Node(new_data) # create a new node and put the new data
        if self.head is None: # ie if linkedlist is empty
            self.head = new_node
            return
        #else by defualt traverse till end of linkedlist
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node

    #define a function to traverse and print linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.insert(llist.head,10) #insert 10 after head ie 1
    llist.insert(llist.head.next,5) #insert 5 after 10
    llist.append(20) #append 20 after 3 or at the end of linked list
    llist.append(21)
    llist.printList() #call printlist function 