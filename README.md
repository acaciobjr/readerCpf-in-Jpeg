# readerCpf-in-Jpeg
this program will allow you to extract only the cpf number of a text in a jpeg image.

The modules used were:
'pytesseract' for recognizing text in images
'cv2' for image manipulation 
're' for regular expressions 
'os' e 'fnmatch' for working with files and directories

After defining the path to the folder containing the images in Jpg format, the program will go through each file in the specified folder to check if the file has a Jpg extension. Text extraction from jpeg files is performed using a Tesseract OCR function, while poppler renders pdf files, enabling text extraction. If it is not possible to extract the text, the name of the file that could not be read will be informed. When it is possible to extract the text from the image, a regular expression will be used to search for only Cpf's in the text that will be added to a list afterwards. At the end, a message is printed informing the name of the file and the Cpf's found in the text.

Remember to install poppler and put it in the environment variable. https://blog.alivate.com.au/poppler-windows/

Portuguese:
Após a definição do caminho para a pasta que contém as imagens em formato Jpg, o programa irá percorrer cada arquivo na pasta especificada para verificar se o arquivo possui extensão Jpg. A extração do texto dos arquivos jpeg's ocorre com uma função do Tesseract OCR enquanto que o poppler possibilita a renderização dos arquivos pdf possibilitando a extração dos textos. Caso não seja possível a extração do texto, será informado o nome do arquivo que não foi possível ler. Quando for possível extrair o texto da imagem, será usado uma expressão regular para buscar apenas Cpf’s no texto que serão adicionados a uma lista em seguida. Ao fim, é impresso uma mensagem informando o nome do arquivo e os Cpf’s encontrados no texto.

Lembre-se de instalar o poppler e colocá-lo na variável de ambiente. https://blog.alivate.com.au/poppler-windows/

