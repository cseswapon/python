# Text Type
# string
name = 'Python';
print(type(name), name);

# Numeric Type
'''
    int 
    float
    complex
'''
# int number
number = int('34');
print(type(number), number)
# float number
version = float("3.2");
print(type(version),"Version", version);
# complex number
math = (4+5j);
print(type(math),"Math", math);

# Sequence Types
""""
    list
    tuple
    range
"""
# list
x = ["halim","jubayer","sunil"];
print(type(x), x[0]);
# tuple
y = ("halim","jubayer","sunil");
print(type(y), y[0]);
# range
z = range(2,90)
print(type(z),z)

# mapping type
car = {"name":"R15","mileage":'1500cc',"version":3.2};
print(type(car),car);

# set type
'''
    set
    frozenset
'''
name = {"halim", "zubu", "shimu"};
print(type(name), name);

name2 = frozenset({"halim", "zubu", "shimu"});
print(type(name2), name2);

# Boolean Type
isPayment = True;
print(type(isPayment),isPayment);

# Binary Type
'''
    byte,
    bytearray,
    memoryview
'''
name3 = b"Hello";
print(type(name3), name3);
name4 = bytearray(5);
print(type(name4),name4);
memoryByte = memoryview(bytes(5));
print(type(memoryByte),memoryByte);

# None type

x = None;
print(type(x),x);