class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
        #
    def getNext(self):
        return self.next
        #
    def setData(self,newdata):
        self.data = newdata
        #
    def setNext(self, newnext):
        self.next = newnext
        #

class ListQ(object):

    def __init__(self):
        self.sizenumber = 0
        self.last = None
        self.head = None

    def __str__(self):			    #Utgår ifrån att alla noders paylods bara kommer vara text strängar
        s = ""
        p = self.head
        while p != None:
            s = s +" "+ str(p.data)
            p = p.next
        return s
    def put(self,x):
        if self.head == None:       #Om kedjan är tom, så sätts noden först
            temp = Node(x)
            temp.setNext(None)
            self.head = temp
            self.last = temp
        else:                       #Om kedjan innehåller noder, sätts den som sist
            temp = Node(x)
            self.last.setNext(temp)
            self.last = temp
        self.sizenumber += 1
    def get(self):                  #Visar elementet först i kön, och tar sedan bort det från kedjan.
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = temp.next
            self.sizenumber -= 1
            return temp.getData()
    def peek(self,position=None):
        if position ==self.last:
            return self.last
        else:
            if self.head is None:
                return None
            else:
                return self.head
    def isEmpty(self):
        empty = (self.sizenumber == 0)
        return empty
    def size(self):
        return self.sizenumber