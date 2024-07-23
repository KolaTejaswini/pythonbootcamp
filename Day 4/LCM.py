# LCM for 2 number
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
while b!=0:
    a,b=a*b/b,a%b
print("lcm  of 2 numbers is:",a)
