import os
import re
import fnmatch
import cv2
import pytesseract
from pdf2image import convert_from_path
#from config import connection

#iniciando conexao com o banco
#cursor = connection.cursor()

#caminhos
caminho_imagens = r"C:\Users\Matheus\Documents\GitHub\Leitor_de_Arquivo\files"
caminho_tesseract = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho_tesseract + r"\tesseract.exe"

for nome_arquivo in os.listdir(caminho_imagens):
    if fnmatch.fnmatch(nome_arquivo, '*.pdf'):
        caminho_arquivo = os.path.join(caminho_imagens, nome_arquivo)

        imagens = convert_from_path(caminho_arquivo)
        #Convertendo PDF em JPEG para a leitura do arquivo
        for imagem in imagens:
            temp_img_path = 'temp_img.jpg'
            imagem.save(temp_img_path, 'JPEG')
            #Armazenando o texto do JPEG
            texto = pytesseract.image_to_string(cv2.imread(temp_img_path))
            #Apagando arquivo
            os.remove(temp_img_path)

            if not texto:
                print(f"Não foi possível identificar o texto na imagem {caminho_arquivo}.")
            else:
                cpfs = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', texto)
                nomes = re.findall(r'[A-Z][a-z]+(?: [A-Z][a-z]+)+', texto)
                cpfs_numeros = []
                for cpf in cpfs:
                    cpf_numeros = re.sub(r'\D', '', cpf)
                    cpfs_numeros.append(cpf_numeros)
                    #quardando informacao no banco
                    #qry_InsertCPFs = f'INSERT INTO documentos_tratados(CPF_DOCUMENTO) \
                    #                   VALUES ({cpf_numeros})'
                    #cursor.execute(qry_InsertCPFs)  #executando query
                    #connection.commit()             #editando no banco

#cursor.close()  #finalizando a conexão
#connection.close() #finalizando a conexão