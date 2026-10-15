class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return None
        if self.head.next is None:
            value = self.head.data
            self.head = None
            return value
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        value = temp.next.data
        temp.next = None
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
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


def main():
    sll = SinglyLinkedList()
    sll.insert_beginning(20)
    sll.insert_beginning(10)
    sll.insert_end(30)
    print("Singly Linked List:")
    sll.display()
    print("Position of 20:", sll.search(20))
    print("Position of 50:", sll.search(50))
    print("Deleted from beginning:", sll.delete_beginning())
    print("Deleted from end:", sll.delete_end())
    sll.display()


if __name__ == "__main__":
    main()
