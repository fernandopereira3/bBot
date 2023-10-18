import subprocess
import os
import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level='NOTSET', format=FORMAT, datefmt='[%d/%b - %H:%M]',filename='/scripts/backup.log',filemode='a',encoding='utf-8')
log = logging.getLogger('rich')


class Limpeza():
        def limpezaSMB():
                log.warning('LIMPEZA SMB INICIADA')
                srcDir = ['/home/source/administrativo','/home/source/cimic','/home/source/comunicados','/home/source/cpd','/home/source/eat','/home/source/notes','/home/source/producao','/home/source/reintegracao','/home/source/seguranca']
                Del = ['*ini','~*.*','*.db','*.tmp','.*']
                i = 0
                for i in range(0,len(srcDir)):
                        for j in range(0, len(Del)):
                                limp_rotina = ['find', srcDir[i], '-name', Del[j], '-delete'] 
                                processo = subprocess.run(limp_rotina)
                logging.warning('LIMPEZA SMB COMPLETA!')

        def limpezaBIBLI():
                log.warning('LIMPEZA BILBIOTECAS INICIADA')
                #umount = os.system('umount -l 10.14.180.4:/home/smb')
                #mount = os.system("mount -t nfs 10.14.180.4:/home/bibliotecas /home/source")
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

                Del = ['*ini','~*.*','*.db','*.tmp','.*']
                i = 0
                for i in range(0,len(srcDir)):
                        for j in range(0, len(Del)):
                                limp_rotina = ['find', srcDir[i], '-name', Del[j], '-delete'] 
                                processo = subprocess.run(limp_rotina)

                umount = os.system('umount -l 10.14.180.4:/home/bibliotecas')
                logging.warning('LIMPEZA BIBLIOTECAS COMPLETA!')
        