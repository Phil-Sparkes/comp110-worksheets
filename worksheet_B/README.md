```
while IncorrectGuesses < 4                                      # loops until the user has 4 inccorect guesses

    print "Pick a word"
    Guess = word picked                                         #The player guesses a word

    Likeness = 0                                                

    for X = range 1 to SecretWordLength                         # loops depending on the length of the secret word
        if Guess[X] = SecretWord[X]                             # Checks each letter of the guess against the secret word to see if they match
            Likeness = Likeness + 1                             # if the letters match then the likeness is increased by one
        end if
    end for
    
    print "likeness = " + Likeness + "/" + SecretWordLength     # displays the likeness score so the player knows how close the guess was to the answer

    if Likeness = SecretWordLength                              # if the Likeness matches the SecretWordLength then the player has guessed correctly
        print "You win"                                         # displays the win message and exits
        exit
    else
        IncorrectGuesses = IncorrectGuessses + 1                # user did not guess correctly - adds one to the incorrect counter
        print "Incorrect guesses " + IncorrectGuesses + "/4"    # shows the user how many incorrect guesses they have
    end if

end while

print "game over"                                               # if the user has 4 incorrect guesses then "game over" is displayed
```

![flowchart](Flowchart.png)
