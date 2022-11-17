import Backup as b
import logging
import datetime
import rich
from rich import print

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level='NOTSET', format=FORMAT, datefmt='[%d/%b - %H:%M]',filename='/scripts/backup.log',filemode='a',encoding='utf-8')
log = logging.getLogger('rich')

now = datetime.datetime.now()
hora = now.strftime('%H')

if hora != '23': #### BACKUP DO SMB, REALIZADO A CADA HORA
    try:
        print('[bright_green on black reverse]BACKUP DE SMB INICIADO[/]')
        bkp = b.Bkp.backupSMB()
    except:
        print('[bright_red on black reverse]ERRO CRITICO!!![/]')
        log.warning('ERRO CRITICO AO REALIZAR O BACKUP DO SMB, POR FAVOR VERIFIQUE!')
          
elif hora == '23': # BACKUP DAS BIBLIOTECAS, REALIZADO DIARIAMENTE AS 23 ##
    try:
        print('[bright_green on black reverse]BIBLIOTECAS INICIADO[/]')
        bibliotecas = b.Bkp.backupBIBLI()
    except:
        print('[bright_red on black reverse]ERRO CRITICO!!![/]')
        log.warning('ERRO CRITICO AO REALIZAR O BACKUP DAS BIBLIOTECAS, POR FAVOR VERIFIQUE!')
