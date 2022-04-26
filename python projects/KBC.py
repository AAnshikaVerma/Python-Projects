question_list= [
    
    "How many continents are there?",

    "What is the capital of India?",

    "What we study in Navgurukul?" ,

    "which state of india has no shortest coastline?" ,

    " which of these viruses taken it is name from a place  in malaysia?" 
]

options_list = [

    ["Four", "Nine", "Seven", "Eight"],

    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],

    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],

    ["maharastra","goa","odisa","west bangal"],

    ["nipah","ebola","influenia","HIV"]
]

solution_list = [3, 4, 1, 2,2]


answer=[["3.seven","4.eight"],["3.chennai","4.delhi"],["1.software enginearing","2. councealing"],["2. goa","3. odisa"],["2.ebola","4.HIV"]]

i=0
count=0
p=0
print("WELCOME TO KAUN BANEGA CROREPATI:")
while i<len(question_list):
    print("Your question is :")
    print(question_list[i])
    print("Your options are :")
    j=0
    z=i
    while j<len(options_list[i]):
        print(options_list[i][j])
        j+=1
    c=input("Do you want to use 50-50 lifeline :")

    if  c=="yes":
        print()
        if count<1:
            print(answer[z])
            r=int(input("ANSWER : "))
            if r== solution_list[i]:
                print("  Well played ! Your answer is Correct: ")
                p=p+10000
                print(" you win" ,p,)
            else:
                print("Incorrect answer.",("\U0001F612"))
                print("WIN",p)
                break
            count=count+1
        else:
            print("Sorry ! You have already used lifeline")
            r2=int(input("ANSWER"))
            if r2== solution_list[i]:
                print("  Well played 🎊! Your answer is correct: ")
                p=p+10000
                print(" YOU WIN",p)
            else:
                print("Incorrect answer")
                print(" YOU WIN",p,"")
    else:
        r3=int(input("ANSWER :"))
        if r3==solution_list[i]:
            print("Correct your answer")
            p=p+10000
            print(" YOU WIN",p,"")
        else:
            print("Wrong answer",("\U0001F612"))
            print(" YOU WIN",p,"")
    i=i+1
print("You win total amount",p)
print("Congratulations ! 🥳🥳")
print("Thankyou for participating in KBC:")
print("Game Over ","\U0001F607")