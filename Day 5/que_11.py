#code for ABC,4 SKIP 4 LETTERS AFTER A,B,C
inp=input()
n=int(input())
for i in inp:
    if(65<=ord(i)<=91):
        print(chr(ord(i)+n),end="")