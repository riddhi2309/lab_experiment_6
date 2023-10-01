#Getting the input by the user n and x
n = int(input("Enter the number:-"))
x = int(input("Enter the number:-"))
#initializg the variable sum,i,a
sum= 1
i=1
a = 1
# starting the for loop
for j in range(n):
    sum = sum + (x**i)/a
    i+=1
    a+=1
print(round(sum,9))