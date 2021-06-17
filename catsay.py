import argparse

FACES = {
    "normal": "● . ●",
    "sad": ". _.",
    "angry": "> .<",
    "hyper": "≧ ◡≦",
    "smile": "◠ ‿◠",
    "content": "^ -^"
}

TEMPLATE = r"""
{{\{bar}/}}
( {face})
/ > {text}
""".strip()

def build_catsay(text: str, face: str):
    bar_length = len(face) - 1
    return TEMPLATE.format(text=text, face=face, bar='_'*bar_length)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cowsay, but better.')
    parser.add_argument('text', metavar='text', type=str, nargs='+',
                        help='What will the cat say?')
    parser.add_argument('--face', '-f', dest='face', default='normal',
                        help="Pick face from: {} or provide own".format(", ".join(FACES.keys())))

    args = parser.parse_args()

    # Does face exist?
    face = args.face
    if args.face in FACES:
        face = FACES[args.face]
    
    print(build_catsay(" ".join(args.text), face))