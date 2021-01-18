class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next =  next 

class Linkedlist :
    def __init__ (self):
        self.head=None

    def insertbegin(self,data):
        node = Node(data, self.head)
        self.head = node

    def insertend(self,data):

        if self.head == None:
            self.head = Node(data)
            return
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data)        

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr =''
        while itr :
            llstr = llstr+ str(itr.data) +'--->'
            itr=itr.next
        print(llstr)

    def newlist(self,plist):
        self.head=None
        for data in plist:
            self.insertend(data)

    def removat(self,ind):
        if ind <0 :
            raise Exception("INvalid index passed")

        if ind ==0:
            self.head= self.head.next
            return

        itr = self.head
        i=0
        for i in range(ind-1):
            itr=itr.next
        itr.next= itr.next.next 

    def insertat(self, ind, data) :
        if ind <0:
            raise Exception("INvalid index")

        if ind==0:
            self.insertbegin(data)
            return
        cnt= 0
        itr = self.head
        while itr :
            if cnt == ind -1:
                node = Node(data,itr.next)
                itr.next=node
                break
            itr= itr.next
            cnt=cnt+1    
        

if __name__=='__main__':
    ll= Linkedlist()
    ll.newlist(['avi','jeet','parth','darsh'])
    ll.removat(1)
    ll.insertat(2,"mehta")

    ll.print()

