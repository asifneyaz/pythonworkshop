# define a class for node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, data):
        self.next = data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def add_node(self, node):
        if self.length == 0:
            self.add_at_beg(node)
        else:
            self.add_at_end(node)

    def add_at_beg(self, node):
        new_node = node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def add_at_end(self, node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        node.next = None
        current_node.next = node
        self.length = self.length + 1

    def print_linked_list(self):
        node_list = []
        current_node = self.head
        while current_node is not None:
            node_list.append(current_node.data)
            current_node = current_node.next

        print(node_list)


if __name__ == '__main__':
    linked_list_object = LinkedList()
    node0 = Node(7)

    node1 = Node(7)
    node2 = Node(5)
    node3 = Node(3)
    node4 = Node(1)
    linked_list_object.add_node(node0)
    linked_list_object.add_node(node1)
    linked_list_object.add_node(node2)
    linked_list_object.add_node(node3)
    linked_list_object.add_node(node4)
    linked_list_object.print_linked_list()



































# # Node of a Singly Linked List
# class Node:
#     # constructor
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     # method for setting the data field of the node
#
#     def set_data(self, data):
#         self.data = data
#
#     # method for getting the data field of the node
#
#     def get_data(self):
#         return self.data
#
#     # method for setting the next field of the node
#
#     def set_next(self, data):
#         self.next = data
#
#     # method for getting the next field of the node
#
#     def get_next(self):
#         return self.next
#
#     # returns true if the node points to another node
#
#     def has_next(self):
#         return self.next is not None
#
#
# # class for defining a linked list
#
#
# class LinkedList:
#
#     # initializing a list
#     def __init__(self):
#         self.length = 0
#         self.head = None
#
#     # method to add a node in the linked list
#     def add_node(self, node):
#         if self.length == 0:
#             self.add_beg(node)
#         else:
#             self.add_last(node)
#
#     # method to add a node at the beginning of the list with a data
#     def add_beg(self, node):
#         new_node = node
#         new_node.next = self.head
#         self.head = new_node
#         self.length += 1
#
#     def add_last(self, node):
#         current_node = self.head
#
#         while current_node.next is not None:
#             current_node = current_node.next
#
#         new_node = node
#         new_node.next = None
#         current_node.next = new_node
#         self.length = self.length + 1
#
#     def print_list(self):
#         node_list = []
#         current_node = self.head
#         while current_node is not None:
#             node_list.append(current_node.data)
#             current_node = current_node.next
#
#         print(node_list)
#
#
# node1 = Node(7)
# node2 = Node(2)
# node3 = Node(8)
# node4 = Node(4)
# node5 = Node(5)
# node5.set_next = None
#
# ll = LinkedList()
# ll.add_node(node1)
# ll.add_node(node2)
# ll.add_node(node3)
# ll.add_node(node4)
# ll.add_node(node5)
# ll.print_list()
