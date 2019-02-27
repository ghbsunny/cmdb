from dispatcher import Dispatcher

if __name__ == '__main__':
    print("sunny")
    print("welcome to www.ghbsunny.cn")
    dis = Dispatcher()
    dis.run()

n = int(input("please input one num: "))
def func(n):
    return 1 if n == 1  else n*func(n-1)
result = func(n)
print(str(n)+"! result is " + str(result))
