import random
woord = ["hottentottententententoonstelling", "aansprakelijkheidswaardevaststellingsveranderingen", "meervoudigepersoonlijkheidsstoornis", "weinig", "klein", "ik", " levensverzekeringsaangelegenheden", "stokbrood", "chocoladetaart", "Kindercarnavalsoptochtvoorbereidingswerkzaamhedencomitéleden", "Lagekostenluchtvaartmaatschappij"]
fouten = 0
gekozenwoord = (random.choice(woord))
nietmogelijk = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "-", "_", "[", "]", "{", "}", ";", ":", "\\", "|", "`", "~", "'", "."]
woordraden = ""
res = ""
geraden = []
boodschap4 = '''
Je hebt 3 fouten
__________
|
|
|
|
|
|______
'''
boodschap2 = '''
Je hebt 1 fout
______
'''
boodschap3 = '''
Je hebt 2 fouten
|
|
|
|
|
|______
'''
boodschap5 = '''
Je hebt 4 fouten
__________
|/        |
|
|
|
|
|______
'''
boodschap6 = '''
Game over!

_________
|        |
|       ( )
|       /|\\
|       / \\
|
|
|______
'''

def print_welkom():
  boodschap = '''
Welkom bij
   ___    __    __    ___   ____  ____
  / __)  /__\  (  )  / __) (_  _)( ___)
 ( (_-. /(__)\  )(__( (_-..-_)(   )__)
  \___/(__)(__)(____)\___/\____) (____)
'''

  print(boodschap)

def vraag_input():
    global woordraden
    global fouten
    global raden
    global geraden
    raden = input("raad een letter of type ? om het woord te raden ")

    if raden == "... Was the imposter":
        print(gekozenwoord)
    elif raden == "?":
        woordraden = input("raad het woord ")
        if woordraden == gekozenwoord:
            print("goed gedaan je hebt het woord geraden!!!")
        else:
            print(woordraden + " is niet het goede woord")
            fouten += 1
    elif len(raden) == 1:
        if raden in geraden:
            geraden.append(raden)
            print("die letter heb je al geraden")
        elif raden in gekozenwoord:
            print("De letter " + raden + " zit in het woord")
            geraden.append(raden)
        elif raden in nietmogelijk:
            print("dat is niet mogelijk")
        else:
            print("De letter " + raden + " zit niet in het woord")
            fouten += 1
            geraden.append(raden)
    else:
        print("dat is niet mogelijk probeer het opnieuw")

def hoeveel_fout():

    if fouten == 0:
      print("je hebt 0 fouten")
    elif fouten == 1:
      print(boodschap2)
    elif fouten == 2:
      print(boodschap3)
    elif fouten == 3:
      print(boodschap4)
    elif fouten == 4:
      print(boodschap5)
    elif fouten == 5:
      print(boodschap6)

## loop door letters van geheime woord:
## als letter in geraden:
## res = vers + letter
## anders
## res is vers + "_"
## res = ""
## woord is woord[]
## geraden = ["w", "z"]

def laten_zien():
    global res
#    if raden = woord[index][1]:
#        res[1] = raden
#    if raden = woord[index][2]:
#        res[2] = raden
#    if raden = woord[index][3]:
#        res[3] = raden
#    print("res")

    for i in gekozenwoord:
        if i in geraden:
            res = res + i

        else:
            res = res + "-"

    print(res)
    res = ""

def runner_code():

    doorgaan = True

    while doorgaan:
        vraag_input()
        hoeveel_fout()
        laten_zien()
        if (fouten == 5) or (woordraden == gekozenwoord):
            if fouten == 5:
                print("Jammer je hebt verloren het woord was " + gekozenwoord)
            elif woordraden == gekozenwoord:
                print("Goed gedaaaaaaaaan je hebt gewonnen!!!!!!!!!! het woord was " + gekozenwoord)

            doorgaan = False

runner_code()
