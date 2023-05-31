import time
from tqdm import tqdm
import urllib.request
from urllib.request import urlopen
import os

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, save_as):
    print('Downloading dataset...')
    time.sleep(1)

    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, save_as, reporthook=t.update_to)
    os.system('cls')
    input('Press ENTER to Show RAW DATA..')