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
 ||/      |
 ||       O
 ||       
 ||
//\\\\
""",
    """\
 _________
 ||/      |
 ||       O
 ||       |
 ||       
//\\\\
""",
    """\
 _________
 ||/      |
 ||       O
 ||      /|
 ||       
//\\\\
""",
    """\
 _________
 ||/      |
 ||       O
 ||      /|\\
 ||       
//\\\\
""",
    """\
 _________
 ||/      |
 ||       O
 ||      /|\\
 ||      /
//\\\\
""",
    """\
 _________
 ||/      |
 ||       O
 ||      /|\\
 ||       /\\
//\\\\
""",
]


def body(num):
    return hangman_body[num]