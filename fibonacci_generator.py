# Fibonacci generator function
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

while True:
# Create the generator
  fib = fibonacci_generator()
  n=int(input("How many fibonacci numbers you need ?\nInput: "))
# Generate the first n Fibonacci numbers
  for _ in range(n):
    print(next(fib))
  continue
