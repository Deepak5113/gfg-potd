# User function Template for python3
'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''

import sys
import io
import atexit


class Solution:

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):

        # code here
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        max_deadline = max(job.deadline for job in Jobs)
        timeline = [-1] * (max_deadline + 1)
        max_profit = 0
        jobs_done = 0

        for job in Jobs:
            for j in range(job.deadline, 0, -1):
                if timeline[j] == -1:
                    timeline[j] = job.id
                    max_profit += job.profit
                    jobs_done += 1
                    break
        return jobs_done, max_profit


# {
 # Driver Code Starts
# Initial Template for Python 3


# Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])

# } Driver Code Ends
