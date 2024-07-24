# print all the vowels followed by consonents
vowel="aeiou"
consonent="bcghjeiwergbjumxfdgce"
ans=""
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i in vowel):
        ans+=i
        for i in inp:
            if(i in consonent):
                ans+=i
        print(ans)
    
