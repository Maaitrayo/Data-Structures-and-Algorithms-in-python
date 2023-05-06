class Node:
    def __init__(self, data=None, next=None) :
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        
        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    
    def insert_at(self,index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0
        while itr:
            if data_after == itr.data:
                self.insert_at(count+1, data_to_insert)
            
            itr = itr.next
            count += 1
    # def insert_after_value(self, data_after, data_to_insert):
    #     itr = self.head
    #     while itr:
    #         if data_after == itr.data:
    #             node = Node(data_to_insert, itr.next)
    #             itr.next = node
    #         else:
    #             raise Exception("Data not found")
            
    #         itr = itr.next
    
    def remove_by_value(self, data):
        itr = self.head
        count = 0
        while itr:
            if data == itr.data:
                self.remove_at(count)
            
            itr = itr.next
            count += 1


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)

def exercise_1():
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

def tut():
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_end(40)
    ll.insert_values(['ok', 'hello', 'me', 'us'])
    ll.print()
    ll.remove_at(2)
    ll.insert_at(2,'among')
    ll.print()
    print("length", ll.get_length())

if __name__ == '__main__':
    tut()
    exercise_1()