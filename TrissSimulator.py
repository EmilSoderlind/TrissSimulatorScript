import sys
import random
from Triss import Triss

# Old function
def doNumberOfTriss(n):
    print("Skrapar {} trisslotter".format(n))
    totVinst = 0
    trissCost = 30*n
    for n in range(0,n):
        totVinst = totVinst + doTriss()
    print("Du betalade {} SEK, och vann {} SEK".format(trissCost,totVinst))
    if(trissCost>totVinst):
        print("Förlust!", "{} SEK".format(totVinst-trissCost))
    else:
        print("Vinst!", "{} SEK".format(totVinst-trissCost))

def createTrissList():

    # Create list of triss:es
    trissList = []

    # Create 200000 triss
    for trissNumber in range(0,2000000):
        currTriss = Triss()

        # Printing progress
        sys.stdout.flush()
        prettyCreatedIndex = format(trissNumber+1, ',d')
        sys.stdout.write("\r| {}%".format(round(((trissNumber+1)/2000000)*100,1)))

        # Set each triss prize
        if(trissNumber > 432419):
            currTriss.setPrize(0)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 252720 and trissNumber <= 432419):
            currTriss.setPrize(30)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 43920 and trissNumber <= 252719):
            currTriss.setPrize(60)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 14120 and trissNumber <= 43919):
            currTriss.setPrize(90)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 6920 and trissNumber <= 14119):
            currTriss.setPrize(120)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 3160 and trissNumber <= 6919):
            currTriss.setPrize(150)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 1960 and trissNumber <= 3159):
            currTriss.setPrize(180)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 1007 and trissNumber <= 1959):
            currTriss.setPrize(300)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 697 and trissNumber <= 1006):
            currTriss.setPrize(500)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 497 and trissNumber <= 696):
            currTriss.setPrize(600)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 397 and trissNumber <= 496):
            currTriss.setPrize(900)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 232 and trissNumber <= 396):
            currTriss.setPrize(1000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 152 and trissNumber <= 231):
            currTriss.setPrize(1500)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 82 and trissNumber <= 151):
            currTriss.setPrize(2000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 52 and trissNumber <= 81):
            currTriss.setPrize(5000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 12 and trissNumber <= 51):
            currTriss.setPrize(10000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 10 and trissNumber <= 11):
            currTriss.setPrize(20000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 8 and trissNumber <= 9):
            currTriss.setPrize(100000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber == 7):
            currTriss.setPrize(200000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber >= 2 and trissNumber <= 6):
            currTriss.setPrize(265000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber == 1):
            currTriss.setPrize(1000000)
            # Append triss to list
            trissList.append(currTriss)
            continue
        elif(trissNumber == 0):
            currTriss.setPrize(2765000)
            # Append triss to list
            trissList.append(currTriss)
            continue

    return trissList

def scrambleList(list):
    dest = list[:]
    random.shuffle(dest)
    return dest

def main():

    # Constants
    skrejpTime = 4

    print("Creating 2.000.000 tickets")
    filledList = createTrissList()
    print("\n| Scrambeling.\n")
    scrambledList = scrambleList(filledList)

    prizeSum = 0

    # Looping through each triss in scrambledList
    for trissIndex in range(0,1999999):

        print("Do you want to skrejp a triss?")
        oneMore = input("(Press [Enter] to skrejp or write something to exit)\n")
        print(oneMore)
        # Comparing non case-sensetive
        if(oneMore == "" or oneMore is None):

            print("------- Triss #{} -------".format(trissIndex+1))
            currTriss = scrambledList[trissIndex]
            prizeSum += currTriss.getPrize()
            print("You won {} SEK!".format(currTriss.getPrize()))
            print("------- Triss #{} -------\n\n".format(trissIndex+1))

            trissIndex += 1
        else:
            break

    print("\n---- Final skrejping stats ----")

    print("Skrejped: {} Triss:es".format(trissIndex))
    print("Spent: {} SEK".format((trissIndex)*30))
    print("Won: {} SEK".format(prizeSum))
    if(prizeSum-(trissIndex*30) > 0):
        print("Profit: {} SEK".format(prizeSum-(trissIndex*30)))
    else:
        print("Loss: {} SEK".format(prizeSum-(trissIndex*30)))

    print("---- Final skrejping stats ----")


    print("\nThank you, come again!")


if __name__ == '__main__':
    main()
