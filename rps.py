#!/usr/bin/env python3

# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""

# The Player class is selected at random for the computer.
# Select the number of rounds and enjoy.
import random
moves = ['rock', 'paper', 'scissors']


def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.move_temp = "rock"

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        self.move_temp = their_move


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.step = 0

    def move(self):
        throw = None
        if self.step == 0:
            throw = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            throw = moves[1]
            self.step = self.step + 1
        else:
            throw = moves[2]
            self.step = self.step + 1
        return throw
        while moves > 2:
            throw = moves[0]

class HumanPlayer(Player):
    def move(self):
        throw = input('rock, paper, scissors: ')

        while throw != 'rock' and throw != 'paper' and throw != 'scissors':
            print('Throw again')
            throw = input('rock, paper, scissors: ')
        return throw


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} <> Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1_score += 1
            print('** Player 1 wins! **')
        else:
            if move1 == move2:
                print('** Tie **')
            else:
                self.p2_score += 1
                print('** Player 2 wins! **')

        print(f"Player:{self.p1.__class__.__name__}, Score:{self.p1_score}")
        print(f"Player:{self.p2.__class__.__name__}, Score:{self.p2_score}")

    def play_game(self):
        print("Game start!")
        number_rounds = inputNumber("How many round do you want to play? ")
        for round in range(number_rounds):
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print('** Congrats! Player 1 WINS! **')
        elif self.p2_score > self.p1_score:
            print('** Sadly Player 2 WINS! **')
        else:
            print('** The match was a tie! **')
        print('The final score is ' + str(self.p1_score) + ' TO ' +
              str(self.p2_score))
        print("Game over!")


if __name__ == '__main__':
    strategies = {
        "1": Player(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer()
    }

    user_input = inputNumber("Select the player strategy "
                             "you want to play against: "
                             "1-Rock Player "
                             "2-Random Player "
                             "3-Cycle Player "
                             "4-Reflect Player ")
    # p1 = HumanPlayer()
    # p2 = Player()
    game = Game(HumanPlayer, strategies[user_input])
    game.play_game()
