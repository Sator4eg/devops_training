a1 = int(input('enter a1 '))
b1 = int(input('enter b1 '))
a2 = int(input('enter a2 '))
b2 = int(input('enter b2 '))
cal1 = str()
cal2 = str()
if a1 % 2 != 0 and b1 % 2 != 0:
    cal1 = 'white'
elif a1 % 2 == 0 and b1 % 2 == 0:
    cal1 = 'white'
else:
    cal1 = 'black'
if a2 % 2 != 0 and b2 % 2 != 0:
    cal2 = 'white'
elif a2 % 2 == 0 and b2 % 2 == 0:
    cal2 = 'white'
else:
    cal2 = 'black'
if cal1 == cal2:
    print(cal1, 'Yes')
else:
    print(cal1, cal2, 'no')
#test comment
#test comment developer brunch

