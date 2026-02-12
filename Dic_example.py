
word= ['hello','world','this','is', 'another','day','to', 'check','if','we','gonna','get','lucky!','hello','world','this','is', 'another','day','to','hello','world','this','is', 'another','day','to', 'check','if','we','gonna','get','lucky!']

count = {}

for item in word:
    count[item] = count.get(item,0) +1

print(count)
