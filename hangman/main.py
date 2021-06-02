hangman_body = [
    """\
 _________
 ||/      |
 ||       
 ||
 ||
//\\\\
""",
    """\
 _________
 ||/      | H
 ||       O
 ||       
 ||
//\\\\
""",
    """\
 _________
 ||/      | HE
 ||       O
 ||       |
 ||       
//\\\\
""",
    """\
 _________
 ||/      | HEL
 ||       O
 ||      /|
 ||       
//\\\\
""",
    """\
 _________
 ||/      | HELP
 ||       O
 ||      /|\\
 ||       
//\\\\
""",
    """\
 _________
 ||/      | HELP MEEEEEEE!!!!!!
 ||       O
 ||      /|\\
 ||      /
//\\\\
""",
    """\
 _________
 ||/      | H....
 ||       O
 ||      /|\\
 ||      / \\
//\\\\
""",
]


def hangman(word):

    guessed_word = []
    old_word = list(word)
    tries = 1

    for i in word:
        guessed_word.append("_")

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
                return f"\nYou got it pogchamp! \nThe word is: {word}\n"
            else:
                tries += 1
                print(hangman_body[tries - 2])

    return "".join(guessed_word)


print(
    f"""
###------------------###
### HARDCORE HANGMAN ###
###------------------###
{hangman_body[0]}"""
)
word = input("What is the word? ")

print(hangman(word))
