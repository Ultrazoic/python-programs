import random
import string


def get_random():
    rand=""
    for i in range(3):
        rand=rand+random.choice(string.ascii_lowercase)
    return rand
    

print("Press 1 to Code secret Language OR Press 0 to decode it!!")
cmd = int(input())

# program to code
if(cmd==1):
    dm="enter the message you want to convert \n"
    print(dm.title())

    m = input()
    words=(m.split(" "))
    nwords = []
    for word in words:
        if(len(words)<3):
            m=m[::-1]
            nwords.append(m)
    
        else: 
            m1=get_random()+word[1:]+word[0]+get_random()
            nwords.append(m1)

    print(" ".join(nwords))
        
#program to decode
elif(cmd==0):
    cm="enter the message you want to decode\n"
    print(cm.title())
    r= input()
    words1=r.split(" ")
    nwords1=[]
    for word1 in words1:
        if(len(words1)<3):
            r=r[::-1]
            nwords1.append(r)
            
        else:
            r1=word1[3:-3]
            r1=r1[-1]+r1[0:-1]
            nwords1.append(r1)
    print(" ".join(nwords1))

 

