import ctypes

clib = ctypes.cdll.LoadLibrary('./c/main.so')
cpplib = ctypes.cdll.LoadLibrary('./cpp/main.so')
golib = ctypes.cdll.LoadLibrary('./go/main.so')

clib.hello()
print(clib.sum(5, 6))

cpplib.hello()
print(cpplib.sum(6, 7))

golib.Hello()
print(golib.Sum(7, 8))
