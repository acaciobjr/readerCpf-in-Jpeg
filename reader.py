import pytesseract
import cv2
import re
import os
import fnmatch

caminho_imagens = r"C:\Users\Rose\Documents\Gteste"

with open('texto.txt', 'w', encoding='utf-8') as f:
    avisoLocal = "Os cpfs encontrados foram: "

    for nome_arquivo in os.listdir(caminho_imagens):
        if fnmatch.fnmatch(nome_arquivo, '*.jpg'):
            caminho_arquivo = os.path.join(caminho_imagens, nome_arquivo)

            imagem = cv2.imread(caminho_arquivo)
            caminho = r"C:\Program Files\Tesseract-OCR"
            pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
            texto = pytesseract.image_to_string(imagem)

            if not texto:
                print(f"Não foi possível identificar o texto na imagem {caminho_arquivo}.")
            else:
                cpfs = re.findall(r'\d{3}\.\d{3}\ .\d{3}-\d{2}', texto)
                cpfs_numeros = []
                for cpf in cpfs:
                    cpf_numeros = re.sub(r'\D', '', cpf)
                    cpfs_numeros.append(cpf_numeros)
                print(f"CPF(s) na imagem {caminho_arquivo} é: {cpfs_numeros}")
                str_cpfs = ",".join(cpfs_numeros)
                f.write(avisoLocal + str_cpfs + "\n")
