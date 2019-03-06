class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        split_path = path.split("/")
        for val in split_path:
            if not val or val == '.':
                continue
            elif val == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(val)
        ans = ''
        if not res:
            return '/'
        else:
            for val in res:
                ans += ('/' + val)
            return ans