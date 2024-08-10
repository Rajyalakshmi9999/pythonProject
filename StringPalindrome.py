
# /////////////////////////
# def isPalindrome(s):
#     return s == s[::-1]
#
#
#
# # Driver code
# s = "malayalam1"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")
    # ////////////////////////
    # Another way
    # st = 'malayalam'
    # j = -1
    # flag = 0
    # for i in st:
    #     if i != st[j]:
    #         flag = 1
    #         break
    #     j = j - 1
    # if flag == 1:
    #     print("NO")
    # else:
    #     print("Yes")

# x = "malayalam"
#
# w = ""
# for i in x:
#     w = i + w
#
# if (x == w):
#     print("Yes, given string is palindrome")
# else:
#     print("No, the given string is not palindrome")
original_string = "hello"
reversed_string = ''.join(reversed(original_string))
print(reversed_string)
if original_string==reversed_string:
    print("palindrome")
else:
    print("not palindrome")
print(reversed_string[0])
