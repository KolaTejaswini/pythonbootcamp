# write a program to count all the consonents 


check=['a','e','i','o','u']
abc="bcgflladerthikmnbvcf"
ans=""
i="hello wOrld"
inp=i.lower()
for i in inp:
        if(i in check):
            ans+=i
for i in inp:
          if(i in abc):
             ans+=i
print(ans)