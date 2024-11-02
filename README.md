# pyFlashCard

Flash Card program written in python (using [Raylib](https://www.raylib.com/)) for vocabs.

# Prerequisites

- [Python 3](https://www.python.org/downloads/)
- Install requirements: `pip install -r requirements.txt`

# Run

```
python flashcard.py
// OR
python flashcard.py <path-to-vocabs-list-file>
// OR
// with this you can iterate over the files in that directory
python flashcard.py <path-to-vocabs-lists-directory>
```

# Usage

- `Q` quit
- `Spacebar` Show the meaning of the word
- `J` next word
- `K` previous word
- `H` first word
- `L` last word
- `F` Toggle fullscreen
- `S or O` Sort the list
- `R or I` Randomize the list
- `N` Next file (if a directory was provided in args)
- `P` Previous file (if a directory was provided in args)

The following only words for YAML files:
- `M` Mark or Unmark a word (marked words are colored yellow)
- `X` Export marked words (words are exported to a file named `exported.yml` in the root directory (directory where `flashcard.y` is))

The vocabs list should be in the following format if it is a simple text file (see `lists/` directory for examples):

```
word - meaning
another word - meaning
```

Alternatively, you can use YAML files as well (see `lists/` directory for examples).
