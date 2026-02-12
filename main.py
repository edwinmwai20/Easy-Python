lst = [1,2,3,4,5,6,7,8,9,10]

left = 0
right = len(lst) - 1

while left < right:
    # swap
    lst[left], lst[right] = lst[right], lst[left]

    left += 1
    right -= 1

print(lst)
