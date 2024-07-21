# replace the elements in the array with avg of max nd min elements


my_list=list(map(int,input().split(" ")))
maxi=my_list[0]
mini=my_list[0]
for i in range(len(my_list)):
     if(my_list[i]>maxi):
          maxi=my_list[i] 
for i in range (len(my_list)):
     if(my_list[i]<mini):
          mini=my_list[i]                                                       
          avg=((maxi+mini)/2)
for i in range(0,len(my_list)):
          my_list[i]=avg
print(my_list)      