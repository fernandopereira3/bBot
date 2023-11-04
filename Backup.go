//   SOMENTE PEDI PARA O CHATGPT 
//   TRANSCREVER DE PYTHON PARA GOLANG
//	 PARA ESTUDAR O CODIGO NO FUTURO.
package main

import (
    "bufio"
    "fmt"
    "io/ioutil"
    "os"
    "path/filepath"
    "strings"
    
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
)

func main() {
    file, err := os.Open("diretorios.txt")
    if err != nil {
        fmt.Println("Erro ao abrir o arquivo:", err)
        return
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        directoryPath := scanner.Text()
        files, err := ioutil.ReadDir(directoryPath)
        if err != nil {
            fmt.Println("Erro ao ler diretório:", err)
            continue
        }

        sess, err := session.NewSession(&aws.Config{
            Region: aws.String("us-west-2"),
            Credentials: credentials.NewStaticCredentials("", "", ""),
        })
        if err != nil {
            fmt.Println("Erro ao criar a sessão AWS:", err)
            return
        }

        svc := s3.New(sess)

        for _, file := range files {
            if file.Size() > 1024*1024 && (strings.HasSuffix(file.Name(), ".pdf") || strings.HasSuffix(file.Name(), ".txt")) {
                filePath := filepath.Join(directoryPath, file.Name())
                fileContent, err := ioutil.ReadFile(filePath)
                if err != nil {
                    fmt.Println("Erro ao ler arquivo:", err)
                    continue
                }

                _, err = svc.PutObject(&s3.PutObjectInput{
                    Bucket: aws.String("nome-do-seu-bucket"),
                    Key:    aws.String(file.Name()),
                    Body:   bytes.NewReader(fileContent),
                })
                if err != nil {
                    fmt.Println("Erro ao enviar arquivo para o S3:", err)
                } else {
                    fmt.Printf("Arquivo %s (%d bytes) enviado para o Amazon S3.\n", file.Name(), file.Size())
                }
            }
        }
    }

    if err := scanner.Err(); err != nil {
        fmt.Println("Erro ao ler linhas do arquivo:", err)
    }
}
