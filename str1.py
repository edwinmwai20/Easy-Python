# string in python & the methods
    # immutable, sequence type, ordered
    # it store Unicode text
    # you create using quotes "", '', """"

a = "this is a representaion of a unicode characters. they are all in a sequence"
b = 'al,so, th,is, is o,n,e'
c = """
    this is a multi-line string
    we can add unicode texts as long as we have the triples quotes
    mutiple line of strings
    """
d = "alpha numeric character. The user is 13476, the location is 30100. The user is armed and dangerous"

# print(a)
# print(id(b))

b = b + " though this might give a different id"
# print(id(b))
# print(b)

# formating a string
person = {
    'name' : "Kimosabi",
    "age" : 30,
    "occupation" : "mtu wa ratish"
}

prog = f"Hello, {person["name"]}"
# print(prog)

# String Operations
    # 1. Slicing

# print(a[0])
# print(a[-1])
# print(a[1:23])
# print(a[::3]) # stepping through
# print(a[::-1]) #reversing of the string

    #2. Method

str_split = b.split(",")
print(type(str_split))
str_joined = ''.join(str_split)
print(str_joined)

print(b.replace("i", "L"))

# check content
# print(d.lower().islower())
# print(d.isalpha())
# print(d.isspace())

# comparison

str_to_compare = "he is an awesome guy"

if str_to_compare == "he is an awesome guy":
    print(True)

if str_to_compare in "he is an awesome guy, you can check out his account on twillio":
    print(True)

print(a + b)

print(a.capitalize())