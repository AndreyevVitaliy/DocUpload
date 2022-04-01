from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import telebot
import pprint as pp



import os

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()


def connect_telepot():
    bot = telepot('5178608519:AAGqDLaQzbTEuyaGC5R9-LoZ45Y_8DxQ3Qg')
    # bot.getMe()
    response = bot.getUpdates()
    pp.pprint(response)


def upload_file(dir_path=''):
    try:
        drive = GoogleDrive(gauth)
        for file_name in os.listdir(dir_path):
            file1 = drive.CreateFile({'title': f'{file_name}'})
            file1.SetContentFile(os.path.join(dir_path, file_name))
            file1.Upload()
    except Exception as _ex:
       return 'error'




    # # создание файла, сюда нужно прикрутить выбор каталога
    # file1 = drive.CreateFile({'title': '111.txt'})
    # file1.SetContentFile(os.path.join('/Users/vitaliy/Desktop/DocUpload/', 'Files/111.txt'))
    # file1.Upload() # Files.insert()
    #
    # file1['title'] = 'HelloWorld.txt'  # Change title of the file
    # file1.Upload() # Files.patch()

# content = file1.GetContentString()  # 'Hello'
# file1.SetContentString(content+' World!')  # 'Hello World!'
# file1.Upload() # Files.update()

# file2 = drive.CreateFile()
# file2.SetContentFile('hello.png')
# file2.Upload()
# print('Created file %s with mimeType %s' % (file2['title'],
# file2['mimeType']))
# Created file hello.png with mimeType image/png

# file3 = drive.CreateFile({'id': file2['id']})
# print('Downloading file %s from Google Drive' % file3['title']) # 'hello.png'
# file3.GetContentFile('world.png')  # Save Drive file as a local file
#
# # or download Google Docs files in an export format provided.
# # downloading a docs document as an html file:
# docsfile.GetContentFile('test.html', mimetype='text/html')

def main():
    # print(upload_file('/Users/vitaliy/Desktop/DocUpload/Files'))
    connect_telepot()

if __name__ == '__main__':
    main()
