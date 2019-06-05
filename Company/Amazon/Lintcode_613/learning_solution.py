'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import collections
import heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        hmap = collections.defaultdict(list)
        for x in results:
            id, score = x.id, x.score
            if len(hmap[id]) < 5:
                heapq.heappush(hmap[id], score)
            else:
                mini = heapq.heappop(hmap[id])
                mini = max(score, mini)
                heapq.heappush(hmap[id], mini)
        for id in hmap:
            hmap[id] = sum(hmap[id]) / 5.0
        return hmap