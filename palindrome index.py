
# def palindromeindex(s):
#     if(s[::-1]==s):
#         return -1
#
#     n=len(s)
#     for i in range(n//2):
#         if(s[i]!=s[n-1-i]):
#             if(s[i:n-1-i]==s[i:n-1-i][::-1]):
#                 return n-1-i
#
#             elif(s[i+1:n-i]==s[i+1:n-i][::-1]):
#                 return i
#     return -1
#
# text=input("Enter the text :\n ")
# print(palindromeindex(text))

# l=[2,5,1,3,4]
#
# for i in range(len(l)):
#     # print(l[i],i)
#     # if(l[i]-(i+1)>2):
#     #     print('hai')
#
#     for i in range(max(0,i,l[i]-2)):
#         print((0,i,l[i]-2))

