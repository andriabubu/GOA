e = int(input("Enter Your Midterm Test Score (0 to 100): "))
if e < 0:
     e = 0
elif e > 100:
     e = 100

r = int(input("Enter Your Final Test Score (0 to 100): "))
if r < 0:
     r = 0
elif r > 100:
     r = 100

t = int(input("Enter Your Project Score (0 to 100): "))
if t < 0:
     t = 0
elif t > 100:
     t = 100

print("your average score is")
Average = ((e+r+t)/3)
if Average >= 70:
     print("you passed")
else:
     print("you failed")
print(Average)
