class vec3:
    def __init__(self):
       e=1
    def __int__(self,e0:float,e1:float,e2:float):
        self.e=[e0,e1,e2]

    def x(self)->float:
        return self.e[0]
    def y(self)->float:
        return self.e[1]
    def z(self)->float:
        return self.e[2]