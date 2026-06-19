import os
import shutil 

PASTA_ALVO = "../Testes"

CATEGORIAS = {
    "Videos" : [".mp4", ".mkv"],
    "Documents" : [".pdf", ".docx", ".txt"]
}

arquivos = os.listdir(PASTA_ALVO)

for arquivo in arquivos:
    nome, extensao = os.path.splitext(arquivo)
    for nome_pasta, extensao_pasta in CATEGORIAS.items():
        if extensao in extensao_pasta:
            pasta_destino = nome_pasta
            break 
print(f"arquivo original: {nome}, extensão: {extensao}")
