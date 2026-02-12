#A dictionary is a collection of key-value pairs.
# They are important in managing data efficiently

# Why are they important?

#1. They store key-value, look-up for any data 0(1)
      # - They are optimized for speed 

# 2.Everything uses them
   # - JSON
   # API Response
   # Configuration setting

# 3.They are able to model real world objects

# 4.They are mutable

person = {
    #key : value
    "name":"wassabi",
    "age": 30,
    "isCool": True,
    "greet": lambda _ :"hello world"
}

#Values are stored by the keys,valyes are accessed by the label

print(person['isCool'])

#  Some of the common methods
# 1. get()
   # Retrieve information in a safer way

print("This guy height is:", person.get("height",0))# - prints height 0 instead of none(0 is the alternative)

print("This guy height is:", person.get("age",0))# - This one prints 30 since age is already defined

#. 2.key()
   # Returns al available keys in a list format

print(person.keys())

# 3. value()
    #- Returns all the values
# print(person(values()))


# 4.itmes()
    #returns key value pairs

for keys, values in person.items():
    print(keys,"=>",values)
    

#####################################################



# I have an array of strings, i want to count the number of words on each string

word= ['hello','world','this','is', 'another','day','to', 'check','if','we','gonna','get','lucky!']

print(word)
