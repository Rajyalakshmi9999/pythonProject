def compare_strings(str1, str2):
    count1 = 0
    count2 = 0

    for i in range(len(str1)):
        if str1[i] >= "0" and str1[i] <= "9":
            count1 += 1

    for i in range(len(str2)):
        if str2[i] >= "0" and str2[i] <= "9":
            count2 += 1

    return count1 == count2
