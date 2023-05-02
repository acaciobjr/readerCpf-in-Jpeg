import pytesseract
import cv2
import re
import os
import fnmatch

#Aqui você precisa inserir o endereço do diretório que possuem as jpegs
caminho_imagens = r"caminho da pasta que deseja ler os cpfs em Jpeg's"

for nome_arquivo in os.listdir(caminho_imagens):
    if fnmatch.fnmatch(nome_arquivo, '*.jpg'):
        caminho_arquivo = os.path.join(caminho_imagens, nome_arquivo)
        imagem = cv2.imread(caminho_arquivo)
        #Esta configuração de medidas são para imagens com dimensões de 1160 x 1600 pixels
        x, y, largura, altura = 300, 400, 560, 800
        partedaimagem = imagem[y:y + altura, x:x + largura]

        caminho = r"C:\Program Files\Tesseract-OCR"
        pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
        texto = pytesseract.image_to_string(partedaimagem)

        if not texto:
            print(f"Não foi possível identificar o texto na imagem {caminho_arquivo}.")
        else:
            cpfs = re.findall(r'\d{3}\.\d{3}\ .\d{3}-\d{2}', texto)
            cpfs_numeros = []
            for cpf in cpfs:
                cpf_numeros = re.sub(r'\D', '', cpf)
                cpfs_numeros.append(cpf_numeros)
            print(f"CPF(s) na imagem {caminho_arquivo} é: {cpfs_numeros}")
