import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dark cave.")
    time.sleep(1)
    print("There are two paths in front of you.")

def choose_path():
    print("\nChoose your path:")
    print("1. Go left")
    print("2. Go right")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        return 'left'
    elif choice == '2':
        return 'right'
    else:
        print("Invalid choice. Try again.")
        return choose_path()

def left_path():
    print("\nYou chose the left path.")
    time.sleep(1)
    print("You encounter a friendly troll.")
    time.sleep(1)
    print("The troll offers you a magic potion.")
    time.sleep(1)

    potion_choice = input("Do you accept the potion? (yes/no): ")
    if potion_choice.lower() == 'yes':
        print("You drink the potion and feel invigorated!")
    else:
        print("You decline the potion. The troll waves goodbye.")

def right_path():
    print("\nYou chose the right path.")
    time.sleep(1)
    print("You come across a dragon!")
    time.sleep(1)
    print("The dragon stares at you.")

    action = input("Do you 'fight' or 'run'?: ")
    if action.lower() == 'fight':
        print("You bravely fight the dragon, but it's too powerful.")
        time.sleep(1)
        print("Game over! The dragon breathes fire.")
    elif action.lower() == 'run':
        print("You wisely choose to run away.")
        time.sleep(1)
        print("You escape the dragon and find a treasure chest!")
        time.sleep(1)
        print("Congratulations! You win the game.")

def main():
    introduction()
    path = choose_path()

    if path == 'left':
        left_path()
    elif path == 'right':
        right_path()

if __name__ == "__main__":
    main()
