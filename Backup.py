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
        aws_access_key_id='AKIAXI2SKEAFOQQB6NK3',
        aws_secret_access_key='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',
        region_name='us-west-2'
    )


class Bkp:

    def backupSMB():
        mount = os.system("mount -t nfs -o resvport,rw 10.0.0.140:/home/arquivos ~/mount/arquivos")
        # log.warning('Backup inicializado!')
        source = open('diretorios.txt', 'r')
        leitor = source.readline()
        # srcDir = ['/home/source/administrativo','/home/source/cimic','/home/source/comunicados','/home/source/cpd','/home/source/eat','/home/source/notes','/home/source/producao','/home/source/reintegracao','/home/source/seguranca']
        # bkpDir = '/home/bkp/smb/'
        # source = "/Users/fernando/Documents"
        for (dirpath, dirnames, filenames) in os.walk(str(leitor)):
            for f in filenames:
                f_path = os.path.join(dirpath, f)
                f_size = os.path.getsize(f_path)
                f_size_kb = f_size / 1024
                # return print("PATH: " + f_path + "TAMANHO: " + f_size_kb)
                
                # return print(f_size_kb)
        
        source.close()
        umount = os.system("umount 10.0.0.140:/home/arquivos")
        



        # if f_size_kb >= 2.000:
        #     print(f_path)
     
        # i = 0
        # for i in range(0, len(source)):
        #     bkp_rotina = ['rsync', '-hadzPu',b    