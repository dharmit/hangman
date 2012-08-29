#!/bin/env python
import random
import sys

def pick_random(l, ln):
    while 1:
        word = random.choice(l)
        if len(word) != ln:
            continue
        else:
            return word.upper()

def create_lists(word):
    words = list(word)
    guesses = []
    for i in range(0,len(word)):
        guesses.append('')
    return words, guesses

def play_game(words, guesses, wrongs):
    for i in guesses:
        if i == '':
            print '_ ',
        else:
            print i + ' ',
    print "\n"
    char = raw_input("Pick a letter : ")
    char = char.upper()
    if char in wrongs or char in guesses:
        print "Sorry, you already guesses '%s'" % char
        print
        return play_game(words, guesses, wrongs)
    elif char in words:
        indices = [i for i in range(0, len(words)) if words[i] == char]
        for i in range(0, len(indices)):
            guesses[indices[i]:indices[i]+1] = char
        if guesses == words:
            for i in guesses:
                print i + ' ',
            print "Congratulations! You won!"
            return 0
        else:
            return play_game(words, guesses, wrongs)
    else:
        print "Sorry, that was a wrong guess."
        print
        wrongs.append(char)
        attempts = draw_hangman(len(wrongs))
        print "\n"
        if attempts == 7:
            print "Sorry, you failed to guess the word."
            print "The mystery word was - %s" % (''.join(s for s in words))
            sys.exit(0)
        else:
            return play_game(words, guesses, wrongs)

def draw_hangman(wrong):                                                            
    if wrong == 1:
        print " 0 "
    elif wrong == 2:
        print " 0 "
        print " | "
    elif wrong == 3:
        print " 0 "
        print "\| "
    elif wrong == 4:
        print " 0 "
        print "\|/"
    elif wrong == 5:
        print " 0 "
        print "\|/"
        print " | "
    elif wrong == 6:
        print " 0 "
        print "\|/"
        print " | "
        print "/  "
    elif wrong == 7:
        print " 0 "
        print "\|/"
        print " | "
        print '/ \\'
    return wrong

if __name__ == "__main__":
    ln = raw_input("How long word can you guess (number of alphabets) : ")
    ln = int(ln)
    l = []
    with open("/usr/share/dict/words", "r") as f:
        for i in f.readlines():
            i = i.rstrip()
            if i.isalpha():
                l.append(i)
    word = pick_random(l, ln)
    words, guesses = create_lists(word)
    wrongs = []
    print "Welcome to Hangman! You get seven chances to guess the mystery word."
    play_game(words, guesses, wrongs)
