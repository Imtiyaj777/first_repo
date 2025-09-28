# operators

# Arithmetic Operators

a=10
b=7
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division
print(a%b) # modulus
print(a**b) # exponentiation
print(a//b) # floor division

a=5
b="add"

# print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a-b) # TypeError: unsupported operand type(s) for -: 'int' and 'str'

print(a*b) # addaddaddaddadd

# print(a/b) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
# print(a%b) # TypeError: unsupported operand type(s) for %: 'int' and 'str'
# print(a**b) # TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
# print(a//b) # TypeError: unsupported operand type(s) for //: 'int' and 'str'


# Comparison Operators
a=10
b=5

print(a==b) # equal to
print(a!=b) # not equal to
print(a>b) # greater than
print(a<b) # less than
print(a>=b) # greater than or equal to
print(a<=b) # less than or equal to

# assignment operators
x=5
x+=3
print(x) # 8

x=5
x-=3
print(x) # 2

x=5
x*=2
print(x) # 10

x=5
x/=2
print(x) # 2.5

x=5
x%=2
print(x) # 1

x=5
x**=2
print(x) # 25

x=5
x//=2
print(x) # 2

# logical operators

a=True
b=False
print(a and b) # False

a=True
b=False
print(a or b) # True

a=True
b=False
print(not a) # False
print(not b) # True

#membership operators
a="hello"
print('h' in a) # True
print('z' in a) # False

a="hello"
print('h' not in a) # False
print('z' not in a) # True

# identity operators

a=5
b=5
print(a is b) # True
print(a is not b) # False

a=[1,2,3]
b=a
print(a is b) # True
print(a is not b) # False

# Example
x = 5
x *= x +2

d = 10
c = 5
print(c<d<c*2)


print([] and 0 or "hello" and 22)


# bitwise operator

print(bin(11)) 

# or (|)
p=5
q=6
print(p|q)

# and (&)
p=5
q=6
print(p&q)

# xor
p=5
q=6
print(p^q)

#negatiation ( tricik [~]: -(n+1)) and ternary (syntax)
i=21
print(~i)

#trenary syntax
j=10
k=12

print(j if j > k else k)
