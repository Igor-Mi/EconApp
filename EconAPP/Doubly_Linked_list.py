class Node:#a class of individual nodees
    def __init__(self,value,previous,nex):#sets up a simple node
        self.value=value#current entity pointer
        self.prev=previous#next node
        self.next=nex#previous node
        
class Dlist:#a class for the whole list
    def __init__(self):#sets up the list
        self.__head=None#pointer to the start of the list
        self.__tail=None#pointer to the end of the list
        self.__set={}#a set containg all the nodes
        self.__pt=None#pointer to the current item
        
    def add(self,value,ct):#adds a value to the list
        self.__set[ct]=Node(value,self.__tail,None)#makes the new node
        if(self.__head==None):#checks if the node becomes the new head
            self.__head=ct
        else:
            self.__set[self.__tail].next=ct

        self.__tail=ct
        
    def reset(self):#sets the current pointer back to the start
        self.__pt=self.__head
        
    def get(self):#returns the current item
        if(self.__pt!=None):
            return self.__set[self.__pt]
        
    def ret(self,pos):#returns an item with a given id in the set
        return self.__set[pos];
    
    def next(self):#moves to the next node in the list
        if(self.__pt!=None):#checks if there is a next
            self.__pt=self.__set[self.__pt].next
        
    def previous(self):#moves to the previous node
        if(self.__pt!=None):#checks if there is a previous
            self.__pt=self.__set[self.__pt].previous
            
    def delete(self,current):
        #skips over the current node in a forward direction
        self.__set[self.__set[current].prev].next=self.__set[current].next
        
        #skips over the Node in a backwards direction
        self.__set[self.__set[current].next].prev=self.__set[current].prev

        if(current==self.__head):#checks if it deleted the head
            self.__head=self.__set[current].next#makes the next item the head

        if(current==self.__tail):#checks if it delted the tail
            self.__tail=self.__set[current].prev#makes the previous item the tail

        del self.__set[current]#removes the node


