x = float(input('enter any num: '))
y = float(input('enter any num: '))
z = float(input('enter any num: '))

if(x>y):
    temp = x
    x=y
    y=temp

if(y>z):
    temp = y
    y=z
    z=temp

if(x>y):
    temp = x
    x=y
    y=temp

print(x,y,z)