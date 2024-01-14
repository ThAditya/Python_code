import random
price=1000
while(price<10000):
    question_1 = random.randint(1,56)
    question_2 = random.randint(1,50)
    a = random.randint(1,200)
    print(question_1,"+",question_2)
    print(a,(question_2+question_1),a,a)
    x=int(input("Enter your answer"))
    if(x==(question_1+question_2)):
        print("Your answer is ",question_1+question_2," And this is corect")
        print("You Won ",price,"rupee cash price")
        price=price+1000
    else:
        print("Sorry!! Your answer is wrong \nYou lost this game \n ")
    break