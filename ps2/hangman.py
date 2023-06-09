# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
        


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    gussed_word = ""
    for letter in secret_word:
        if letter not in letters_guessed:
           gussed_word += "_ "
        else:
            gussed_word += letter
    return gussed_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters
    



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # letters_guessed  = []
    # print("Welcome to the game Hangman! ")
    # lenght = len(secret_word)
    # print(f"I am thinking of a word that is {lenght} letters long.")
    
    # print("-------------")

    

    # valabile_guesses = 6
    # warnings = 3
    # while valabile_guesses > 0:
    #   inp_num = False
      
    #   print(f"You have {valabile_guesses} guesses left.")
      
    #   available_letters = get_available_letters(letters_guessed)
    #   print(f"Available letters: {available_letters} ")

    #   guessed_letter = input("please enter a letter: ")


    #   if guessed_letter.isalpha():
    #     guessed_letter = guessed_letter.lower()
    #   else:
    #       inp_num = True

    #   good_guess = get_guessed_word(secret_word, letters_guessed)

    #   if warnings > 0:
    #     if inp_num == True:
    #         warnings -=1
    #         good_guess = get_guessed_word(secret_word, letters_guessed)
    #         print(f"Oops! That is not a valid letter. You now have {warnings} warnings left : {good_guess}")
          
    #     elif guessed_letter in letters_guessed:
    #         warnings -=1
    #         print(f"Oops! You've already guessed that letter. You now have {warnings} warnings left : {good_guess}")
            
    #     elif guessed_letter in secret_word:
    #       letters_guessed.append(guessed_letter)
    #       good_guess = get_guessed_word(secret_word, letters_guessed)
    #       print(f"Good guess: {good_guess}")
    #     else: 
    #         valabile_guesses -= 1 
    #         print(f"Oops! That letter is not in my word: {good_guess}")
    #   else:
    #     if inp_num == True:
    #         valabile_guesses -=1
    #         good_guess = get_guessed_word(secret_word, letters_guessed)
    #         print(f"Oops! That is not a valid letter. You now have no warnings left so you lose one guess: {good_guess}")
          
    #     elif guessed_letter in letters_guessed:
    #         valabile_guesses -=1
    #         print(f"Oops! You've already guessed that letter. You now have no warnings left so you lose one guess: {good_guess}")
    #     elif guessed_letter in secret_word:
    #       letters_guessed.append(guessed_letter)
    #       good_guess = get_guessed_word(secret_word, letters_guessed)
    #       print(f"Good guess: {good_guess}")
    #     else: 
    #         valabile_guesses -= 1 
    #         print(f"Oops! That letter is not in my word: {good_guess}")          
     


    #   print("-------------")
    #   guessed = is_word_guessed(secret_word, letters_guessed)
    #   total_score = valabile_guesses * len(set(secret_word))

    #   if guessed == True:
    #       print("Congratulations, you won!")
    #       print(f"Your total score for this game is: {total_score} ")
    #       break
    #   elif valabile_guesses == 0:
    #       print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
  
          


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    my_word_len = len(my_word)
    revealed_letters = set([letter for letter in my_word if letter != "_"])

    if my_word_len == len(other_word):
        for i, letter in enumerate(my_word):
            other_letter = other_word[i]
            if letter != "_" and letter != other_letter:
                return False
            if letter == "_" and other_letter in revealed_letters:
                return False
        return True
    else:
        return False
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    matches = []
    for word in wordlist:
        if len(my_word) != len(word):
            continue
        is_match = True
        for i in range(len(my_word)):
            if my_word[i] != "_" and my_word[i] != word[i]:
              is_match = False
              break 
        if is_match:
            matches.append(word)
    if len(matches) == 0:
        print("No matches found")
    else:
        print(matches)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed  = []
    print("Welcome to the game Hangman! ")
    lenght = len(secret_word)
    print(f"I am thinking of a word that is {lenght} letters long.")
    
    print("-------------")

    

    valabile_guesses = 6
    warnings = 3
    while valabile_guesses > 0:
      inp_num = False
      
      print(f"You have {valabile_guesses} guesses left.")
      
      available_letters = get_available_letters(letters_guessed)
      print(f"Available letters: {available_letters} ")

      guessed_letter = input("please enter a letter: ")

      if guessed_letter.isalpha():
        guessed_letter = guessed_letter.lower()
      else:
          inp_num = True

      good_guess = get_guessed_word(secret_word, letters_guessed)

      if guessed_letter == "*":
          if match_with_gaps(good_guess, secret_word):
              show_possible_matches(good_guess)

      if guessed_letter != "*":
        if warnings > 0:
          if inp_num == True:
              warnings -=1
              good_guess = get_guessed_word(secret_word, letters_guessed)
              print(f"Oops! That is not a valid letter. You now have {warnings} warnings left : {good_guess}")
            
          elif guessed_letter in letters_guessed:
              warnings -=1
              print(f"Oops! You've already guessed that letter. You now have {warnings} warnings left : {good_guess}")
              
          elif guessed_letter in secret_word:
            letters_guessed.append(guessed_letter)
            good_guess = get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess: {good_guess}")
          else: 
              valabile_guesses -= 1 
              print(f"Oops! That letter is not in my word: {good_guess}")
        else:
          if inp_num == True:
              valabile_guesses -=1
              good_guess = get_guessed_word(secret_word, letters_guessed)
              print(f"Oops! That is not a valid letter. You now have no warnings left so you lose one guess: {good_guess}")
            
          elif guessed_letter in letters_guessed:
              valabile_guesses -=1
              print(f"Oops! You've already guessed that letter. You now have no warnings left so you lose one guess: {good_guess}")
          elif guessed_letter in secret_word:
            letters_guessed.append(guessed_letter)
            good_guess = get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess: {good_guess}")
          else: 
              valabile_guesses -= 1 
              print(f"Oops! That letter is not in my word: {good_guess}")          
      


        print("-------------")
        guessed = is_word_guessed(secret_word, letters_guessed)
        total_score = valabile_guesses * len(set(secret_word))

        if guessed == True:
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score} ")
            break
        elif valabile_guesses == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
