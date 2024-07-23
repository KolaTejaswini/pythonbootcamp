#write a program  prime numbers
a=int(input("enter the number:"))
r=a*0.5
count=0
if a==1:
      print("not  prime number")
elif a==2:
      print("prime")
for i in range(2,int(r+1)):
       if a%i==0:
            count+=1
            break
if(count==0):
        print("prime")
else:
 
           print("not a prime")    