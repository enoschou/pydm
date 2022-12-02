import os
from glob import glob

class Trees2:
    @staticmethod
    def count(path, dataset, sp):
        w = os.path.join(path, dataset, sp, '*.jpg')
        count = len(glob(w))
        
        return count

p = input('path: ')
d = input('dataset: ')
s = input('species: ')

print(f'{d} {s}: {Trees2.count(p, d, s)}')
