# define a class for node
# create a node object and add element to node

# define a class for linked list
# create an object linked list from the class
# call add node method from linked list to add a node
# call delete node method to remove a node
# call print linked list method to print the linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, next_data):
        self.next = next_data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_node(self, node):
        if self.length == 0:
            new_node = node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            self.add_at_end(node)

    def add_at_beg(self, node):
        self.head = node
        self.length += 1

    def add_at_end(self, node):
        current = self.head
        while current is not None:
            current = current.next


    def print_linked_list(self):
        node_list = []
        current_node = self.head
        while current_node is not None:
            node_list.append(current_node.data)
            current_node = current_node.next

        print(node_list)


if __name__ == '__main__':

    node0 = Node(7)
    node1 = Node(8)
    node2 = Node(5)
    node3 = Node(0)
    node4 = Node(1)
    linked_list_object = LinkedList()
    linked_list_object.add_node(node0)
    linked_list_object.add_node(node1)
    linked_list_object.add_node(node2)
    linked_list_object.add_node(node3)
    linked_list_object.add_node(node4)
    linked_list_object.print_linked_list()
    print(hex(id(node0)))
    print(hex(id(node0.next)))
    print(hex(id(node1)))





