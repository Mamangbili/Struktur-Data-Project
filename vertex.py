from typing import TypeVar
Point = TypeVar('Point')

class Vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, obj: Point):
        try:
            if self.x == obj.x and self.y == obj.y: 
                return True
        except:
            return False

    def __hash__(self) -> int:
        return hash((self.x,self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def get(self):
        return (self.x,self.y)



