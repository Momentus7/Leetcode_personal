class SingleLL:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)

Head=SingleLL(1)
A=SingleLL(2)
B=SingleLL(3)
C=SingleLL(4)

Head.next=A
A.next=B
B.next=C


curr=Head

while curr:
    print(curr)
    curr=curr.next
    


def display(head):
    curr=head
    elements=[]

    while curr:
        
        elements.append(str(curr.val))
        curr=curr.next

    print( "->".join(elements))

display(Head)


def search(head,val):
    curr=head
    while curr:
        if val==curr.val:
            return True
        curr=curr.next
    return False

print(search(Head,3))