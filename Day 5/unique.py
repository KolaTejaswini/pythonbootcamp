#print the non repeating characters in a given string
#print the unique characters in a given string
check=['a','e','i','o','u']
abc="bcgflladerthikmnbvcf"
ans=""
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)