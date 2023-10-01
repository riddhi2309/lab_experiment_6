#Getting the input by the user
n = int(input("enter the number :-"))
#initialization
sum = 0
fact = 1
i = 1
#starting the while loop
for j in range(n):
    fact = fact*i
    sum = sum + 1/fact
    i+=1
print(sum)
    



