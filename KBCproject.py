# Python program for KBC Questions
question=("when was maharana pratap born?")
options="A.15 dec      B.9 may    C.12 jan     D.23 april "
print(question)
print(options)
answer=input().lower() #here the lower method is used to accept both lower and uppercase as input

if(answer== "b" ):
    print("Congrats You won 20,000 Rs Want To play more or take the prize?\n Type 'yes' to play more \n or 'no' to stop ")
    opinion=input()
    if(opinion=="yes"):
        print("Your Next Question is.....")
    else:
        print("Thanks For playing you can take your prize!!")
else:
    print("Oops!! Better Luck next time")