class Solution:
    def delete_node(self, head, x):
        # code here
        if not head:
            return None

        current = head
        count = 1

        # Traverse to the node at the given x
        while current and count < x:
            current = current.next
            count += 1

        # If x is more than number of nodes
        if not current:
            return head

        # If node to be deleted is head
        if current.prev is None:
            head = current.next
            if head:
                head.prev = None
        else:
            current.prev.next = current.next

        if current.next:
            current.next.prev = current.prev

        return head


# {
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    @staticmethod
    def print_list(node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        head = None
        tail = head

        for i in range(n):
            temp = int(data[index])
            index += 1
            if head is None:
                head = Node(temp)
                tail = head
            else:
                new_node = Node(temp)
                tail.next = new_node
                new_node.prev = tail
                tail = new_node

        x = int(data[index])
        index += 1

        obj = Solution()
        res = obj.delete_node(head, x)

        Node.print_list(res)

# } Driver Code Ends
