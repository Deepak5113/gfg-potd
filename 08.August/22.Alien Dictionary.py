# User function Template for python3

from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Your implementation here
        graph = defaultdict(list)
        in_degree = [0] * k

        for i in range(n - 1):
            word1, word2 = dict[i], dict[i + 1]
            min_len = min(len(word1), len(word2))

            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[ord(word1[j]) - ord('a')
                          ].append(ord(word2[j]) - ord('a'))
                    in_degree[ord(word2[j]) - ord('a')] += 1
                    break
        queue = deque()
        for i in range(k):
            if in_degree[i] == 0:
                queue.append(i)

        order = []
        while queue:
            u = queue.popleft()
            order.append(chr(u + ord('a')))

            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(order) == k:
            return ''.join(order)
        else:
            return ""


# {
 # Driver Code Starts
# Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends
