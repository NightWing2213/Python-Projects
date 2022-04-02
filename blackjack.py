from pickletools import pylist
from tokenize import PlainToken
import random

#Dealer Cards
dealer = []
dsum = 0

#Player Cards
player = []
psum = 0


def deal(): #Deal Cards
    while len(dealer) != 2:
        dealer.append(random.randint(1, 13)) #randomly assign cards from 1 through 13
    tform(2)
    print("Dealer has: X & ", dealer[1]) #only show the second card

#Player Cards
    while len(player) != 2:
        player.append(random.randint(1, 13)) #randomly assign cards from 1 through 13
    tform(1)
    summation()
    print("Your hand: ", player, "Points: ", psum)
    if psum < 21:
        hitorstay()
    dhit()
    summation()
    print("Dealer had: ", dealer, "Points: ", dsum)
    if dsum == 21 & psum < 21:
        print("Dealer has 21, Dealer Wins!")
    elif psum > 21:
        print("You busted, Dealer Wins!")
    elif dsum > psum and dsum <22:
        print("Dealer Wins")
    elif psum == 21:
        print("BLACKJACK! YOU WIN!")
    elif psum > dsum and psum < 21 or psum < dsum and dsum > 21:
        print("YOU WIN!")
    elif psum == dsum and dsum <= 21:
        print("Draw")

def dhit():
    global dsum
    global psum
    if dsum < psum and psum < 21: #Hit while dealer is less than player and less than 21, else return
        while dsum < psum:
            dealer.append(random.randint(1, 13))
            tform(2)
            summation()
        return
    else:
        return


def hitorstay():
    if psum < 21:
        hos = str(input("Hit or Stay?"))
        if hos == "hit":
            player.append(random.randint(1,13))
            tform(1)
            summation()
            print("Your hand: ", player, "Points: ", psum)
            hitorstay()
            return
        else:
            return
    else:
        return

def tform(a): #Transform Ace and faace cards
    if a == 2:
        for i in range(len(dealer)):
            if dealer[i] == 1:
                dealer[i] = "A"
            if dealer[i] == 11:
                dealer[i] = "J"
            if dealer[i] == 12:
                dealer[i] = "Q"
            if dealer[i] == 13:
                dealer[i] = "K"
    if a == 1:
        for i in range(len(player)):
            if player[i] == 1:
                player[i] = "A"
            if player[i] == 11:
                player[i] = "J"
            if player[i] == 12:
                player[i] = "Q"
            if player[i] == 13:
                player[i] = "K"
def summation():
    global psum
    global dsum
    psum = 0
    dsum = 0
    for i in range(len(player)): #summation for player
        if player[i] == "J" or player[i] == "Q" or player[i] == "K":
            psum = psum + 10
        elif player[i] == "A":
            psum = psum + valoface(i, 1)
        elif int(player[i]) > 1 and int(player[i]) < 11:
            psum = player[i] + psum
    for i in range(len(dealer)): #summation for dealer
        if dealer[i] == "J" or dealer[i] == "Q" or dealer[i] == "K":
            dsum = dsum + 10
        elif dealer[i] == "A":
            dsum = dsum + valoface(i, 2)
        elif int(dealer[i]) > 1 and int(dealer[i]) < 11:
            dsum = dealer[i] + dsum
    return

def valoface(i, h): #decide whether the ace will be 1 or 11
    if h==1:
        if psum == 0 & i==0:
            if 1 + int(player[1]) > 10 or 1 + int(player[1])==3:
                return int(1)
            else:
                return int(11)
        if psum == 0 & i==1:
            if 1 + int(player[0]) > 10 or 1 + int(player[0])==3:
                return int(1)
            else:
                return int(11)
        else:
            if psum + 11 > 21:
                return int(1)
            else:
                return int(11)
    else:
        if dsum == 0 & i==0:
            if (1 + int(dealer[1]) > 10) or (1 + int(dealer[1])==3):
                return int(1)
            else:
                return int(11)
        if dsum == 0 & i==1:
            if 1 + int(dealer[0]) > 10 or 1 + int(dealer[0])==3:
                return int(1)
            else:
                return int(11)
        else:
            if dsum + 11 > 21:
                return int(1)
            else:
                return int(11)

if __name__ == "__main__":
    deal()