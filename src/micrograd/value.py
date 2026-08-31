# The below import is needed only in Day 2
import math

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
        if isinstance(other, (int, float)):
            out = Value(self._data + other, (self, ), _op="+")
        else:
            out = Value(self._data + other._data, (self, other), _op="+")
        def _backward():
            self._grad += 1.00 * out._grad
            if isinstance(other, Value):
                other._grad += 1.00 * out._grad
        out._backward = _backward
        return out

    # constant + (self)
    def __radd__(self, other):
            return self.__add__(other)

    def __sub__(self, other):
            if isinstance(other, (int, float)):
                out = Value(self._data - other, (self, ), _op="-")
            else:
                out = Value(self._data - other._data, (self, other), _op="-")
            def _backward():
                self._grad += 1.00 * out._grad
                if isinstance(other, Value):
                    other._grad += -1.00 * out._grad
            out._backward = _backward
            return out

    # constant - (self)
    def __rsub__(self, other):
        out = Value(other - self._data , (self, ), _op="-")
        def _backward():
            self._grad += -1.00 * out._grad

        out._backward = _backward
        return out
    
    def __mul__(self, other):

        if isinstance(other, (int, float)):
            out = Value(self._data * other, (self, ), _op="*")
        else:
            out = Value(self._data * other._data, (self, other), _op="*")
        def _backward():
            if isinstance(other, Value):
                self._grad += other._data * out._grad
                other._grad += self._data * out._grad
            else:
                self._grad += other * out._grad
        out._backward = _backward
        return out

    # constant * (self)
    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        if isinstance(other, Value):
            out = Value(self._data**other._data, (self, other), _op="**")
        else:
            out = Value(self._data**float(other), (self, ), _op="**")
        def _backward():
            if isinstance(other, Value):
                self._grad += (other._data*((self._data)**(other._data-1))) * out._grad
                other._grad += self._data**other._data * math.log(self._data)

            else:
                self._grad += (other*((self._data)**(other-1))) * out._grad
        out._backward = _backward
        return out

    # constant ** (self)
    def __rpow__(self, other):
        out = Value(float(other) ** self._data, (self,), _op="**")

        def _backward():
            self._grad += (float(other) ** self._data) * math.log(float(other)) * out._grad

        out._backward = _backward
        return out

    # This implimentation was done in day_02, ignore this in day 1
    def tanh(self):
        cal = (math.exp(2*self._data)-1)/(math.exp(2*self._data)+1)
        out = Value(cal, (self,), _op = 'tanh')
        def _backward():
            self._grad += (1 - cal**2) * out._grad
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

# for experiments by using this value class go to (./experiments/day01.py)