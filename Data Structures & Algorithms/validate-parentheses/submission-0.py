from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        openbrack = {"(" , "{", "["}
        match = {")" : "(", "}" : "{", "]" : "["}
        openstack = deque()
        for b in s:
            if b in openbrack:
                openstack.append(b)
            elif b in match and openstack:
                if match[b] != openstack[-1]:
                    return False
                else:
                    openstack.pop()
            else:
                return False
                        
        return not openstack    