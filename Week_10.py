#Week 10

def maxCountKey(d):
    d = dict(sorted(d.items(), key = lambda x:x[1],reverse = True))
    for k in d:
        return k

def maxWordCounts(d,n):
    d = dict(sorted(d.items(), key = lambda x:x[1],reverse = True))
    keys = []
    vals = []
    ans = []
    count = 0
    for k in d:
        if(count >= n):
            break
        if(count < n):
            keys.append(k)
            vals.append(d[k])
        count = count + 1
    ans.append(keys)
    ans.append(vals)
    return ans
