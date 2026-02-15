##Numeric
#1. int 
x=10

#2. float
x=10.4

#3 .complex
x=3+5j

print(type(x))


###text

#1 .str
x='fbs'

x="fbs"

x='''this is first
bit class'''

x="""this is f b class"""

print(type(x))

###Sequential

#1 list
x=[1,2,3,4]

print(type(x))

#2 tuple
x=(1,2,3,4)
print(type(x))

#3 range()

x=range(1,10)
print(type(x))


###Settype
#1 .set
x={0,20,30,40,'a'}

#2 frozenset
x=frozenset({1,2,3,2,'a'})
print(x)
print(type(x))


###Mapping
#1. Dictionary
x={1:'python',2:'java',3:'c'}
print(x)
print(type(x))
print(x[1])


###Boolean
#1. bool
x=False
print(x)
print(type(x))

###Nonetype

x=None
print(type(x))