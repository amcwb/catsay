# Catsay
Because cowsay wasn't good enough.

Here's a simple Python script to make cat say anything, also comes with faces and customisation!

## Installation
This has no external dependencies. You just need Python 3.6+.

## Usage
```
usage: catsay.py [-h] [--face FACE] text [text ...]

Cowsay, but better.

positional arguments:
  text                  What will the cat say?

optional arguments:
  -h, --help            show this help message and exit
  --face FACE, -f FACE  Pick face from: normal, sad, angry, hyper, smile, content or provide own
```

### Examples
With provided faces:
```bash
$ py catsay.py han shot first -f angry
{\___/}
( > .<)
/ > han shot first

$ py catsay.py well hello there -f content
{\___/}
( ^ -^)
/ > well hello there

$ # With default face
$ py catsay.py resting face               
{\____/}
( ● . ●)
/ > resting face
```

With custom faces (if containing gaps, parentheses must be used):
```
$ py catsay.py that's rad -f "∪ ◡∪"
{\___/}
( ∪ ◡∪)
/ > that's rad
```