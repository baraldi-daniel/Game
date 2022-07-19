import random

def translation(card):
    if card[0]==0:
        card_number="four"
    elif card[0]==1:
        card_number="five"
    elif card[0]==2:
        card_number="six"
    elif card[0]==3:
        card_number="seven"
    elif card[0]==4:
        card_number="queen"
    elif card[0]==5:
        card_number="joker"
    elif card[0]==6:
        card_number="king"
    elif card[0]==7:
        card_number="ace"
    elif card[0]==8:
        card_number="two"
    elif card[0]==9:
        card_number="three"

    if card[1]==1:
        suit="diamonds"
    elif card[1]==2:
        suit="spades"
    elif card[1]==3:
        suit="hearts"
    elif card[1]==4:
        suit="clubs"

    card_number_suit=card_number+" of "+suit

    return card_number_suit

def Strength_Order(manillas_inthegame,cards_inthegame):
    if manillas_inthegame != "":
        for o in manillas_inthegame:
            try:
                cards_inthegame.remove(o)
            except:
                True
        cards_inthegame.sort()
        cards_inthegame.extend(manillas_inthegame)
        cards_inthegame_sorted=cards_inthegame[:]
        
    else:
        cards_inthegame_sorted.sort()
        cards_inthegame_sorted=cards_inthegame[:]
        
        
            
    return cards_inthegame_sorted
    

def Computer_Move_and_Result(card_human, computer_deck, order, roundofgame, card_human_manilla):

    computer_card=[]
    possibilities_win=[]
    possibilities_equal=[]
    possibilities_lose=[]
    
    order_number_human=order.index(card_human)
    for i in computer_deck:
        if order.index(i)>order_number_human and card_human[1] != i[1] and card_human_manilla==True:
            possibilities_win.append(i)
        elif order.index(i)>order_number_human and card_human[0] != i[0]  and card_human_manilla==False:
            possibilities_win.append(i)
        elif card_human[0] == i[0] and card_human_manilla==False: #and roundofgame!=3:
            possibilities_equal.append(i)
        else:
            possibilities_lose.append(i)

    #print(possibilities_win)
    #print(possibilities_equal)
    #print(possibilities_lose)
    #print(order_number_human)
    #print(card_human_manilla)
    #print(possibilities_win != [])

    if possibilities_win != []:
        computer_card=random.choice(possibilities_win)
        winorlose="computerwin"
    elif possibilities_win==[] and possibilities_equal!=[]: #and roundofgame!=3:
        computer_card=random.choice(possibilities_equal)
        winorlose="tie"
    elif possibilities_win==[] and possibilities_lose!=[]:
        computer_card=random.choice(possibilities_lose)
        winorlose="computerlose"

    
    return computer_card,winorlose

quitgame=False

