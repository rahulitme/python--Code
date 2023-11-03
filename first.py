#Integer inputs
Var = int(input('Enter an integer value: '))
print(Var)


#using int in loops
#initialize an integer
i = 0
while i <= 4:
    print(i,end=" ")
    i+=1
print()


#using int to iterate through an list
#initialize a list
arr = [1,2,3,4,5]
#iterating through list
for integer in range(len(arr)):
    print(arr[integer],end=" ")
print()

#mathematical operations on integer
#initialize int variables
a = 10
b = 2
#addition
print(a+b)


#Subtraction
print(a-b)


#multiplication
print(a*b)


#division
print(a/b)


#floor division
print(a//b)