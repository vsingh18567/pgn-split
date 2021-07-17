# pgnsplit

`pgnsplit` is a simple command-line application that takes a single [pgn](https://en.wikipedia.org/wiki/Portable_Game_Notation) file (e.g. from a [Lichess Study](https://lichess.org/study/KjivNw7F)) and extracts all the variations in the pgn, putting each of them in their own individual pgn files in a folder `./pgn/`, which can then be stored in some sort of database (e.g. in SCID or ChessX).

This solves the problem in various chess software, where importing pgns only stores the mainline variation. 

This is presented as a lightweight and easy-to-use alternative to [David J. Barnes' pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/help.html), which is still more appropriate for the intricate manipulation of pgn files. 

## Requirements
* Python (>3.8)
* pip (which normally comes with Python)

## Installation
```bash
$ pip install pgnsplit
```

## Usage
```bash
$ pgnsplit <filepath>
```
`<filepath>` must be the path to a properly formatted pgn file. The individual pgn files will be stored in a local folder. 

## Improvements
Further improvements/functionality could be made as requested/needed.