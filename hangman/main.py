from getpass import getpass


hangman_body = [
    """\
    _________
    ||/      |
    ||       
    ||
    ||
  _//\\\\_______
    """,
    """\
    _________
    ||/      | H
    ||       O
    ||       
    ||
  _//\\\\_______
    """,
    """\
    _________
    ||/      | HE
    ||       O
    ||       |
    ||       
  _//\\\\_______
    """,
    """\
    _________
    ||/      | HEL
    ||       O
    ||      /|
    ||       
  _//\\\\_______
    """,
    """\
    _________
    ||/      | HELP
    ||       O
    ||      /|\\
    ||       
  _//\\\\_______
    """,
    """\
    _________
    ||/      | HELP MEEEEEEE!!!!!!
    ||       O
    ||      /|\\
    ||      /
  _//\\\\_______
    """,
    """\
    _________
    ||/      | H....
    ||       O
    ||      /|\\
    ||      / \\
  _//\\\\_______
    """,
    """\
         O    *Man was forever scarred from this experience*
        /|\\
        / \\
    """,
]


def hangman(word):
    guessed_word = [i.replace(i, "_") for i in word]
    old_word = list(word)
    tries = 1

    while tries <= 7:
        if "".join(guessed_word) == word:
            return f"\nYou got it pogchamp! \nThe word is: {word}\n"

        else:
            guess = input(f"Try {tries}: ")

            if guess in old_word and guess != "":
                word_idx = old_word.index(guess)
                old_word[word_idx] = "_"
                guessed_word[word_idx] = guess
                print("".join(guessed_word))

            elif guess == word:
                return f"\nYou got it dude! \nThe word is: {word}\n\n{hangman_body[7]}"

            else:
                tries += 1
                print(hangman_body[tries - 2])

    return f"The man has perished, you are to blame.\nThe word was {word}, bet you feel pretty bad now...\n"


print(
    f"""
    ###------------------###
    ### HARDCORE HANGMAN ###
    ###------------------###
    {hangman_body[0]}"""
)

word = getpass("What is the word? ")

print(hangman(word))
