for w in range (1 , 101 ,):
     if w % 5 == 0 and w % 3 == 0:
         print("FizzBuzz")
     elif w % 3 == 0:
         print("Fizz")
     elif w % 5 == 0:
         print("Buzz")
     else:
         print(w)