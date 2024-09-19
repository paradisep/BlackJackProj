import pygame
from cmdlinever import SetUpGame, CheckTVal, AddCardToHand
from sprite.spritesheet import Spritesheet

pygame.init()

#define screen size
SCREEN_W = 1000
SCREEN_H = 600

#create game window
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Black Jack")

#frame rate
clock = pygame.time.Clock()
FPS = 60

#blackjack variables
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
SetUpGame(Suits,GameStuff)

def Reinstate():
    global Suits
    global Clubs
    global Spades
    global Diamonds
    global Hearts
    global GameStuff
    global PlayerHand
    global DealerHand
    global TotalDealerVal
    global TotalPlayerVal
    global PlayerStanded
    global PlayerBusted
    global DealerBusted
    global DealerStanded
    global DealerMsgActive
    global startofwinscreen
    Suits = [{},{},{},{}]
    Clubs = Suits[0]
    Spades = Suits[1]
    Diamonds = Suits[2]
    Hearts = Suits[3]
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
    startofwinscreen = 0

#setting up spritesheet for cards
le_spritesheet = Spritesheet('sprite/spritesheet.png',0,0)
HeartsSprites = []
ClubsSprites = []
DiamondsSprites = []
SpadesSprites = []
for h in range(0,4):
    for s in range(0,13):
        realnum = (h*13)+(s)
        if h==0: #0-12
            if realnum < 10:
                HeartsSprites.append(le_spritesheet.parse_sprite(f'tile00{realnum}.png'))
            if realnum >= 10:
                HeartsSprites.append(le_spritesheet.parse_sprite(f'tile0{realnum}.png'))
        if h==1: #13 - 25
            ClubsSprites.append(le_spritesheet.parse_sprite(f'tile0{realnum}.png'))
        if h==2: #26 - 38
            DiamondsSprites.append(le_spritesheet.parse_sprite(f'tile0{realnum}.png'))
        if h==3: #39 - 51
            SpadesSprites.append(le_spritesheet.parse_sprite(f'tile0{realnum}.png'))
index = 0

AddCardToHand(Suits,PlayerHand)
AddCardToHand(Suits,PlayerHand)
AddCardToHand(Suits,DealerHand)
AddCardToHand(Suits,DealerHand)

DEALERMOVE = pygame.USEREVENT + 2
DealerIsMoving = False
pygame.time.set_timer(DEALERMOVE, 3000)
            # TO RESET WE NEED TO DO THESE:
            #    Reinstate()
            #    SetUpGame(Suits,GameStuff)
            #    AddCardToHand(Suits,PlayerHand)
            #    AddCardToHand(Suits,PlayerHand)
            #    AddCardToHand(Suits,DealerHand)
            #    AddCardToHand(Suits,DealerHand)
