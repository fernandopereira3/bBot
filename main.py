import logging
import classes
import os
import subprocess
from datetime import datetime
import time

mount = os.system("mount -t nfs 10.14.180.4:/home/smb /home/source")
path = r'/home/source/.controle'
now = datetime.now()
now_time = now.strftime('%H:%M:%S')

time_c = os.path.getctime(path)
c_time = time.ctime(time_c)
verificado = time.strptime(c_time)
DataArquivo = time.strftime('%H:%M:%S', verificado)
comparativo = now_time > DataArquivo

if comparativo == True:
    bkp = classes.Backup.backup()
   
else:
    logging.warning('Opa! alguma coisa de errado na hora de fazer o backup')

controle = ['touch','/home/source/.controle']
subprocess.run(controle) 
umount = os.system('umount -l 10.14.180.4:/home/smb')