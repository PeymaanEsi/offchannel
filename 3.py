from itertools import combinations

list1=[]  
num1=int(input("Enter number of elements for first list:"))  
for i in range(num1):  
    b=int(input("Enter element:"))  
    list1.append(b)  

combs = list(combinations(list1, 2))

for e in combs:
    if sum(e) == 1:
        print(list(e))
        continue  
else:
    print([])