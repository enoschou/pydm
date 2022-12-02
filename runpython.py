import os
from glob import glob

class Trees2:
    @staticmethod
    def count(path, dataset, sp):
        w = os.path.join(path, dataset, sp, '*.jpg')
        count = len(glob(w))
        
        return count
    
print(f"tree DR: {Trees2.count('trees', 'train', 'DR')}")
