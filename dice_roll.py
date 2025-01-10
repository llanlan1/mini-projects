
"""Dice Roll"""
from random import randint
from time import sleep


def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess


def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Maximum possible value is %d." % max_val
  return first_roll, second_roll, max_val


guess = get_user_guess()
first_roll, second_roll, max_val = roll_dice(6)


if guess > max_val:
  print "This move is invalid!"
else:
  print "Rolling..."
  sleep(2)
  print "The first roll is %d" % first_roll
  sleep(1)
  print "The second roll is %d" % second_roll
  sleep(1)
  total_roll = first_roll + second_roll
  print total_roll
  print "Result..."
  sleep(1)
  if guess == total_roll:
    print "You have won!"
  else:
    print "You have lost... try again!"


roll_dice(6)
