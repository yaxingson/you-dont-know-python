from ftplib import FTP

ftp = FTP('ftp.mozilla.org')

ftp.login('anonymous', 'guido@python.org')

ftp.close()


