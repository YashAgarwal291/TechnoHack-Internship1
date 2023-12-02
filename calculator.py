def add(a,b): 
  return a+b
def sub(a,b): 
  return ((a-b) if (a>b) else (b-a))
def mul(a,b): 
  return a*b
def div(a,b): 
  return a/b
def operation(a,b,c):
  if c=="+": 
    return add(a,b)
  elif c=='-': 
    return sub(a,b)
  elif c=='*':
    return mul(a,b)
  else: 
    return div(a,b)
a=int(input("Enter the expression"))
b=int(input("Enter the value "))
c=input("enter the operator ")

print("Result  is equal to ",operation (a,b,c))
