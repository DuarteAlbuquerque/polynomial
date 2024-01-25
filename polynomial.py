class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " / " + repr(self.p2)

    def evaluate(self, x):
        try:
            return self.p1.evaluate(x) / self.p2.evaluate(x)
        except ZeroDivisionError:
            print("Error: Division by zero")
            return None

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Add, Sub, Div)):
            repr_p1 = "( " + repr(self.p1) + " )"
        else:
            repr_p1 = repr(self.p1)
        
        if isinstance(self.p2, (Add, Sub, Div)):
            repr_p2 = "( " + repr(self.p2) + " )"
        else:
            repr_p2 = repr(self.p2)

        return repr_p1 + " * " + repr_p2

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)


poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(-1))
