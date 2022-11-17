import Backup as b
import logging
from rich import print
from rocketry import Rocketry
from rocketry.conds import (after_fail, after_success, hourly, daily)
from rocketry.log import MinimalRecord
from redbird.logging import RepoHandler
from redbird.repos import CSVFileRepo



FORMAT = '%(asctime)s %(message)s'
#logging.basicConfig(level='DEBUG', format=FORMAT, datefmt='[%H:%M:%S]')
logger = logging.getLogger('rocketry.task')
repo = CSVFileRepo(filename='/scripts/backup.csv', model=MinimalRecord)
handler = RepoHandler(repo=repo)
logger.addHandler(handler)

app = Rocketry(config={'task_execution': 'process'})

@app.task(hourly.between('06:00','18:00')) ### TAREFA DAS 6 AS 18 BACKUP DO SMB DO SERVIDOR .4
def smb():
   print('[red on green reverse blink]BACKUP SMB INICIADO[/r]')
   bkp = b.Bkp.backupSMB()

@app.task(after_fail(smb)) ### CASO ERRO DO BACKUP
def erro_smb():
   print('[blink reverse red]ERRO NO BACKUP DO SMB[/]')
   logger.warning('Erro CRITICO ao realizar o BACKUP do SMB, por favor verifique!')

@app.task(daily.after('23:00')) ### APOS AS 23 BACKUP DAS BIBLIOTECAS DO SERVIDOR .4
def biblio():
   print('[red on green reverse blink]BACKUP DAS BIBLIOTECAS INICIADO[/r]')
   bibliotecas = b.Bkp.backupBIBLI()

@app.task(after_fail(biblio))
def erro_bibliotecas():
   print('[blink reverse red]ERRO NO BACKUP DAS BIBLIOTECAS[/]')
   logger.warning('Erro CRITICO ao realizar o BACKUP das BIBLIOTECAS, por favor verifique!')
   
app.run()