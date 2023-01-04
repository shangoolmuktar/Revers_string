
'''Reverse string using append'''
str1 = input("Please Enter String : ")
rev_str=[]
for i in str1:
    rev_str.append(i[::-1])
    print(rev_str)
'''Reverse string using len'''
str=input("string : ")
str1=str[::-1]
result=''
for i in range(len(str1)-1,-1,-1):
    result=result+str1[i]
    print(result)

s=input("string : ")
str=s[::-1]
print(str)
print(str[1],str[2],str[3],str[0])
print(str[2],str[3],str[0],str[1])
print(str[3],str[0],str[1],str[2])
print(str[0],str[1],str[2],str[3])


