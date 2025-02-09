def main():
  name = input("What is your name? ")
  num = int(input("What is your square num? "))
  hello(name)
  print(square(num))

def hello(name):
  print("Hello, " + name)

def square(x):
  return x * x

main()