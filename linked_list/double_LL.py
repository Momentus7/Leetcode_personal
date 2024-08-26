class DoubleLL:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
    
    def __str__(self):

        return str(self.val)


Head=Tail=DoubleLL(1)

def display(Head):
    curr=Head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr=curr.next
    print("<->".join(elements))

display(Head)

def insert_at_begin(head,tail,val):
    new_node=DoubleLL(val,next=head)
    head.prev=new_node
    return new_node,tail

Head,Tail=insert_at_begin(Head,Tail,3)

display(Head)