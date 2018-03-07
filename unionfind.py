class setUnion(object):
    """Union-Find data structure"""

    def __init__(self, nElements):
        self.nElements = nElements
        self.parent = [i for i in range(1, nElements + 1)]
        self.parent.insert(0, None)
        self.size = [1 for i in range(1, nElements + 1)]
        self.size.insert(0, None)
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])    

    def unionSets(self, s1, s2):
        r1 = self.find(s1)
        r2 = self.find(s2)

        if r1 == r2:
            return

        elif self.size[r1] >= self.size[r2]:
            self.size[r1] = self.size[r1] + self.size[r2]
            self.parent[r2] = r1
            return

        else: 
            self.size[r2] = self.size[r1] + self.size[r2]
            self.parent[r1] = r2
            return

    def sameComponent(self, s1, s2):
        return self.find(s1) == self.find(s2)




unionFind = setUnion(10)
print(unionFind.nElements, unionFind.parent, unionFind.size)
