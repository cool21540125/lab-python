class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(": ")", "[": "]", "{": "}"}
        unresolved = ""
        for idx, item in enumerate(s):
            if item in map.keys():
                unresolved += item
            elif unresolved != "" and item == map[unresolved[len(unresolved) - 1]]:
                unresolved = unresolved[0 : len(unresolved) - 1]
            else:
                return False
        return unresolved == ""
