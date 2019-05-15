def KSubstring(stringIn, K, Tp):
# Write your code here
    res = set()
    hmap = {}
    le = 0
    s = stringIn
    for ri in range(len(s)):
        ch = s[ri]
        if ch not in hmap:
            hmap[ch] = 0
        hmap[ch] += 1
        if ri-le+1 > K:
            hmap[s[le]] -= 1
            if hmap[s[le]] == 0:
                del hmap[s[le]]
            le += 1
        if len(hmap) == Tp and ri - le + 1 == K:
            res.add(s[le:ri+1])
    print(res)
    return len(res)