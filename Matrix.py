Rows = int(input("แถว : "))  
Columns = int(input("หลัก :"))  

list = []  

for _ in range(Rows):
    r = []  
    for __ in range(Columns):  
        r.append(int(input("ใส่ตัวเลข : ")))  
    list.append(r)  
  
for _ in range(Rows):  
    for __ in range(Columns):  
        print(list[_][__], end=" ")  
    print()  

Rows2 = int(input("แถว : "))  
Columns2 = int(input("หลัก : "))  

list2 = []  

  
for _ in range(Rows2):
    r = []  
    for __ in range(Columns2):  
        r.append(int(input("ใส่ตัวเลข : ")))  
    list2.append(r)  
  
for _ in range(Rows2):  
    for __ in range(Columns2):  
        print(list2[_][__], end=" ")  
    print() 