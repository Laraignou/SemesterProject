# import tempfile
# import office

# from msal import token_cache
# from office365 import graph_client
# # from office365.onedrive.driveitems.driveItem import DriveItem

# client = graph_client(token_cache)
# # address folder by path 
# folder_item = client.me.drive.root.get_by_path("archive").get().execute_query()

# with tempfile.TemporaryDirectory() as local_path:
#     items = folder_item.children.get().execute_query()
#     for drive_item in items:  # type: DriveItem
#         if drive_item.is_file:
#             with open(os.path.join(local_path, drive_item.name), 'wb') as local_file:
#                 drive_item.download(local_file).execute_query()  # download file content
#             print("File '{0}' has been downloaded into {1}".format(drive_item.name, local_file.name))



# #Import the requests library
# import requests

# URL = "https://1drv.ms/t/s!Ai8Ld7Hb96N9oGthYzrNH5pcdMi5?e=1gQCVb"

# #  Download the data behind the URL
# response = requests.get(URL)

# #  Open the response generated into a new file in your local called image.jpg
# # open("test.txt", "wb").write(response.content)

# from onedrivedownloader import download
# import requests

# ln = "https://1drv.ms/t/s!Ai8Ld7Hb96N9oGthYzrNH5pcdMi5?e=1gQCVb"



# from onedrivedownloader import download


# download("https://1drv.ms/f/s!Ai8Ld7Hb96N9oB9B6OR1mJGANYOM?e=aeybEf", "The_Movies_Dataset.zip", unzip=False, force_download=True, force_unzip=False, clean=False)



# import pathlib
# import pandas as pd
# import dropbox
# from dropbox.exceptions import AuthError

# dbx = dropbox.Dropbox("<ACCESS_TOKEN>")

# with open("Prime_Numbers.txt", "wb") as f:
#     metadata, res = dbx.files_download(path="/Homework/math/Prime_Numbers.txt")
#     f.write(res.content)

#     # https://www.dropbox.com/sh/4ijzgjutq9bdukv/AAD-L8E3g4bTyWy2lDIfT3l4a?dl=0

# def run(runfile):
#   with open(runfile,"r") as rnf:
#     exec((rnf.read()))
# # run('Project/main.py')


# with open("Project/main.py") as f:
#     exec(f.read())