list1=[]  
list2=[]  
num1=int(input("Enter number of elements for first list:"))  
for i in range(num1):  
    b=int(input("Enter element:"))  
    list1.append(b)  
      
num2=int(input("Enter number of elements for second list:"))  
for i in range(num2):  
    d=int(input("Enter element:"))  
    list2.append(d)  
  
temp = []
if len(list1) < len(list2):
    temp = list2
    list2 = list1
    list1 = temp

list3 = []

for e in range(len(list1)):
    list3.append(list1[e])
    if e < len(list2):
        list3.append(list2[e])

print(list3)