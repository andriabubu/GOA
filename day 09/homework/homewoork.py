# 2) დაწერეთ პროგრამა, რომელიც იღებს ორი ადამიანის ასაკს და განსაზღვრავს ვინ არის უფროსი.

person1 = input("enter first person age: ")
person2 = input("enter second person age: ")
if person1 == person2: print("they are both the same age")
if person1 > person2: print("the first person is bigger than second person")
if person1 < person2: print("the second person is bigger than first person")