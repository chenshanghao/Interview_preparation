class Solution:
    """
    @param tagList: The tag list.
    @param allTags: All the tags.
    @return: Return the answer
    """
    def getMinimumStringArray(self, tagList, allTags):
        # Write your code here
        dict1, dict2 = {}, {}
        for i in tagList:
            dict1[i] = 1
            dict2[i] = 0
        m, n = len(tagList), len(allTags)
        cnt = 0
        ans = n + 1
        l, r = 0, -1
        while (r < n):
            if cnt < m:
                r += 1
                if r == n:
                    break
                if allTags[r] in dict1:
                    dict2[allTags[r]] += 1
                    if dict2[allTags[r]] == 1:
                        cnt += 1
            else:
                if (allTags[l] in dict1):
                    dict2[allTags[l]] -= 1
                    if dict2[allTags[l]] == 0:
                        cnt -= 1
                l += 1
            if cnt == m:
                ans = min(ans, r - l + 1)
        
        return ans if ans != n+1 else -1
        