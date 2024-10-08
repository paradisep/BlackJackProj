import random as rand
#setting up suits
Suit_temp = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10,"Ace":[1,11]}
Suits = [{},{},{},{}]
Clubs = Suits[0]
Spades = Suits[1]
Diamonds = Suits[2]
Hearts = Suits[3]
#instancing gamestuff
GameStuff = [{},{},0,0,False,False,False,False,False]
#instancing Hands
PlayerHand = GameStuff[0]
DealerHand = GameStuff[1]
#instancing Hand Values
TotalPlayerVal = GameStuff[2]
TotalDealerVal = GameStuff[3]
#GameStates
PlayerStanded = GameStuff[4]
PlayerBusted = GameStuff[5]
DealerBusted = GameStuff[6]
DealerStanded = GameStuff[7]
DealerMsgActive=GameStuff[8]
#bundle all used game stuff together to easily reset
def SetUpGame(S,GS):
    if len(S)>1:
        for suit in range(0,len(S)):
            for key in list(Suit_temp.keys()):
                if suit==0:
                    S[suit][f"{key} of Clubs"] = Suit_temp[key]
                if suit==1:
                    S[suit][f"{key} of Spades"] = Suit_temp[key]
                if suit==2:
                    S[suit][f"{key} of Diamonds"] = Suit_temp[key]
                if suit==3:
                    S[suit][f"{key} of Hearts"] = Suit_temp[key]
    if len(GS)>1:
        #reseting Hands
        GS[0] = {} #PlayerHand = {}
        GS[1] = {} #DealerHand = {}
        #resting Hand Values
        GS[2] = 0 #TotalPlayerVal = 0
        GS[3] = 0 #TotalDealerVal = 0
        #Resting Game States
        GS[4] = False #PlayerStanded = False
        GS[5] = False #PlayerBusted=False
        GS[6] = False #DealerBusted=False
        GS[7] = False #DealerStanded=False
        GS[8] = False #DealerMsgActive=False

#function checks the total value of player's hand
def CheckTVal(Hand):
    temptotal=0
    #has ace checks if the player has ace and adjusts player's total hand value as such
    HasAce = False
    for x in Hand:
        if  "ace" in x.lower() or type(Hand[x])==list:
            HasAce=True
        else:
            temptotal+=Hand[x]
    if temptotal+11>21 and HasAce==True:
        temptotal+=1
    elif HasAce==True:
        temptotal+=11
    #function returns total of player's hand
    return temptotal
#functionally the same as the CheckPlayerTVal function but replace's the PlayerHand with DealerHand
#function adds a card to the respective hand which is given in the Hand variable
def AddCardToHand(Suits, Hand):
    Stemp = rand.choice(Suits)
    e=True
    #checking if all suits are empty!!! if they are then rip...
    while e==True:
        emptysuits=0
        for x in Suits:
            if len(x)<=0:
                emptysuits+=1
        if emptysuits>=4:
            e=False
            return print("All Suits Empty")
        if len(Stemp)>0:
            e=False
        else:
            Stemp = rand.choice(Suits)
    cardname,cardval = rand.choice(list(Stemp.items()))
    Hand[cardname] = Stemp[cardname]
    del Stemp[cardname]
'''
SetUpGame(Suits,GameStuff)
#setting up player hand for gameplay loop
AddCardToHand(PlayerHand)
AddCardToHand(PlayerHand)
#setting up dealer hand for gameplay loop
AddCardToHand(DealerHand)
AddCardToHand(DealerHand)

#Full gameplay loop starts here with checking the Player's card values and telling the player one card the dealer has
#and one card they have.
TotalPlayerVal = CheckPlayerTVal()
print(f"You have {list(PlayerHand.keys())} which is a {TotalPlayerVal} ")
print(f"Dealer has {rand.choice(list(DealerHand.keys()))}")

#Actual gameplay starts here with the player deciding to hit or stand, this is done with some boolean gamestates
while PlayerStanded==False and PlayerBusted==False:
    #get player input (no try catchs cuz like, it dont matta, we're getting a string anyway)
    hitorstand = str(input("Would you like to hit or stand? :")).lower()
    if "stand" in hitorstand:
        print("You have stood")
        PlayerStanded=True
    elif "hit" in hitorstand:
        AddCardToHand(PlayerHand)
        print(f"You have {PlayerHand}")
        TotalPlayerVal = CheckPlayerTVal()
        print(f"Which is {TotalPlayerVal}")
    if TotalPlayerVal>21:
        print(f"You busted with {PlayerHand}")
        PlayerBusted=True
#After the Player is has stood or busted the Dealer goes next, or doesnt depending on if the player busts.
TotalDealerVal = CheckDealerTVal()
print(f"Dealer has {DealerHand}")
if PlayerBusted==False:
    #checks if dealer has less than 17 (because dealer stands on 17)
    while TotalDealerVal<17:
            print("Dealer has hit")
            AddCardToHand(DealerHand)
            TotalDealerVal = CheckDealerTVal()
            print(f"Dealer now has {DealerHand}")
    #checks if dealer has more than 17 (but less than 21 to not cause the dealer to accidentally say
    #they stood when they busted)
    if TotalDealerVal>=17 and TotalDealerVal<=21 :
        print(f"Dealer has stood with a {TotalDealerVal}")
    #dealer bust check
    if TotalDealerVal>21:
        print(f"Dealer has busted with {TotalDealerVal}")
        DealerBusted=True

#these four if statements check gamestates parameters and declare if player won, lost, or tied against the dealer
if PlayerBusted==False and DealerBusted==False:
    #main gameplay happens here, player and the dealer should regularly *not* bust.
    if TotalDealerVal>TotalPlayerVal:
        print(f"Dealer wins with {TotalDealerVal}.")
        print(f"You lose with {TotalPlayerVal}")
    elif TotalDealerVal==TotalPlayerVal:
        print(f"You and the Dealer tied on a {TotalPlayerVal}")
    elif TotalPlayerVal>TotalDealerVal:
        print(f"You won with a {TotalPlayerVal}, Congratulations!")
elif PlayerBusted==True and DealerBusted==False:
    print(f"Dealer wins with {TotalDealerVal}.")
    print(f"You lose with {TotalPlayerVal}")
elif PlayerBusted==False and DealerBusted==True:
    print(f"You win with {TotalPlayerVal}.")
    print(f"Dealer loses with {TotalDealerVal}")
elif PlayerBusted==True and DealerBusted==True:
    print(f"You and the dealer both busted on {TotalPlayerVal}")
    print("You tie, I guess...")
'''