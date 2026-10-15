class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
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
            self.tail.next = self.head
        return value

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return None
        value = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = self.head
        return value

    def search(self, value):
        if self.head is None:
            return -1
        temp = self.head
        pos = 1
        while True:
            if temp.data == value:
                return pos
            temp = temp.next
            pos += 1
            if temp == self.head:
                return -1

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("back to head")


def main():
    cll = CircularLinkedList()
    cll.insert_beginning(20)
    cll.insert_beginning(10)
    cll.insert_end(30)
    print("Circular Linked List:")
    cll.display()
    print("Position of 20:", cll.search(20))
    print("Position of 50:", cll.search(50))
    print("Deleted from beginning:", cll.delete_beginning())
    print("Deleted from end:", cll.delete_end())
    cll.display()


if __name__ == "__main__":
    main()
