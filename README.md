# readerCpf-in-Jpeg
this program will allow you to extract only the cpf number of a text in a jpeg image.

The modules used were:
'pytesseract' for recognizing text in images
'cv2' for image manipulation 
're' for regular expressions 
'os' e 'fnmatch' for working with files and directories

After defining the path to the folder containing Jpg images, the program will loop through each file in the specified folder to check if the file has a Jpg extension. The image reading will be enabled by specifying the metric coordinates of the image, which the user should modify according to the size of the Jpg's. The program used measurements for a Jpg of 1160 x 1600 pixels. Text extraction is performed using a Tesseract OCR function. If text extraction is not possible, the name of the file that could not be read will be displayed. When it is possible to extract text from the image, a regular expression is used to search only for CPFs in the text, which will then be added to a list. Finally, a message is printed informing the file name and CPFs found in the text.

Portuguese:
Após a definição do caminho para a pasta que contém as imagens em formato Jpg, o programa irá percorrer cada arquivo na pasta especificada para verificar se o arquivo possui extensão Jpg. A leitura da imagem será possibilitada pela especificação das coordenadas métricas da imagem, que o usuário deve alterar conforme o tamanho das Jpg’s. O programa utilizou medidas para uma Jpg de 1160 x 1600 pixels. A extração do texto ocorre com uma função do Tesseract OCR. Caso não seja possível a extração do texto, será informado o nome do arquivo que não foi possível ler. Quando for possível extrair o texto da imagem, será usado uma expressão regular para buscar apenas Cpf’s no texto que serão adicionados a uma lista em seguida. Ao fim, é impresso uma mensagem informando o nome do arquivo e os Cpf’s encontrados no texto.

