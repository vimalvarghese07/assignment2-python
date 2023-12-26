a=input("Enter the name of Fruit:")
b=input("Enter the name of Fruit:")
c=input("Enter the name of Fruit:")
d=input("Enter the name of Fruit:")
e=input("Enter the name of Fruit:")
fruits=[a,b,c,d,e]
newList=[]
for x in fruits:
    if "e" in x:
        newList.append(x)
print(newList)