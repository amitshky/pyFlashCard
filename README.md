# pyFlashCard
Flash Card program written in python (using [Raylib](https://www.raylib.com/)) for vocabs.

# Prerequisites
- [Python 3](https://www.python.org/downloads/)
- [Raylib (Python binding for raylib)](https://pypi.org/project/raylib/) (`pip install setuptools raylib`)

# Run
```
python flashcard.py
// OR
python flashcard.py <path-to-vocabs-list-file>
// OR
python flashcard.py <path-to-vocabs-lists-directory> // you can iterate over the files in that directory
```

# Usage
- `Q` to quit
- `Spacebar` Show the meaning of the word
- `J` next word
- `K` previous word
- `H` first word
- `L` last word
- `S` Sort the list
- `R` Randomize the list
- `N` Next file (if a directory was provided in args)
- `P` Previous file (if a directory was provided in args)

The vocabs list should be in the following format (see `lists/` directory for examples):
```
word - meaning
```
