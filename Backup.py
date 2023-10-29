import subprocess
import os
import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level='NOTSET', format=FORMAT, datefmt='[%d/%b - %H:%M]',filename='/scripts/backup.log',filemode='a',encoding='utf-8')
log = logging.getLogger('rich')

class Bkp():
        def backupSMB():
                # mount = os.system("mount -t nfs 10.14.180.4:/home/smb /home/source")
                log.warning('Backup inicializado!')
                with open('diretorios.txt', 'r') as srDir:
                        srDir.readline()
                # srcDir = ['/home/source/administrativo','/home/source/cimic','/home/source/comunicados','/home/source/cpd','/home/source/eat','/home/source/notes','/home/source/producao','/home/source/reintegracao','/home/source/seguranca']
                bkpDir = '/home/bkp/smb/'
                i = 0
                for i in range(0,len(srDir)):
                        bkp_rotina = ['rsync','-hadzPu', srDir[i], bkpDir] 
                        processo = subprocess.run(bkp_rotina) 
                srDir.close()  
        
                os.system('chmod -R 777 /home/bkp/')
                umount = os.system('umount -l 10.14.180.4:/home/smb')
                log.warning('Backup SMB Completo')

        def backupBIBLI():
                mount = os.system("mount -t nfs 10.14.180.4:/home/bibliotecas /home/source")
                log.warning('Backup BIBLIOTECAS inicializado!')
                #/adm /aevp /chefia /cimic /cpd /cras /financas /inclusao /infra /judiciaria /peculio /pessoal /portaria /producao /rol /saude /seguranca /supervisao 
                with open('diretorios.txt', 'r') as srDir:
                        srDir.readline()

                bkpDir = '/home/bkp/bibliotecas/'
                i = 0
                for i in range(0,len(srDir)):
                        bkp_rotina = ['rsync','-hadzPu', srDir[i], bkpDir] 
                        processo = subprocess.run(bkp_rotina) 

                srDir.close()
                os.system('chmod -R 777 /home/bkp/bibliotecas')
                umount = os.system('umount -l 10.14.180.4:/home/bibliotecas')
                log.warning('Backup BIBLIOTECAS Completo!')