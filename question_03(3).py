n = float(input("Enter the number:-"))
error = float("Enter the error:-")
i = 1
fact=1
f_i=n
f_i1 = f_i - n**(2*i)
f_i1=n-(n**2)/2

while abs(f_i1-f_i)>=error:
    print(f"Iter{i}:",abs(f_i1-f_i))
    f_i=f_i1
    i+=1
    fact=fact*((2*i)*(2*i-1))
    if i%2==0:
        f_i1 = f_i1 + (n**(2*i))/fact
    else:
        f_i1 = f_i1 - (n**(2*i))/fact

print("no. of terms: ",i+1)
print("f_i+1: ",f_i1)
