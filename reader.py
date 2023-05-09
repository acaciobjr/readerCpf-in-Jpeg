import pytesseract
import cv2
import os
import re
from pdf2image import convert_from_path

# caminhos
caminho_imagens = r"C:\Users\Rose\Documents\Gteste"
caminho_tesseract = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = os.path.join(caminho_tesseract, "tesseract.exe")


def processar_texto(texto, caminho_arquivo, f):
    if not texto:
        print(f"Não foi possível identificar o texto no arquivo {caminho_arquivo}.")
        return

    cpfs = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', texto)
    RG = re.findall(r'\d{13}', texto)
    print(RG)
    cpfs_numeros = [re.sub(r'\D', '', cpf) for cpf in cpfs]

    if cpfs_numeros:
        avisoLocal = f"CPF e RG no arquivo {caminho_arquivo} são: {cpfs_numeros} e {RG}"
        print(avisoLocal)
        str_cpfs = ",".join(cpfs_numeros)
        f.write(avisoLocal + "\n")
    else:
        print(f"Não foi possível identificar CPFs no arquivo {caminho_arquivo}.")


with open('texto.txt', 'w', encoding='utf-8') as f:
    for nome_arquivo in os.listdir(caminho_imagens):
        extensao = os.path.splitext(nome_arquivo)[1].lower()
        caminho_arquivo = os.path.join(caminho_imagens, nome_arquivo)
        texto = ''

        if extensao == '.pdf':
            imagens = convert_from_path(caminho_arquivo)
            for imagem in imagens:
                temp_img_path = 'temp_img.jpg'
                imagem.save(temp_img_path, 'JPEG')
                texto += pytesseract.image_to_string(cv2.imread(temp_img_path))
                os.remove(temp_img_path)

        elif extensao == '.jpg':
            imagem = cv2.imread(caminho_arquivo)
            texto = pytesseract.image_to_string(imagem)

        if texto:
            processar_texto(texto, caminho_arquivo, f)
