# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n
def sum(n):
    if n == 1 or n == 0:
        return 1
    return sum(n-1) + n

# f = factorial_iter(5)
f = sum(3)
print(f)