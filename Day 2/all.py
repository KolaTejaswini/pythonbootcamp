my_list=list(map(int,input().split(" , ")))
choice=int(input())
if(choice==1):
    my_list.append(23)
    print(my_list)
elif(choice==2):
    my_list.pop(3)
    print(my_list)
elif(choice==3):
     my_list.sort()
     print(my_list)
else:
     print(f"hello,{len(my_list)}")
