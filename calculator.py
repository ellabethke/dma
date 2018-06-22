import sys
import math

def pythagoras(a,b):
    a_squared = math.pow(a,2)
    b_squared = math.pow(b, 2)

    return math.sqrt(a_squared + b_squared)

def main():
   command = sys.argv[1]


   if command == "add":
       x = int(sys.argv[2])
       y = int(sys.argv[3])

       print(x + y)
   if command == "subtract":
           x = int(sys.argv[2])
           y = int(sys.argv[3])

           print(x - y)
   if command == "multiply":
       x = int(sys.argv[2])
       y = int(sys.argv[3])

       print(x * y)
   if command == "divide":
       x = int(sys.argv[2])
       y = int(sys.argv[3])

       print(x / y)
   if command == "exponents":
           x = int(sys.argv[2])
           y = int(sys.argv[3])
           print(x ** y)

   if command == "count_to":
       x = int(sys.argv[2])

       for i in range(x):
           print(i)


   if command == "hypot":
       a = int(sys.argv[2])
       b = int(sys.argv[3])

       print(pythagoras(a,b))

main()