# x=[1,2,3,4,5,6,7,8]

# n = len(x)

# for i in range(n):
     
#      mirror = n-1-i

#      if n < mirror:

#         x[n],x[mirror]= x[mirror],x[n]



# print(x)

x=[1,2,3,4,5,6,7]

for item in range(n//2):

    z = n-1-item 

    x[item], x[z] = x[z],[item]

print(x)