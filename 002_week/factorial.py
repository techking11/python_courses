# resursion lesson
def factorial(n):
  if(n == 1):
    return 1
  return n * factorial(n - 1)

result = factorial(3)


"""
factorial(3) -> 3 * factorial(2)
factorial(2) -> 3 * 2 * factorial(1)
factorial(1) -> 3 * 2 * 1
result = 3 * 2 * 1 = 6

algorithm ( n * n - 1)

Recursion (n!)
3! = 3 * 2 !
2! = 2 * 1 !
1! = 1!

n! = n . (n - 1) !
"""