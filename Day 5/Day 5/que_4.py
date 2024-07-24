#by using print(ord(" ")) we can calculate ASCII values
#  check how many vowels are there in a string

check=['a','e','i','o','u']
count=0
inp="helloworld"
for i in inp:
        if(i in check):
                count+=1
                print(count)