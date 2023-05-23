import zipfile

with zipfile.ZipFile('Dataset_Collection.zip', 'r') as zip_ref:
        zip_ref.extractall('./')