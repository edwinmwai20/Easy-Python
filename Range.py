stair = [1,2,3,4,5,6,7,8,9]
# n = len(stair)
# dp =[0]*n
# def Step(t):
#     for i in range(0,t-1):
#         if (t in stair):
#             print(f'step {t}')

# print(Step(4))
            
def steps(n):
    for i in range(0,n):
        print(f"This is step {i+1}")

print(steps(5))