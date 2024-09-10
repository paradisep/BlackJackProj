import random as rand
Suit_temp = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10,"Ace":[1,11]}
#setting up suits
Clubs = {**Suit_temp}
Spades = {**Suit_temp}
Diamonds = {**Suit_temp}
Hearts = {**Suit_temp}
Suits = [Clubs,Spades,Diamonds,Hearts]
#instancing Hands
PlayerHand = {}
DealerHand = {}

#gameplay loop below, setting up player hand
Stemp = rand.choice(Suits)
cardname,cardval = rand.choice(list(Stemp.items()))
PlayerHand[cardname] = Stemp[cardname]
del Stemp[cardname]
Stemp = rand.choice(Suits)
cardname,cardval = rand.choice(list(Stemp.items()))
PlayerHand[cardname] = Stemp[cardname]
del Stemp[cardname]
#setting up dealer hand
Stemp = rand.choice(Suits)
cardname,cardval = rand.choice(list(Stemp.items()))
DealerHand[cardname] = Stemp[cardname]
del Stemp[cardname]
Stemp = rand.choice(Suits)
cardname,cardval = rand.choice(list(Stemp.items()))
DealerHand[cardname] = Stemp[cardname]
del Stemp[cardname]
print(f"You have {list(PlayerHand.keys())}")
print(f"Dealer has {rand.choice(list(Stemp.keys()))}")