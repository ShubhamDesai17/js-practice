import sys
# num1=20
# num2=10

def add(num1, num2):
    num3=num1+num2
    return num3

def sub(n1, n2):
    n3=n1-n2
    print(n3)
    return n3

def mul(n1, n2):
    print(n1*n2)
    return n1*n2

# add()
# sub(10, 5)
# mul(10,2)

n1=int(sys.argv[1])
op=sys.argv[2]
n2=int(sys.argv[3])

if op=="add":
    output=add(n1,n2)
    print(output)
