q = int(input("enter your number 0-99 "))
if q <= 100 and q >= 0:
        for q in range(1, q+1):
           print(q)
else:
      while q <= 0 or q >= 100:
            q = int(input("enter your number 0-99 "))
            if q < 100 and q > 0:
                  for q in range(1, q+1):
                         print(q)
