import os
import boto3

class Bkp:

    def backupSMB(self):
         with open('diretorios.txt', 'r') as source:
            for leitor in source.readlines():
                directory_path = leitor.strip()

                for (dirpath, dirnames, filenames) in os.walk(directory_path):
                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)
                        file_size = os.path.getsize(file_path) / (1024 * 1024)  # Tamanho em MB
                        if file_size <= 1  and (filename.endswith('.pdf') or filename.endswith('.txt')):
                            s3_client.upload_file(file_path, 'bbot-s3', filename)
                            print(f'Arquivo {filename} ({file_size:.2f} MB) enviado para o Amazon S3.')


if __name__ == "__main__":
    s3_client = boto3.client(
        's3',
        
        region_name='us-west-2'
    )

    backup = Bkp()
    backup.backupSMB() 