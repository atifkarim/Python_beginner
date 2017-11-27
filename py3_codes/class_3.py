class calculator:
    def addition(x,y):
        added = x + y
        print(added)

    def subtraction(x, y):
        sub = x - y
        print(sub)

    def multiplication(x, y):
        mult = x * y
        print(mult)

    def division(x, y):
        div = x / y
        print(div)
calculator.addition(x=int(input()),y=int(input()))


x = input('What is your name?: ')
print('Hello',x)

y=float(input())
print ("the num is: ",y)



import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

x = statistics.mean(example_list)
print(x)

y = statistics.median(example_list)
print(y)

z = statistics.mode(example_list)
print(z)

a = statistics.stdev(example_list)
print(a)

b = statistics.variance(example_list)
print(b)

