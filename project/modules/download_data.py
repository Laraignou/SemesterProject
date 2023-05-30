import time
from tqdm import tqdm
import urllib.request
from urllib.request import urlopen

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

"""WORKS WITH VS.CODE AND NOT CMD (CAUSE DIFFERENT PATHS)"""

# download_url(url="https://www.dropbox.com/s/s5yarta1lk6afz3/Dataset_Collection.zip?dl=1", save_as ="project/resources/data/Dataset.zip")


"""WORKS WITH CMD ATM AND NOT VS.CODE (CAUSE DIFFERENT PATHS)"""
# download_url(url="https://www.dropbox.com/s/s5yarta1lk6afz3/Dataset_Collection.zip?dl=1", save_as ="resources/data/Dataset.zip")