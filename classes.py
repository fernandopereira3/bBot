import logging
import subprocess
import os

logging.basicConfig(filename='/scripts/backup.log',
        format='%(message)s %(asctime)s',
        filemode='a',
        encoding='utf-8')

class Backup():
        def backup():
                logging.warning('Iniciando backup')
                #mount = os.system("mount -t nfs 10.14.180.4:/home/smb /home/source")
                srcDir = ['/home/source/administrativo','/home/source/cimic','/home/source/comunicados','/home/source/cpd','/home/source/eat','/home/source/notes','/home/source/producao','/home/source/reintegracao','/home/source/seguranca']
                bkpDir = '/home/bkp/smb/'
                i = 0
                for i in range(0,len(srcDir)):
                        bkp_rotina = ['rsync','-hadzPu', srcDir[i], bkpDir] 
                        processo = subprocess.run(bkp_rotina)   
                os.system('chmod -R 777 /home/bkp/')
                logging.warning('Backup completo!')

       

class Limpeza():
        def limpeza():
                logging.info('Iniciando limpeza')
                mount = os.system("mount -t nfs 10.14.180.4:/home/smb /home/source")
                bkpDir = ['/home/bkp/smb/administrativo','/home/bkp/smb/cimic','/home/bkp/smb/comunicados','/home/bkp/smb/cpd','/home/bkp/smb/eat','/home/bkp/smb/notes','/home/bkp/smb/producao','/home/bkp/smb/reintegracao','/home/bkp/smb/seguranca']
                Del = ['*ini', "~*.*", "*.db", "*.tmp"]
                i = 0
                for i in range(0,len(bkpDir)):
                        for j in range(0, len(Del)):
                                limp_rotina = ['find', bkpDir[i], '-name', Del[j], '-delete'] 
                                processo = subprocess.run(limp_rotina)
                #umount = os.system('umount -l 10.14.180.4:/home/smb')   
                os.system('chmod -R 777 /home/bkp/')
                logging.info('Limpeza completa!')
        