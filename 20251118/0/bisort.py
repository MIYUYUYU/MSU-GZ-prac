import sys
with open(sys.argv[1], 'br') as fin:
    bins = fin.read()
    with open(sys.argv[1], 'wb') as fout:
              print(bins)
              fout.write(bins[len(bins)//2:] + bins[:len(bins)//2])

