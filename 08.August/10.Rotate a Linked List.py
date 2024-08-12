# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:

    # Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if not head or k == 0:
            return head

        # Step 1: Find the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Step 2: Calculate effective rotations
        k = k % length
        if k == 0:
            return head

        # Step 3: Locate the k-th node
        current = head
        for i in range(k - 1):
            current = current.next

        # Step 4: Rotate the list
        new_head = current.next
        current.next = None  # Break the list here

        # Move to the end of the new list
        end = new_head
        while end.next:
            end = end.next

        # Attach the original head at the end of new list
        end.next = head

        return new_head


# {
 # Driver Code Starts
# Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


# Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        k = int(data[idx + 1].strip())
        idx += 2
        head = Solution().rotate(head, k)
        printList(head)
        t -= 1

# } Driver Code Ends