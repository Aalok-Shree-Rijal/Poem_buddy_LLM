class Value:
    def __init__(self, _data, _children=(), _label='', _op=''):
        self._data = _data
        self._grad = 0.00
        self._label = _label
        self._prev = set(_children)
        self._op=_op
        self._backward = lambda: None


    def __repr__(self):
        return f"{self._label} = {self._data}"

    def __add__(self, other):
        out = Value(self._data + other._data, (self, other), _op="+")
        def _backward():
            self._grad += 1.00 * out._grad
            other._grad += 1.00 * out._grad
        out._backward = _backward
        return out
    
    def __mul__(self, other):
        out = Value(self._data * other._data, (self, other), _op="*")
        def _backward():
            self._grad += other._data * out._grad
            other._grad += self._data * out._grad
        out._backward = _backward
        return out

    def backward(self):
        self._grad = 1.00
        # topological sort (kind of similar to TREE in DSA)[https://github.com/aalok-shree-rijal/learning_dsa]
        topo_list = []
        visited = set()
        def topo_build(o):
            if o not in visited:
                visited.add(o)
                for parent in o._prev:
                    topo_build(parent)
            topo_list.append(o)
        topo_build(self)
        for item in reversed(topo_list):
            item._backward()

# from below here experiment different expressions and make your own mini networks, calculate the gradient
# and compare what the code produced by what you got, it is lot more fun

# a = Value(2); a._label = "a"
# b = Value(3); b._label = "b"
# d = Value(3); d._label = "d"

# d = a+a+a; d._label = "d"
# c = a + b; c._label="c"
# e = (a+b)*(a+b); e._label="e"

# e.backward()

# print(a._grad)
# print(b._grad)
# print(c._grad)
# print(d._grad)
# print(e._grad)