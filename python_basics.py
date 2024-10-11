import time
# is_online=False
# print(is_online)
# name=input("hello ")
# print("hi "+name)


course='python for'
print(course.upper)
print(course)
print(course.find('Y'))
print(course.find('y'))
print(course.find('for'))
print(course.replace('y','4'))

print(10//3)
a=25
if a>30:
    print("hi")
    print("hello")
elif a>20:
    print("you")
else:
    print("me")
print("done")    

# a=input("weight: ")

# b=input("(k)g or (L)bs: ")
# if (b.upper()=="K"):
#     print("weight in lbs: "+str(a/0.45))

names=["a",'b','c','d']
names.remove('b')
# names.clear()
print(1 in names)
print(len(names))
print(names[0:3])
for i in names:
    # for i in "bro code":
    print(i)
i=0
while i<len(names):
    print(names[i])
    i=i+1
num=range(5,10)
for i in num:
    print(i)


for i in range(5,10,2):
    print(i)

# name="bro code"
#  fn=name[0:2]//[:2]
# dn=name[4]
# print(dn)
# print(fn)

# fn=name[0:8:2]
# print(fn)
# an=name[0:8:1]
# //[::1]
# print(an)
# bn=name[::-1]
# print(bn)
# webbsite1="https//google.com"
# slice=slice(7,-4)
# print(webbsite1[slice])

# name=None
# while not name:
#     name=input("Enter your name:")
#     print("hello"+name)

# for sec in range(10,0,-1):
#     print(sec)
#     time.sleep(1)
# print("happy")


# rows=int(input("rows: "))
# columns=int(input("columns: "))
# symbol=input("symbol: ")
# for i in range(rows):
#     for j in range(columns):
#         print (symbol,end="")
#     print()

# for i in range(1,15):
#     if i == 13:
#         pass
#     else:
#         print(i)


# d=["cofee","tea"]
# for x in d:
#     print(x)
# e=["pizza","pasta"]
# f=["cake","pudding"]
# food=[d,e,f]
# print(food[0][1])
# //set....add/.remove/.clear
sets={'a','b','c','a'}
sets1={'t','s','r','g','a'}
# sets.update(sets1)
# joinset=sets.union(sets1)
# for x in joinset:
#     print(x)
# print(sets.difference(sets1))
# print(sets.intersection(sets1))

# fruits=['t','s','r','g','a']
# print('a' in fruits)
# fruits.sort()
# fruits.reverse()
# print(help(fruits))
# foods=[]
# prices=[]
# total=0
# while True:
#      food = input("Enter a food to buy (q to quit): ")
#      if food.lower()=="q":
#         break
#      else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)
# print("----- YOUR CART -----")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price

# print()
# print(f"Your total is: ${total}")


# 2D list of lists
num_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]]

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# 2D list of tuples
# num_pad = [(1, 2, 3),
#                       (4, 5, 6),
#                       (7, 8, 9),
#                       ("*", 0, "#")]

# 2D list of sets
# num_pad = [{1, 2, 3},
#                       {4, 5, 6},
#                       {7, 8, 9},
#                       {"*", 0, "#"}]

# # 2D tuple of lists
# num_pad = ([1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 9],
#                       ["*", 0, "#"])

# # 2D tuple of tuples
# num_pad = ((1, 2, 3),
#                       (4, 5, 6),
#                       (7, 8, 9),
#                       ("*", 0, "#"))

# # 2D tuple of sets
# num_pad = ({1, 2, 3},
#                       {4, 5, 6},
#                       {7, 8, 9},
#                       {"*", 0, "#"})

# # 2D set of lists (NOT VALID)
# num_pad = {[1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 9],
#                       ["*", 0, "#"]}

# # 2D set of tuples
# num_pad = {(1, 2, 3),
#                       (4, 5, 6),
#                       (7, 8, 9),
#                       ("*", 0, "#")}

# # 2D set of sets (NOT VALID)
# num_pad = {{1, 2, 3},
#                       {4, 5, 6},
#                       {7, 8, 9},
#                       {"*", 0, "#"}}


# 
# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("----------------------")
#     print(question)
#     for option in options[question_num]:
#         print (option)
#     guess=input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess==answers[question_num]:
#         score+=1
#         print("correct")
#     else:
#         print("incorrect")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1

# print("----------------------")
# print("       RESULTS        ")
# print("----------------------")

# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")
 #dictionary =  a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")
# capitals.update({"Germany":"berlin"})
# # capitals.pop("china")

# for key,value in capitals.items():
#     print(f"{key} : {value}")

# Concession stand program

# menu = {"pizza": 3.00,
#                "nachos": 4.50,
#                "popcorn": 6.00,
#                "fries": 2.50,
#                "chips": 1.00,
#                "pretzel": 3.50,
#                "soda": 3.00,
#                "lemonade": 4.25}
# cart = []
# total = 0

# print("--------- MENU ---------")
# for key, value in menu.items():
#     print(f"{key:10}:${value:.2f}")
# print("------------------------")

# while True:
#     food= food = input("Select an item (q to quit): ").lower()
#     if food=="q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
# print("------ YOUR ORDER ------")
# for food in cart:
#     total+=menu.get(food)
#     print(food,end=" ")
# print()
# print(f"Total is: ${total:.2f}")
