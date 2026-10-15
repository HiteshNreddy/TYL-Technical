class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return None
        value = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def delete_end(self):
        if self.tail is None:
            print("List is empty")
            return None
        value = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def search(self, value):
        temp = self.head
        pos = 1
        while temp is not None:
            if temp.data == value:
                return pos
            temp = temp.next
            pos += 1
        return -1

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        print("None", end=" <-> ")
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


def main():
    dll = DoublyLinkedList()
    dll.insert_beginning(20)
    dll.insert_beginning(10)
    dll.insert_end(30)
    print("Doubly Linked List:")
    dll.display()
    print("Position of 20:", dll.search(20))
    print("Position of 50:", dll.search(50))
    print("Deleted from beginning:", dll.delete_beginning())
    print("Deleted from end:", dll.delete_end())
    dll.display()


if __name__ == "__main__":
    main()
