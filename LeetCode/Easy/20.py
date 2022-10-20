class Solution:
    def isValid(self, sentence: str) -> bool:
        brkts = []
        types = {"(", "[", "{"}
        
        for s in sentence:
            if s in types:
                brkts.append(s)
            elif s == ")" and brkts and brkts[-1] == "(":
                brkts.pop()
            elif s == "}" and brkts and brkts[-1] == "{":
                brkts.pop()
            elif s == "]" and brkts and brkts[-1] == "[":
                brkts.pop()
            else:
                return False
            
        if len(brkts) == 0:
            return True
        else:
            return False
