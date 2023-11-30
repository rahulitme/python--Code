num = 28
sum = 0

i = 1
while i < num:
    if num % i == 0:
        sum += i

    i += 1

if sum == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")