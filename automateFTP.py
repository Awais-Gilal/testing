from ftplib import FTP
import os

host_name = "192.168.10.2"                  #input("Enter host name of FTP: ") 192.168.10.4
port = 2221
user_name = "android"                       #input("Enter user name of FTP: ") #android
password = "android"                        #input("Enter password of FTP: ") # android
remote_dir =  "snaptube/download/"          #/snaptube/download/"        #input("Enter remote directory of FTP: ") 
local_dir =  "D:\\"                         #input("Enter local directory of PC: ")
idm_path = 'C:\\Program Files (x86)\\Internet Download Manager'
idm_exe = "IDMan.exe"
ftp_basic_link = f"ftp://{host_name}:{str(port)}/"

os.chdir(idm_path)

ftp = FTP()
ftp.connect(host_name, port=port)
ftp.login(user_name, password)
ftp.cwd(remote_dir)
ftp.set_pasv(True)

files = ftp.nlst()

for file in files:
    if file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".mp3"):
        remote_file_path = remote_dir + file
        local_file_path = local_dir + file
        conform = input(f"Do you want to add this {file} in queue:")

        if len(conform) ==0:
            command_to_idm = idm_exe + ' /d "' + ftp_basic_link + remote_file_path + '" /a'
            os.system(command_to_idm)
            # time.sleep(5)
            print("\n")
        else:
            continue
    else:
        continue
ftp.quit()
