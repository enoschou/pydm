import os
from glob import glob

print(f'runpython6.py\'s name is {__name__}')

class Trees2:
    @staticmethod
    def count(path, dataset, sp):
        w = os.path.join(path, dataset, sp, '*.jpg')
        count = len(glob(w))
        
        return count

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('species', type=str)
    parser.add_argument('-p', '--path', type=str, default='trees', help='root path of samples')
    parser.add_argument('-d', '--dataset', default='train', choices=['train', 'test'])

    args = parser.parse_args()

    print(f'{args.dataset} {args.species}:'
          f'{Trees2.count(args.path, args.dataset, args.species)}')
    