class Solution:
    def isValid(self, s: str) -> bool:
        match = {")" : "(", "}" : "{", "]" : "["}
        openstack = []
        for b in s:
            if b in match:
                if openstack and openstack[-1] == match[b]:
                    openstack.pop()
                else:
                    return False
            else:
                openstack.append(b)
                        
        return not openstack    