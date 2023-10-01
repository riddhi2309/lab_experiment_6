#Getting the input by the user
sen = input("enter the a sentence:-")
#Intialize the function by the variale count ,space, count_v,count_c ,count_w
count=0
space = " "
count_v=0
count_c = 0
count_w = 1
vowel =["a","e","i","o","u"]
#starting the for loop
for p in sen:
    if p in vowel:
        count_v+=1
    elif p in space:
       count_w+=1  
    else:
        count_c+=1
print(count_c)
print(count_v)
print(count_w)
