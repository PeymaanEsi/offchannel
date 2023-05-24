str1 = input("Enter String:")

for s in str1:
    if str1.count(s) == 1:
        print(s)
        break
else:
    print(None)