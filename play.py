def rules():
    print("R: Rock\nS: Scissor\nP: Paper")
    print("Enter 'no' in the both fieds to stop playing.")
rules()
lst = ["R", "S", "P"]
w1 = ["R", "S"]
w2 = ["S", "P"]
w3 = ["P", "R"]
while 1:
    p1 = input("Player1: ")
    p2 = input("Player2: ")
    p1 = p1.upper()
    p2 = p2.upper()
    
    if(p1!= "" and p2!= ""):
        if(p1=="NO" and p2=="NO"):
            break
        elif(p1 not in lst or p2 not in lst):
            print("Wrong Entry...Try again")
            rules()
        else:
            if(p1 in w1):
                if(p2 in w1):
                    if(p1 == w1[0]):
                        print("Winner is: Player1")
                    else:
                        print("Winner is: Player2")
            if(p1 in w2):
                if(p2 in w2):
                    if(p1 == w2[0]):
                        print("Winner is: Player1")
                    else:
                        print("Winner is: Player2")
            if(p1 in w3):
                if(p2 in w3):
                    if(p1 == w3[0]):
                        print("Winner is: Player1")
                    else:
                        print("Winner is: Player2")
    else:
        print("You must enter both values to play:")
        rules()
    