while quitgame==False:




    print("This is a card game called Truco Paulista (but without bluff) simplified to one game with 3 rounds, 1 card for each. You will receive three cards. More information at https://en.wikipedia.org/wiki/Truco, in the 'Truco Paulista' section")

    seq=range(0,10)
    suit=range(1,5)
    list_cards=[]
    weak2strong=[]
    manillas_e_vira=[]
    cards_inthegame=[]
    manillas_inthegame=[]
    computer_move=[]
    w=0
    order=[]
    cards_played=[]
    cards_played_user=[]
    cards_played_computer=[]
    roundofgame=3
    options={"A":0,"B":1,"C":2}
    human=0
    computer=0
    validation_option=False
    human_deck_final=[]
    computer_deck_final=[]
    

    #Main part:

    ##List Cards:
    for i in seq:
        for j in suit:
            card=[i,j]
            list_cards.append(card)

    ##Cards Weak 2 Strong
    list_cards.sort()
    weak2strong=list_cards[:]

    ##Choose Vira and Remove from Deck
    vira=random.choice(weak2strong)
    weak2strong.remove(vira)

    ##Choose Manillas
    manilla = vira[0]+1
    manilla_top1=[manilla,4]
    manilla_top2=[manilla,3]
    manilla_top3=[manilla,2]
    manilla_top4=[manilla,1]
    manillas=[manilla_top1,manilla_top2,manilla_top3,manilla_top4]


    ##Choose Cards to Computer
    computer_card1= random.choice(weak2strong)
    weak2strong.remove(computer_card1)
    computer_card2= random.choice(weak2strong)
    weak2strong.remove(computer_card2)
    computer_card3= random.choice(weak2strong)
    weak2strong.remove(computer_card3)

    ##Choose Cards to Human
    human_card1=random.choice(weak2strong)
    weak2strong.remove(human_card1)
    human_card2=random.choice(weak2strong)
    weak2strong.remove(human_card2)
    human_card3=random.choice(weak2strong)
    weak2strong.remove(human_card3)



    ##Define Decks
    human_deck=[human_card1, human_card2, human_card3]
    for i in human_deck:
        human_deck_final.append(translation(i))
        #print(human_deck_final)
    

    computer_deck=[computer_card1,computer_card2,computer_card3]
    for i in computer_deck:
        computer_deck_final.append(translation(i))


    while roundofgame>0:
        
    ##Define Options List and Remove Played
        options_list=list(options.keys())
        try: options_list.remove(options_list[roundofgame])
        except:
            True

        options_list_index=list(options.values())
        try: options_list_index.remove(options_list_index[roundofgame])
        except:
            True

        options=dict(zip(options_list,options_list_index))
        #print(options)
        

    ##Define Cards in The Game
        for e in cards_played_user:
            try:
                human_deck.remove(e)
            except:
                True
        cards_inthegame=human_deck[:]
        
        for r in cards_played_computer:
            try:
                computer_deck.remove(r)
            except:
                True
        cards_inthegame.extend(computer_deck)
        #print(cards_inthegame)

    #Define Manillas in the Game and Sort by Strength
        q=0
        for p in cards_inthegame:
            #if q<3:
                #print("\nUser card:", translation(p), p)
            #else:
                #print("\nComputer card:",translation(p), p)
            q+=1
            if p in manillas:
                manillas_inthegame.append(p)
                manillas_inthegame.sort(key=lambda x:x[1])

    #Define Order
        order=Strength_Order(manillas_inthegame, cards_inthegame)
        #print("\n")
        #print(order)

    #Define Round of Game
        roundplaying=4-roundofgame
            

    
    #Score:
        print("_______________________________________________")
        print("Round:", roundplaying)
        score="human:"+str(human)+"||"+"computer:"+str(computer)
        print("\n======================================")
        print("Score:",score)
        print("======================================\n")

    ##Print Vira
        print("\n***************************************")
        print("The turned card is:", translation(vira)) #,vira)
        print("***************************************\n")

    ##Moves
        print("Make your move! Your cards are:\n")
        for u in options_list:
            print(u,": ", translation(human_deck[options[u]]))

        while validation_option==False:
            move_human=input("\nEnter the option you want:")
            move_human=move_human.upper()
            if move_human.upper() in options_list:
                validation_option=True
            else:
                print("Oops! Invalid option!")
                
        validation_option=False
        card_human=human_deck[int(options[move_human])]
        if card_human in manillas_inthegame:
            card_human_manilla=True
        else:
            card_human_manilla=False



    ##Game_Round
        computer_move=Computer_Move_and_Result(card_human,computer_deck, order, roundofgame, card_human_manilla)
        computer_card=computer_move[0]
        winorlose=computer_move[1]

        print("----------------------------------------------------------------------")
        print("You played:", translation(card_human))#, card_human)
        print("The computer played:", translation(computer_card))#,computer_card)
        print("----------------------------------------------------------------------")
        #print(cards_inthegame)

        
        if winorlose == "computerwin":
            computer=computer+1
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("The computer win this round")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        elif winorlose == "tie":
            human=human+1
            computer=computer+1
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("This round is tied")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        else:
            human=human+1
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("Congrats, you win this round")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        

        

        ##Add to cards played
        cards_played_user.append(card_human)
        cards_played_computer.append(computer_card)
        #print(cards_played_user)
        #print(cards_played_computer)

        roundofgame-=1
        

    ##Results
    if human>computer:
        score="human:"+str(human)+"||"+"computer:"+str(computer)
        print("\n++++++++++++++++++++++++++++++++++++++")
        print("Final Score:",score)
        print("Congratulations! You win the game!")
        print("++++++++++++++++++++++++++++++++++++++++\n")
        print("The computer cards were:","[",computer_deck_final[0],";",computer_deck_final[1],";",computer_deck_final[2],"]")
        print("Your cards were:","[",human_deck_final[0],";",human_deck_final[1],";",human_deck_final[2],"]")
    elif computer>human:
        score="human:"+str(human)+"||"+"computer:"+str(computer)
        print("\n++++++++++++++++++++++++++++++++++++++")
        print("Final Score:",score)
        print("Not this time.. The computer win the game!")
        print("++++++++++++++++++++++++++++++++++++++++\n")
        print("The computer cards were:","[",computer_deck_final[0],";",computer_deck_final[1],";",computer_deck_final[2],"]")
        print("Your cards were:","[",human_deck_final[0],";",human_deck_final[1],";",human_deck_final[2],"]")

    playagain=input("\nDo you want to play again? (press enter/type no)\n")

    if playagain=="":
        quitgame=False
    elif playagain=="no":
        quitgame=True
    