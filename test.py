def foo1(b,b1=3):
    print("foo1 called",b,b1)
def foo2(c):
    foo3(c)
    print("foo2 called",c)
    return
def foo3(d):
    print("foo3 called",d)
    return
def main():
    print("main called")
    foo1(100,101)
    foo2(200)
    print("main ending")
main()
import sys
print(sys.getrecursionlimit())

n = int(input("please input one num: "))
def func(n):
    return 1 if n == 1  else n*func(n-1)
result = func(n)
print(str(n)+"! result is " + str(result))
