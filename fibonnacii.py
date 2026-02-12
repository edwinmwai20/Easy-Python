#Fibonnaci

def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


print(fib(5))


#Tribonnaci

def tribonnaci(n):
    if n==0:
        return 0
    elif n in [1,2]:
        return 1
    

    dp = [0]* (n+1)
    dp[0],dp[1],dp[2]
    for i in range(3,n+1):
        dp[i] = dp[i-1] +dp[i-2]+dp[i-3]

    
    
    return dp[n]


