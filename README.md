# randSeqGen
Random sequence generator for testing LMs

### Usage
```bash
./get_sec.py --help
usage: get_sec.py [-h] -n N -smin SMIN -smax SMAX -m M -o O [-r R]

Generates a document with N lines of length from minlen to maxlen containing M
uniq characters.

optional arguments:
  -h, --help            show this help message and exit
  -n N, --num-lines N
  -smin SMIN, --sentence-length-min SMIN
  -smax SMAX, --sentence-length-max SMAX
  -m M, --uniq-words M
  -o O, --output-file O
  -r R, --random-seed R

get_sec.py -n 5 -smin 3 -smax 20 -m 4 -o test.out
```

Will create a file `-o test.out` of length `n=5` lines, with a minimum sentence length of `smin=3`, maximum sentence length of `smax=20` and `m=4` possible distinct vocabulary items.

The created file will look like this:

```
A C A D D D D B A
A D D A D C B A C A A A A D B D A B D D
C B B D C A D A B C A C
B C C D D A D B D D B C C A D A B D
D A D A C D B B B A B B D C C D
```


#### Single context trigrams

```bash
mkdir data
python generate_trigrams.py -slen 3 -m 10 -o data/single_context_freq
```
