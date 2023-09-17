import random

class NumberGuessingGame:
    def __init__(self):
        self.low = 1
        self.high = 100
        self.rand_num = random.randint(self.low, self.high)
        self.guess = 0
        self.tries = 0

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between {} and {}.".format(self.low, self.high))
        print("Try to guess it!")
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess < self.low or guess > self.high:
                    print("Please guess within the range of {} and {}.".format(self.low, self.high))
                    continue

                self.tries += 1

                if guess == self.rand_num:
                    print(f"Congratulations! You guessed the number {self.rand_num} in {self.tries} tries.")
                    self.play_again()
                elif guess > self.rand_num:
                    print("Your guess is too high. Try again.")
                else:
                    print("Your guess is too low. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            self.reset_game()
        else:
            print("Thank you for playing!")
            exit()

    def reset_game(self):
        self.rand_num = random.randint(self.low, self.high)
        self.tries = 0

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
