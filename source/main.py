import os
import re
import fnmatch
import cv2
import pytesseract
from pdf2image import convert_from_path

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
                cpfs_numeros = []
                for cpf in cpfs:
                    cpf_numeros = re.sub(r'\D', '', cpf)
                    cpfs_numeros.append(cpf_numeros)
                print(f"CPF(s) na imagem {caminho_arquivo} é: {cpfs_numeros}")
                #str_cpfs = ",".join(cpfs_numeros)
                #f.write(avisoLocal + str_cpfs + "\n")
