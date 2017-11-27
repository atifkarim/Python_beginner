def simple_addition(num1,num2):
    #num1=int(input())
    #num2 = int(input())
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)

simple_addition(num1=int(input()),num2=(input()))


def basic_window(width,height,font='TNR'):
    # let us just print out everything
    print(width,height,font)
basic_window(350,500)
basic_window(350,500,"courier")

x=5

def ex():

    print("the val of x: ",x)
    z=6
    print("the val of z: ",z)
ex()

x = 6


def example(modify):
    print(modify)
    modify += 5
    print(modify)
    #return modify


x = example(x)
print(x)
