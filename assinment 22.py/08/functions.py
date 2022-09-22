import sys
import time
import datetime


def usage():
    print("countdown.py <number>")

def countdown_timer():
    print(sys.argv)
    if len(sys.argv) == 2:
        try:
            countdown = int(sys.argv[1])
        except ValueError:
            print("Please enter a valid number")
            sys.exit(-1)
    else:
        usage()
        sys.exit(-1)
    
    while countdown > 0:
        # 00:00:00
        countdown_time = str(datetime.timedelta(seconds=countdown))
        print(countdown_time)
        time.sleep(1)
        countdown -= 1
    print("countdown finished")


def main():


    countdown_timer()


if __name__ == '__main__':
    main()

# Rock, Paper , Scissors
import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie!'

    #r>s, s>p, p>r
    if is_win(user, computer):
        return "You won!"

    return 'You Lost!'

def is_win(player, opponent):
    print(f"user: {player}")
    print(f"computer: {opponent}")
    # return true if player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def main():
    print(play())


if __name__ == "__main__":
    main()


    