#game loop
run = True
startofwinscreen=0
while run:
    myfont = pygame.font.SysFont("monospace", 30,bold=True)
    other = pygame.font.SysFont("arial",60,bold=True,italic=True)
    Hittxt = myfont.render('Hit', True, 'Red')
    Hitbutton = pygame.Rect(SCREEN_W/5,SCREEN_H/2,110,60)
    Standtxt = myfont.render('Stand', True, 'Blue')
    Standbutton = pygame.Rect((SCREEN_W/4)*3,SCREEN_H/2,110,60)
    
    #DEV RESET BUTTON
    Resettxt = myfont.render('replay', True, 'Black')
    ResetButton = pygame.Rect(SCREEN_W/2-55,SCREEN_H/4*3,110,60)
    
    clock.tick(FPS)
    #update background
    screen.fill("dark green")
    backsplash = other.render("DEALER STANDS ON 17", True, "Black")
    backsplash.set_alpha(125)
    screen.blit(backsplash,(SCREEN_W/5*2,SCREEN_H/2-100))
    
    handposP=0
    handposD=0
    if len(list(PlayerHand.keys()))>0:
      for key, value in list(PlayerHand.items()):
          handposP+=1
          if "jack" in key.lower():
            index=9
          elif "queen" in key.lower():
              index=10
          elif "king" in key.lower():
              index=11
          elif "ace" in key.lower():
              index=12
          else:
              index=value-2
          if "hearts" in key.lower():
              screen.blit(HeartsSprites[index],((((SCREEN_W/((len(list(PlayerHand.keys())))+1))*handposP)) - 142/2,(SCREEN_H/2)+100))
          elif "clubs" in key.lower():
              screen.blit(ClubsSprites[index],((((SCREEN_W/((len(list(PlayerHand.keys())))+1))*handposP)) - 142/2,(SCREEN_H/2)+100))
              index+=13
          elif "diamonds" in key.lower():
              screen.blit(DiamondsSprites[index],((((SCREEN_W/((len(list(PlayerHand.keys())))+1))*handposP)) - 142/2,(SCREEN_H/2)+100))
              index+=13*2
          elif "spades" in key.lower():
              screen.blit(SpadesSprites[index],((((SCREEN_W/((len(list(PlayerHand.keys())))+1))*handposP)) - 142/2,(SCREEN_H/2)+100))
              index+=13*3
    if len(list(DealerHand.keys()))>0:
        for key, value in list(DealerHand.items()):
            handposD+=1
            if PlayerBusted==False and PlayerStanded==False:                
                if handposD==2:
                    break
            if "jack" in key.lower():
                index=9
            elif "queen" in key.lower():
                index=10
            elif "king" in key.lower():
                index=11
            elif "ace" in key.lower():
                index=12
            else:
                index=value-2
            if "hearts" in key.lower():
                screen.blit(HeartsSprites[index],((((SCREEN_W/((len(list(DealerHand.keys())))+1))*handposD)) - 142/2,(10)))
            elif "clubs" in key.lower():
                screen.blit(ClubsSprites[index],((((SCREEN_W/((len(list(DealerHand.keys())))+1))*handposD)) - 142/2,(10)))
                index+=13
            elif "diamonds" in key.lower():
                screen.blit(DiamondsSprites[index],((((SCREEN_W/((len(list(DealerHand.keys())))+1))*handposD)) - 142/2,(10)))
                index+=13*2
            elif "spades" in key.lower():
                screen.blit(SpadesSprites[index],((((SCREEN_W/((len(list(DealerHand.keys())))+1))*handposD)) - 142/2,(10)))
                index+=13*3
    TotalPlayerVal = CheckTVal(PlayerHand)
    TotalDealerVal = CheckTVal(DealerHand)
    #hit&stand buttons
    mousex,mousey = pygame.mouse.get_pos()
    if Hitbutton.x <= mousex <= Hitbutton.x + Hitbutton.w and Hitbutton.y <= mousey <= Hitbutton.y + Hitbutton.h and PlayerStanded==False and PlayerBusted==False:
        pygame.draw.rect(screen,(180,180,180),Hitbutton)
    else:
        pygame.draw.rect(screen, (110,110,110),Hitbutton)
    screen.blit(Hittxt,(Hitbutton.x+(Hitbutton.w/10),Hitbutton.y+(Hitbutton.h/10)))
    if Standbutton.x <= mousex <= Standbutton.x + Standbutton.w and Standbutton.y <= mousey <= Standbutton.y + Standbutton.h and PlayerStanded==False and PlayerBusted==False:
        pygame.draw.rect(screen,(180,180,180),Standbutton )
    else:
        pygame.draw.rect(screen, (110,110,110),Standbutton)
    screen.blit(Standtxt,(Standbutton.x+(Standbutton.w/10),Standbutton.y+(Standbutton.h/10)))
    
    #DEV RESET BUTTON
    
    
    
    #event handler
    for event in pygame.event.get():
    #quit program
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if TotalPlayerVal<=21 and PlayerStanded==False and PlayerBusted==False:
                if Hitbutton.collidepoint(event.pos):
                    pygame.draw.rect(screen,(255,255,255),pygame.Rect(SCREEN_W/5,SCREEN_H/2,110,60))
                    AddCardToHand(Suits,PlayerHand)
                    TotalPlayerVal = CheckTVal(PlayerHand)
                elif Standbutton.collidepoint(event.pos):
                    pygame.draw.rect(screen,(255,255,255),pygame.Rect((SCREEN_W/4)*3,SCREEN_H/2,110,60))
                    PlayerStanded=True
            if ResetButton.collidepoint(event.pos):
                Reinstate()
                SetUpGame(Suits,GameStuff)
                AddCardToHand(Suits,PlayerHand)
                AddCardToHand(Suits,PlayerHand)
                AddCardToHand(Suits,DealerHand)
                AddCardToHand(Suits,DealerHand)
        if event.type == DEALERMOVE:
            if (PlayerStanded==True or PlayerBusted==True) and DealerStanded==False and DealerBusted==False:
                if TotalDealerVal<17:
                    AddCardToHand(Suits,DealerHand)
                    TotalDealerVal = CheckTVal(DealerHand)
                elif TotalDealerVal>=17 and TotalDealerVal<=21:
                    DealerStanded=True
                elif TotalDealerVal>21:
                    DealerBusted=True
    if TotalPlayerVal>21:
        PlayerBusted=True
    pob = "filler"
    pobcolor = "filler"
    if PlayerStanded==True or PlayerBusted==True and DealerBusted==False and DealerStanded==False:
        if PlayerStanded==True:
            pob="Stood"
            pobcolor = "Blue"
        elif PlayerBusted==True:
            pob="Bust"
            pobcolor = "Red"
        screen.blit(myfont.render(f'Player has {pob}', True, pobcolor),(SCREEN_W/3,SCREEN_H/2))
            
    screen.blit(myfont.render(f'You have: {TotalPlayerVal}',True,'Black'),(25,(SCREEN_H/3*2)-30))
    if (PlayerBusted==True or PlayerStanded==True):
        screen.blit(myfont.render(f'Dealer has: {TotalDealerVal}',True,'Black'),(25,(SCREEN_H/3)))
    
    if ((PlayerBusted==True or PlayerStanded==True) and (DealerBusted==True or DealerStanded==True)) and startofwinscreen==0:
        startofwinscreen = pygame.time.get_ticks()
    if pygame.time.get_ticks()-startofwinscreen>=2000 and startofwinscreen!=0:
        screen.fill("dark green")
        winfont = pygame.font.SysFont("papyrus",60,bold=True,italic=True)
        if ResetButton.x <= mousex <= ResetButton.x + ResetButton.w and ResetButton.y <= mousey <= ResetButton.y + ResetButton.h:
            pygame.draw.rect(screen,(180,180,180),ResetButton )
        else:
            pygame.draw.rect(screen, (110,110,110),ResetButton)
        screen.blit(Resettxt,(ResetButton.x+(ResetButton.w/10)-10,ResetButton.y+(ResetButton.h/10)))
        if PlayerBusted==False and DealerBusted==False:
            if TotalDealerVal>TotalPlayerVal:
                screen.blit(winfont.render(f'Dealer wins with {TotalDealerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4))
                screen.blit(winfont.render(f'You lose with {TotalPlayerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4+60))
            elif TotalDealerVal==TotalPlayerVal:
                screen.blit(winfont.render(f'You and the Dealer tie with {TotalPlayerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4))
            elif TotalPlayerVal>TotalDealerVal:
                screen.blit(winfont.render(f'You won with {TotalPlayerVal}, Congrats!', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4))
                screen.blit(winfont.render(f'Dealer loses with {TotalDealerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4+60))
        elif PlayerBusted==True and DealerBusted==False:
            screen.blit(winfont.render(f'Dealer wins with {TotalDealerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4))
            screen.blit(winfont.render(f'You busted with {TotalPlayerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4+60))
        elif PlayerBusted==False and DealerBusted==True:
            screen.blit(winfont.render(f'You win with {TotalPlayerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4))
            screen.blit(winfont.render(f'Dealer busted with {TotalDealerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4+60))
        elif PlayerBusted==True and DealerBusted==True:
            screen.blit(winfont.render(f'Dealer wins with {TotalDealerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4))
            screen.blit(winfont.render(f'You busted with {TotalPlayerVal}', True, "Black"),(SCREEN_W/4-100,SCREEN_H/4+60))
        
    
    #update display
    pygame.display.update()

pygame.quit()
