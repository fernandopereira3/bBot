import os
from pathlib import Path
import logging
logging.basicConfig(filename='/scripts/backup.log',
        format='%(message)s %(asctime)s',
        filemode='a',
        encoding='utf-8',)


mount = os.system("mount -t nfs 10.14.180.4:/home/ssd /home/source2")
Dir = ['/administrativo','/cimic','/comunicados','/cpd','/eat','/notes','/producao','/reintegracao','/seguranca','/musicas']
src = Path('/home/source')
controle = os.system('touch -a /home/source2/.controle')
print(os.path.getmtime(controle))
print(Dir)
umount = os.system('umount -l 10.14.180.4:/home/ssd')
logging.info('diretorios.py')
