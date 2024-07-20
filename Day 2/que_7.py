 #7  your are given with a comma seperated natural numbers 1to10 print evev numbers

#my_list=list(map(int,input().split(",")))
#for i in range(1,len(my_list),2):
   # print(my_list[i])


    #count how may even numbers are there

my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
    count+=1
print(count)
