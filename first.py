
# check this statement
"""
hi python what's up what are you doing now bro
"""
import random

if(4 > 3):
    print("4 is getter then 3");
else:
    print("3 is getter then 4");

name = 'MR.X';
# type casting int,str,float
age = float(23);

x,y,z = 'Mango', 'Banana', 'Orange';

print("\nMy Name is", name, "My Age is", age);

print("\nFruits",x);

# one value of multiple variable
a = b = c = "Multiple";

print(a,b,c);

# range variable

name = ['hero','alom','sujon'];
d,e,f = name;

print(d,e,f);

# global variable

glb = str('hello world Mr.X');

def myfun():
    glb = 'hello world Mr.Y';
    print("I love ", glb);
myfun()

print(glb)

def myfun2():
    global glb2;
    glb2 = 'Hello kaku';
    print(type(1j));
myfun2()
print(glb2)

print(random.randrange(1,20))