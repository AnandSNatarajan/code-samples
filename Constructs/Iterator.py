# All basic python constructs like list, tuple, string are iterators. For an object to be iterable, it should
# define two methods __iter__ and __next__. These are then called from outside as iter() and next() to walk
# through the list.

class pow2:
    def __init__(self, max = 0):
        self.maximum = max

    def __iter__(self):
        self.n = 0
        print(self.maximum)
        return self

    def __next__(self):
        for i in range(self.n+1,self.maximum):
            if (i % 2 == 0):
                self.n = i
                return self
        if (i == self.maximum):
            raise StopIteration

new_obj = pow2(10)
iter_obj = iter(new_obj)
iter_obj = next(iter_obj)
print(iter_obj.n)
new_obj = next(iter_obj)
print(new_obj.n)


# The same effect as above can be achieved by using a python generator
print("\nPython Generator")
def pow2_gen(max):
    for i in range(0,max):
        if (i % 2 == 0):
            yield i
    return -1

a = pow2_gen(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# Using the iterator directly in for loop. This is working because for loop by default uses next
# to iterate through a object. 
for j in pow2_gen(10):
    print(j)

