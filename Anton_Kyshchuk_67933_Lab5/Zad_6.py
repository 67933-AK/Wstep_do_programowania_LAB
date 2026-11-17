import math

a=float(input())
b=float(input())
c=float(input())
def pole(a,b,c):
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        s=(a+b+c)/2
        result = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Pole trójkąta wynosi: {result:.2f}")
        return result
    else:
        return 1
    
pole(a,b,c)