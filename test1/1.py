#while loop

condition = 1

while condition <= 10:
	print(condition)
	condition += 5

print("opeartion complete")

n=3
sum=0
i=1

while i<=n:
    sum=sum+i*i
    i=i+1

print("the sum is: ",sum)

#while True:
   # print"Atif"

#for loop

exampleList = [1,5,6,6,2,1,5,2,1,4]

#for x in exampleList:
#    print(x)

print"Atif"

#for x in range(1,11):
 #   print(x)


#take input
x=raw_input("the value is: ")
type(x)
print("the value of x is: ",x)

#if else loop
print"give the value of y & z "

y=raw_input()
z=raw_input()
if y>z:
    print"good"
elif y<z:
    print"bad"
else:
    print"null"




def example():
    print('this code will run')
    z = 3 + 9
    print(z)
example()



num1=int(input())
print num1