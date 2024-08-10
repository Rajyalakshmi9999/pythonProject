# for i in range(10):
#     switch  i:
#     if i==3:
#         pass
#     print(i)


def switch_case(number):

        switcher = {
            1: "ONE",
            2: "TWO",
            3: "THREE",
            4: "FOUR",
            5: "FIVE",
            6: "SIX",
            7: "SEVEN"
        }
        for i, value in switcher.items():
            if i==3:
                print("number 3")
                break
            else:
                continue
        else:
            print("invalid month")

no  =   9
switch_case(no)
# ////////////////////////////////
pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
for p in pat:
   pass
   if (p == 0):
       current = p
       break
   elif (p % 2 == 0):
       continue
   print(p)    # output => 1 3 1 3 1
print(current)    # output => 0
