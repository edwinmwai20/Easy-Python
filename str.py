#slicing
# in slicing we have start,stop,step

a = "this is a representation of a unicode character"
b= 'take thsi'
# print(a[-1])
# print(a[1:23])
# print(a[::3]) # stepping 
# print(a[::-1]) #reserve through


# methods

str_split = a.split(",")
type(str_split)
str_joined = ''.join(str_split)

print(str_joined)

# print(b.replace(",", ""))


#comparison

str_compare = 'he is an awesome guy'

if str_compare == 'he is an awesome guy, you can check out his account on twitter':
    print(True)

if str_compare in 'he is an awesome guy, you can check out his account on twitter':
    print(True)


print(a+b)
