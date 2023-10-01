x = int(input("Enter the number "))
sum = 0
i=1
while i<=x:
    sum = sum+1/(2**i)
    i+=1
print(sum)