from queue import Empty

# 1.
list1= ["python", "php","java"]
print('1.',list1[0])
print(list1[1])
print(list1[2])

# 2.
list2 = [1,2,3,4,5,6,7,8,9,10]
total = 0
for num in list2:
    total = total + num
print('2.',total)

# 3.
list3 =[3,4,5,7,10]
total = 1
for num in list3:
    total = total * num
print('3.',total)

# 4.
list4=[2,4,5,6,10]
def Multiply( num1, num2 ): 
    answer = num1 * num2
    return answer
print('4.',Multiply(list4[4],list4[-1]))

# 5.
list5=[1,2,3,4,5,6,7,8,9,10]
list5.sort()
print('5.',list5[0],list5[-1])

# 6.
list6=(['abcd', 'aba', '1221'])
def list6(words):
  k = 0
  for a in words:
    if len(a) > 1 and a[0] == a[-1]:
      k += 1
  return k
print('6.',list6(['abcd', 'aba', '1221']))

# 7.
list7= [1,1,2,3,2,2,4,5,6,2,1]
number= set(list7)
print('7.',list(number))

# 8.
list8=[1,2,3,4,5,6,7,8,9,10]
if not list8:
    print('8.',"list is empty")
if list8:
    print('8.',"list is not empty")

# 9.
list9=[1,2,3,4,5,6,7,8,9,10]
list9.remove(list9[3])
list9.remove(list9[-5])
list9.remove(list9[-3])
print('9.', list9)

# 10.
list10=(1,2,3,4,5,6,7,8,9,10)
print('10.',list10)

# 11.
list11=(1,2,3,4,5,6,7,8,9,10)
nemeh=(11)
total2=list(list11)
total2.append(nemeh)
print('11.',tuple(total2))

# 12.
list12=(1,2,3,4,5,6,7,8,9,10)
nemeh=(11)
total2=list(list12)
total2.append(nemeh)
dahiad=(12,13)
total3=list(total2)
total3.extend(dahiad)
print('12.',tuple(total3))

# 13.
list13=(1,2,3,4,5,6,7,8,9,10)
if not list13:
    print('13.',"list is empty")
if list13:
    print('13.',"list is not empty")

# 14.
list14 = (1,2,3)
for i in list14:
    print('14.',i)

# 15.
list15={1,2,3,4,5,6,7,8,9,10}
l15={11,12,13}
Newset = list15.union(l15)
print('15.',Newset)

# 16.
list16={1,2,3,4,5,6,7,8,9,10}
l16={11,1,5} 
Newset = list16.intersection(l16)
print('16.',Newset)

# 17.
list17={1,2,3,4,5,6,7,8,9,10}
print('17.',len(list17))

# 18.
list18={1,2,3}
list18.remove(2)
print('18.',list18)

# 19.
list19={1,2,3}
list19.remove(2)
list19.discard(1)
list19.discard(3)
print('19.',list19)

# 20.
list20={1,2,3}
del list20

# 21.
dict1 = {
    1: 30, 
	2: 20, 
	3: 10 } 
print ('21.',dict1)

# 22.
dict1 = { 
    1: 30, 
	2: 20, 
	3: 10 } 
if 2 in dict1:
	print('22.','2 is in it.' )

# 23.
dict1 = { 
    1: 30, 
	2: 20, 
	3: 10 } 
if 30 in dict1.values():
	print('23.','30 is in it.')
else:
    print('23.','30 is not in it.')

# 24.
dict1 = { 
    1: 30, 
	2: 20, 
	3: 10 } 
for x,y in dict1.items():
	print('24.',x,y)

# 25.
def Merge(dict1, dict2):
    a = {**dict1, **dict2}
    return a
dict1 = { 
    1: 30, 
	2: 20, 
	3: 10 } 
dict2 = { 
    4: 60, 
	5: 50, 
	6: 40 } 
dict3=Merge(dict1, dict2)
print('25.',dict3)

# 26.
dict1 ={ 
    4: 60, 
	5: 50, 
	6: 40 } 
values = dict1.values()
total = sum(values)
print('26.',total)







