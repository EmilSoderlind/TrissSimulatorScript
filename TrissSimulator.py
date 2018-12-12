import random
from Triss import Triss
from datetime import datetime, time
import multiprocessing
from threading import Thread

# Create list of triss:es
trissList = []


def createTrissList(start, end):
    print("Calling: createTrissList({},{})".format(start, end))

    # Create 200000 triss
    for triss_number in range(start, end):
        current_triss = Triss()

        # Set each triss prize
        if triss_number > 432419:
            current_triss.setPrize(0)
            trissList.append(current_triss)
            continue

        elif 252720 <= triss_number <= 432419:
            current_triss.setPrize(30)
            trissList.append(current_triss)
            continue

        elif 43920 <= triss_number <= 252719:
            current_triss.setPrize(60)
            trissList.append(current_triss)
            continue

        elif 14120 <= triss_number <= 43919:
            current_triss.setPrize(90)
            trissList.append(current_triss)
            continue

        elif 6920 <= triss_number <= 14119:
            current_triss.setPrize(120)
            trissList.append(current_triss)
            continue

        elif 3160 <= triss_number <= 6919:
            current_triss.setPrize(150)
            trissList.append(current_triss)
            continue

        elif 1960 <= triss_number <= 3159:
            current_triss.setPrize(180)
            trissList.append(current_triss)
            continue

        elif 1007 <= triss_number <= 1959:
            current_triss.setPrize(300)
            trissList.append(current_triss)
            continue

        elif 697 <= triss_number <= 1006:
            current_triss.setPrize(500)
            trissList.append(current_triss)
            continue

        elif 497 <= triss_number <= 696:
            current_triss.setPrize(600)
            trissList.append(current_triss)
            continue

        elif 397 <= triss_number <= 496:
            current_triss.setPrize(900)
            trissList.append(current_triss)
            continue

        elif 232 <= triss_number <= 396:
            current_triss.setPrize(1000)
            trissList.append(current_triss)
            continue

        elif 152 <= triss_number <= 231:
            current_triss.setPrize(1500)
            trissList.append(current_triss)
            continue

        elif 82 <= triss_number <= 151:
            current_triss.setPrize(2000)
            trissList.append(current_triss)
            continue

        elif 52 <= triss_number <= 81:
            current_triss.setPrize(5000)
            trissList.append(current_triss)
            continue

        elif 12 <= triss_number <= 51:
            current_triss.setPrize(10000)
            trissList.append(current_triss)
            continue

        elif 10 <= triss_number <= 11:
            current_triss.setPrize(20000)
            trissList.append(current_triss)
            continue

        elif 8 <= triss_number <= 9:
            current_triss.setPrize(100000)
            trissList.append(current_triss)
            continue

        elif triss_number == 7:
            current_triss.setPrize(200000)
            trissList.append(current_triss)
            continue

        elif 2 <= triss_number <= 6:
            current_triss.setPrize(265000)
            trissList.append(current_triss)
            continue

        elif triss_number == 1:
            current_triss.setPrize(1000000)
            trissList.append(current_triss)
            continue

        elif triss_number == 0:
            current_triss.setPrize(2765000)
            trissList.append(current_triss)
            continue

    print("Done with ({}->{})".format(start, end))


def scramblelist(list):
    print("\n| Scrambeling.")
    dest = list[:]
    random.shuffle(dest)
    return dest


def main():
    start = datetime.now()
    print("Creating 2.000.000 tickets")

    generate_ticket_list()
    scrambled_list = scramblelist(trissList)

    print("| Done :{}\n".format(datetime.now() - start))
    prize_sum = 0

    # Looping through each triss in scrambled_list
    for trissIndex in range(0, 1999999):

        if not one_more_triss_check():
            break

        prize_sum = current_ticket(prize_sum, scrambled_list, trissIndex)
        trissIndex += 1

    printResult(prize_sum, trissIndex)


def generate_ticket_list():
    #  ------ Threading ------
    start_index = 0
    end_index = 2000000
    number_of_threads = multiprocessing.cpu_count()
    # Length of each interval
    part_lengths = int(end_index / number_of_threads)

    for intervalNumber in range(start_index, number_of_threads):
        temp_start_interval = part_lengths * intervalNumber
        temp_end_interval = part_lengths + (part_lengths * intervalNumber)

        thread = Thread(target=createTrissList, args=(temp_start_interval, temp_end_interval))
        thread.start()

    # Wait for all threads
    for intervalNumber in range(0, number_of_threads):
        thread.join()
    #  ------ Threading ------


def one_more_triss_check():
    print("Do you want to skrejp a triss?")
    user_response = input("(Press [Enter] to skrejp or write something to exit)\n")
    bol = user_response == ""
    return bol


def current_ticket(prizeSum, scrambledList, trissIndex):
    print("------- Triss #{} -------".format(trissIndex + 1))
    currTriss = scrambledList[trissIndex]
    prizeSum += currTriss.getPrize()
    print("You won {} SEK!".format(currTriss.getPrize()))
    print("------- Triss #{} -------\n\n".format(trissIndex + 1))
    return prizeSum


def printResult(prizeSum, trissIndex):
    print("\n---- Final skrejping stats ----")
    print("Skrejped: {} Triss:es".format(trissIndex))
    print("Spent: {} SEK".format(trissIndex * 30))
    print("Won: {} SEK".format(prizeSum))

    if prizeSum - (trissIndex * 30) > 0:
        print("Profit: {} SEK".format(prizeSum - (trissIndex * 30)))
    else:
        print("Loss: {} SEK".format(prizeSum - (trissIndex * 30)))

    print("---- Final skrejping stats ----")
    print("\nThank you, come again!")


if __name__ == '__main__':
    main()
