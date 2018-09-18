class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)

'''
    Write code to remove duplicates from an unsorted linked list.
'''
def remove_dups(node):
    if(node != None):
        dict = {node.val:1}
        prev = node
        node = node.next
        while(node != None):
            if(dict.get(node.val) != None):
                prev.next = node.next
            else:
                dict[node.val] = 1
                prev = node
            node = node.next

'''
 Implement an algorithm to find the kth to last element of a singly linked list.
'''
def find_kth_to_last(node, k):
    runner = node
    while(k > 0):
        node = node.next
        k -= 1

    while(runner != None):
        node = node.next
        runner = runner.next
    return node

def partition(node, x):
    head = node
    tail = node

    while(node != None):
        next = node.next #keep track of next value
        if(node.val < x):
            node.next = head
            head = node
        else:
            node.next = tail
            tail = node
        node = next
    tail.next = None
    return head


def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(1)
    n4 = Node(0)
    n3.next = n4
    n2.next = n3
    n1.next = n2
    partition(n1, 2)
    print(n1)

main()
