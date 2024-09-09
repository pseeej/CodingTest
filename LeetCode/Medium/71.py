class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        paths = path.split("/")
        print(paths)
        for name in paths:
            if name == ".":
                continue
            elif name == ".." and len(stack):
                stack.pop()
            elif name == ".." and not len(stack):
                continue
            elif name == "":
                continue
            else:
                stack.append(name)

        return '/'+'/'.join(stack)
