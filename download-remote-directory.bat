:: Use SCP w/ SSH keys to download remote linux dir from Windows client
:: Local target directory must exist
scp -r -i "C:\Users\username\.ssh\id_rsa" user@host:"/home/pathto/remotedir" "E:\pathto\localdir"
