# 1
n=int(input("1. Тоон утга оруулна уу : "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("Энэ утга палиндром байна.")
else:
    print("Энэ утга палиндром биш байна.")

# 2
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("2.","Өгөгдсөн утга : ", s)
    print ("Том үсгүүдийн тоо : ", d["UPPER_CASE"])
    print ("Жижиг үсгүүдийн тоо : ", d["LOWER_CASE"])

string_test('Семинар 2 Д.Энхсаруул')

# 3
Дасгал3 = [1,2,3,4]
def үржүүлэх(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
print("3.",үржүүлэх(Дасгал3))

# 3
from functools import reduce
Дасгал3 = [1,2,3]
result1 = reduce((lambda x, y: x * y), Дасгал3)
print("3.","lambda-гаар бодсон",result1)

# 4
num = int(input("4. Тоон өгөгдөл оруулна уу "))    
factorial = 1    
if num < 0:    
   print(" хасах утга байж болохгүй")    
elif num == 0:    
   print("0 байж болохгүй")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print('    ',num,'-ийн бактерал нь',factorial)    

# 5
def Reverse(Дасгал5):
    return [ele for ele in reversed(Дасгал5)]
Дасгал5 = [1,2,3,4,5,6,7,8,9,10]
print("5.",Reverse(Дасгал5))

# 6
from functools import reduce
Дасгал6 = [1,2,3,5,6]
result1 = reduce((lambda x, y: x + y), Дасгал6)
print("6.",result1)

# 7
Дасгал7 = [1,2,2,3,3,4,4,5,6,7,8]
Дасгал7 = list(dict.fromkeys(Дасгал7))
print("7.",Дасгал7)

# 8
def maximum(a, b, c): 
   list = [a, b, c] 
   return max(list)  
x = int(input("8. Эхний тоог оруулна уу "))
y = int(input("Хоёр дахь тоог оруулна уу "))
z = int(input("Гурав дахь тоог оруулна уу "))
print("Хамгийн их тоо нь",maximum(x, y, z)) 
