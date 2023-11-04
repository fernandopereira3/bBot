import os
import boto3

class Bkp:

    def backupSMB():
         with open('diretorios.txt', 'r') as source:
            for leitor in source.readlines():
                directory_path = leitor.strip()
                for (dirpath, dirnames, filenames) in os.walk(directory_path):
                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)
                        file_size = os.path.getsize(file_path) / (1024)  # Tamanho em MB
                        if file_size <= 0  and (filename.endswith('.jpg') or filename.endswith('.png')):
                            # s3_client.upload_file(file_path, 'bbot-s3', filename)
                            print(f'{filename} ({file_size:.2f} MB)')


if __name__ == "__main__":
    s3_client = boto3.client(
        's3',
       
        region_name='us-west-2'
    )

    backup = Bkp()
    backup.backupSMB() 