class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical_list = list(path.split('/'))
        que = []

        for item in canonical_list:
            if item == '.': continue
            elif item  == '..':
                if que:
                    que.pop()
            elif len(item) > 0:
                que.append(item)

        return "/" + "/".join(que)