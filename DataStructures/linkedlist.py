class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

node2 = Node()
node1 = Node("data of node1",node2)

class Linkedlist():
    def __init__(self):
        self.head = None
        self.last_node = None


    def print_linkedlist(self):
        linkedlists_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            linkedlists_string += f" {str(node.data)} ->"
            node = node.next_node

        linkedlists_string += "None"
        print(linkedlists_string)

    def insert_beginning(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.insert_beginning(data)

        if self.last_node is None:
            node = self.head
            while node.next_node:
                print("iterate through every node",node.data)
                node = node.next_node

            node.next_node = Node(data,None)
            self.last_node = node.next_node

        else:
            self.last_node.next_node = Node(data,None)
            self.last_node = self.last_node.next_node


linkedlist = Linkedlist()
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_beginning("data")
linkedlist.insert_at_end("end")
linkedlist.insert_at_end("end2")
linkedlist.print_linkedlist()


