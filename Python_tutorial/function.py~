def f(num1,num2):
    print('You called f(x,y) with the value x = ' + str(num1) + ' and y = ' + str(num2))
    print('x * y = ' + str(num1*num2))


f(num1=int(input()),num2=int(input()))


def method(a):
    print(a[0] + a[1])
    print(a+a)
    print(a[2]*a[2])


method(a=[1, 2, 4])


pi=3.14
print("the val of pi is  " +str(pi))

z = 10


def func1():
    global z
    #z = 3


def func2(x, y):
    global z
    return x + y + z


func1()
total = func2(4, 5)
print(total)

#calling function in function
def highFive():
    return 5


def f(x, y):
    z = highFive()  # we get the variable contents from highFive()
    return x + y + z  # returns x+y+z. z is reachable becaue it is defined above


result = f(3, 2)
print(result)
