# fimd the  elements that is present in k+i index
#k=3
#n=2
# [3,6,8,4,61,2]
#o/p = 2

#k=3
#n=4
#80 70 54 36 72
#o/p:error

my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
if(len(my_list)<k+n):
    print("error")
else:
    for i in range(0,len(my_list)):
        print(my_list[k+n],end=" ")
        break