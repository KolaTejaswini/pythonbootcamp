#sum of digits in a num using ASCII values
inp=input()
sum=0
for i in inp:
    if(ord(i)>=48 and ord(i)<=58):
        sum+=int(i)
print(sum)