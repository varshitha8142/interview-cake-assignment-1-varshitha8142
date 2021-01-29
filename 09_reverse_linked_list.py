""" Write a function for reversing a linked list.
Your function will have one input: the head of the list.
Your function should return the new head of the list.

Here's a sample linked list node class:

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None   """

# Start coding from here
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=0
for i in range(7):
    if(head==0):
        head=node(i)
        n=head
    else:
        n.next=node(i)
        c=n
        n=n.next
p=head
print("Before Reverse linked list:")
while(p!=None):
    print(p.data)
    p=p.next 
def f(p):
    global head
    prev = None
    while p:
        n = p.next
        p.next = prev 
        prev = p  
        p = n  
    head = prev
f(head) 
print("Reverse linked list:")
while(n!=None):
    print(n.data)
    n=n.next
