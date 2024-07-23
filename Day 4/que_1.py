# password peripheral
# # mr X trying to create a new pswrd for his insta accnt these are the requried conditions for creating
#  an new pswd
# conditions:
# 1. minimum length is 8,maximum length is 15 
# 2. only @ nd / is allowed in a pswrd
# 3. no spaces are allowed
# 4. only alpha numerics are allowed
# ur suppose to print weak if length is exact 8
# medium length is b/w 8-12
# #strong length is b/w 12-15


pswrd=(input())
n=len(pswrd)
if n<8:
      print("follow the condition")
str="@,/"
str[0]="@"
str[1]="/"     
for i in pswrd:
   if(i in str[0] or str[1]):
    count+=1
    break