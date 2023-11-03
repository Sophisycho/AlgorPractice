class Node:
    # * 在def __init__(self, valie)這一行的self的意思是等待未來不特定創建的實例傳進來，例如未來創建一個my_linked_list的實例，這邊的self就會是my_linked_list
    def __init__(self, value):
        # * 下面的self.vlaue那一行是把右邊的value賦值給self(這裡是new_node實例)的value，這邊其實就只是在設定實例的屬性
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node  # 所以這行的意思就是設定這個LL的head是newnode
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    # def prepend(self, value):
    # def insert(self, index, value):

    def print_list(self):
        temp = self.head  # 把LL中的head賦值給temp
        while temp is not None:  # ? 如果這個LL只有一個node那不就不會print出來?
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
