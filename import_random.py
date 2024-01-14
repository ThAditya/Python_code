import random
def quiz():
        price=1000
        for i in range (10):
            question_1 = random.randint(100,1000)
            question_2 = random.randint(100,1000)
            a = random.randint(200,2000)
            b = question_2+question_1
            c = random.randint(2,2000)
            d = random.randint(200,2000)
            e= [a,b,c,d]
            random.shuffle(e)
            print("Question",{i+1},question_1,"+",question_2)
            for f in e:
                print(f)
            x=int(input("Enter your answer = "))
            if(x==b):
                print("Your answer is ",b," And this is corect \n")
                print("You Won ",price,"rupee cash price \n")
                price=price+1000
            else:
                print("Sorry!! Your answer is wrong \n \nYou lost this game \n ")
                return input("If you want to restart the game write yes if not then write no : ")
s="yes"
while(s=="yes"):
    s=quiz()