from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

# Initializing a GoogleAuth Object
gauth = GoogleAuth()

# client_secrets.json file is verified
# and it automatically handles authentication
gauth.LocalWebserverAuth()

# GoogleDrive Instance is created using
# authenticated GoogleAuth instance
drive = GoogleDrive(gauth)

# Initialize GoogleDriveFile instance with file id
file_obj = drive.CreateFile({'id': '1yqXiIUuZtpc2GPUTjUcdnz6__8nc3rzMKWPR2MM0t3s'})
file_obj.GetContentFile('Formulário sem título (respostas).xlsx',
                        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

dataframe = pd.read_excel('Formulário sem título (respostas).xlsx')
print(dataframe)