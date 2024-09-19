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
GameStuff = [{},{},0,0,False,False,False]
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
SetUpGame(Suits,GameStuff)

#get hit stand buttons:

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

#game loop
run = True
while run:
    myfont = pygame.font.SysFont("monospace", 30,bold=True)
    Hittxt = myfont.render('Hit', True, 'Red')
    Hitbutton = pygame.Rect(SCREEN_W/5,SCREEN_H/2,110,60)
    Standtxt = myfont.render('Stand', True, 'Blue')
    Standbutton = pygame.Rect((SCREEN_W/4)*3,SCREEN_H/2,110,60)
    clock.tick(FPS)
    #update background
    screen.fill("dark green")
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
    #event handler
    for event in pygame.event.get():
    #quit program
        if event.type == pygame.QUIT:
            run = False
        if PlayerStanded==False and PlayerBusted==False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Hitbutton.collidepoint(event.pos):
                    pygame.draw.rect(screen,(255,255,255),pygame.Rect(SCREEN_W/5,SCREEN_H/2,110,60))
                    AddCardToHand(Suits,PlayerHand)
                elif Standbutton.collidepoint(event.pos):
                    pygame.draw.rect(screen,(255,255,255),pygame.Rect((SCREEN_W/4)*3,SCREEN_H/2,110,60))
                    PlayerStanded=True
                    
    #update display
    pygame.display.update()

pygame.quit()
