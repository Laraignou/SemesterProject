import zipfile

def Unzip_Dataset():
        
        with zipfile.ZipFile('Resources/Data/Dataset.zip', 'r') as zip_ref:
                zip_ref.extractall('Resources/Data/')

        # with zipfile.ZipFile('project/Resources/Data/Dataset.zip', 'r') as zip_ref:
        #         zip_ref.extractall('project/Resources/Data/')

