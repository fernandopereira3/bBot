import subprocess
import os
import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level='NOTSET', format=FORMAT, datefmt='[%d/%b - %H:%M]',filename='/scripts/backup.log',filemode='a',encoding='utf-8')
log = logging.getLogger('rich')

class Bkp():
        def backupSMB():
                mount = os.system("mount -t nfs 10.14.180.4:/home/smb /home/source")
                log.warning('Backup SMB inicializado!')
                srcDir = ['/home/source/administrativo','/home/source/cimic','/home/source/comunicados','/home/source/cpd','/home/source/eat','/home/source/notes','/home/source/producao','/home/source/reintegracao','/home/source/seguranca']
                bkpDir = '/home/bkp/smb/'
                i = 0
                for i in range(0,len(srcDir)):
                        bkp_rotina = ['rsync','-hadzPu', srcDir[i], bkpDir] 
                        processo = subprocess.run(bkp_rotina)   
                os.system('chmod -R 777 /home/bkp/')
                umount = os.system('umount -l 10.14.180.4:/home/smb')
                log.warning('Backup SMB Completo')

        def backupBIBLI():
                mount = os.system("mount -t nfs 10.14.180.4:/home/bibliotecas /home/source")
                log.warning('Backup BIBLIOTECAS inicializado!')
                #/adm /aevp /chefia /cimic /cpd /cras /financas /inclusao /infra /judiciaria /peculio /pessoal /portaria /producao /rol /saude /seguranca /supervisao 
                srcDir = ['/home/source/adm',
                          '/home/source/aevp',
                          '/home/source/chefia',
                          '/home/source/cimic',
                          '/home/source/cpd',
                          '/home/source/cras',
                          '/home/source/financas',
                          '/home/source/inclusao',
                          '/home/source/infra',
                          '/home/source/judiciaria',
                          '/home/source/peculio',
                          '/home/source/pessoal',
                          '/home/source/portaria',
                          '/home/source/producao',
                          '/home/source/rol',
                          '/home/source/saude',
                          '/home/source/seguranca',
                          '/home/source/supervisao']

                bkpDir = '/home/bkp/bibliotecas/'
                i = 0
                for i in range(0,len(srcDir)):
                        bkp_rotina = ['rsync','-hadzPu', srcDir[i], bkpDir] 
                        processo = subprocess.run(bkp_rotina) 

                os.system('chmod -R 777 /home/bkp/bibliotecas')
                umount = os.system('umount -l 10.14.180.4:/home/bibliotecas')
                log.warning('Backup BIBLIOTECAS Completo!')