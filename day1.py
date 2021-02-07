#python List built-in function

#1.abs()
abs(-7)
abs(7)


#2.all()
all({'*',","})
all(['','',','])

#3.any()
any((1,0,0))
any((0,0,0))

#4.ascii()
ascii('s')
ascii('usor')

#.bool()
bool(0.5)
bool('')
bool(True)

#Python Dictionary built-in Function

#1.Python Dictionary Comprehension

mydict={x*x:x for x in range(8)}
mydict

#2.Dictionaries with mixed keys
dict3={1:'carrots','one':[1,2,3]}
dict3

#3.dict()
dict(([1,2],[2,4],[3,6]))
dict([1,2],[2,4],[3,6])

#4.Declaring one key more than once
 
mydict2={1:2,1:3,1:4,2:4}
mydict2


#5.Declaring an empty dictionary and adding elements later
animals={}
type(animals)

animals[1]='dog'
animals[2]='cat'
animals[3]='ferret'
animals
