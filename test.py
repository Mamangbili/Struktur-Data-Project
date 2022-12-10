class node:
    def __init__(self,y):
        self.x = 10
        self.y = 10+y

    def __hash__(self) -> int:
        return hash((self.x,self.y,self.z))

    def __eq__(self, __o: object) -> bool:
        if self.x == __o.x and self.y == __o.y : return True
        return False

b = node(1)
c = node(2)

w = 1,2,3

print(type(w))



