class AA:
    def __init__(self, x):
        if x == 1:
            self.a = AA(0)
            self.b = AA(0)
    def __del__(self):
        pass
    def __iter__(self):
        pass
    def __call__(self):
        pass
aa = AA(1)
gg = {1:2,3:4,5:7}
del aa.a, aa.b, gg[1], gg[5]
print gg

class meuh:
    attr = 4
    def __init__(self):
        b = self.attr
#        self.attr = 2 XXX add warning
meuh()

#*WARNING* 6.py:6: '__del__' is not supported
#*WARNING* 6.py:8: '__iter__' is not supported
#*WARNING* 6.py:10: '__call__' is not supported
#*WARNING* 6.py:6: function (class AA, '__del__') not called!
#*WARNING* 6.py:14: attribute won't be deleted
#*WARNING* 6.py:20: class attribute 'attr' accessed without using class name