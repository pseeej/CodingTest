class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud = moves.count("U") - moves.count("D")
        if ud != 0:
            return False
        lr = moves.count("R") - moves.count("L")
        if lr != 0:
            return False

        return True
