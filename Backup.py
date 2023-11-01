import subprocess
import os
import logging
import boto3
import rich

# FORMAT = '%(asctime)s %(message)s'
# logging.basicConfig(level='NOTSET', format=FORMAT, datefmt='[%d/%b - %H:%M]', filename='/scripts/backup.log',filemode='a', encoding='utf-8')
# log = logging.getLogger('rich')


def bucket():
    client = boto3.client(
        ##########
        service_name='s3',
        
        region_name='us-west-2'
    )


class Bkp:

    def backupSMB():
        # source = os.system("mount -t nfs -o resvport,rw 10.0.0.140:/home/arquivos ~/mount/arquivos ")
        # log.warning('Backup inicializado!')
        with open('diretorios.txt', 'r') as source:
            source.readline()
        # srcDir = ['/home/source/administrativo','/home/source/cimic','/home/source/comunicados','/home/source/cpd','/home/source/eat','/home/source/notes','/home/source/producao','/home/source/reintegracao','/home/source/seguranca']
        # bkpDir = '/home/bkp/smb/'
        # source = "/Users/fernando/Documents"
        for (dirpath, dirnames, filenames) in os.walk(source):
            for f in filenames:
                f_path = os.path.join(dirpath, f)
                f_size = os.path.getsize(f_path)
                f_size_kb = f_size / 1024
        
        if f_size_kb >= 2.000:
            print(f_path)

        
        # umount = os.system("umount 10.0.0.140:/home/arquivos")
        source.close()
        
        # i = 0
        # for i in range(0, len(source)):
        #     bkp_rotina = ['rsync', '-hadzPu',b    