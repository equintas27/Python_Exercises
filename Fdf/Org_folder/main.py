import os
import shutil 

PASTA_ALVO = "./Testes"

CATEGORIAS = {
    "Videos" : [".mp4", ".mkv"],
    "Documents" : [".pdf", ".docx", ".txt"]
}

arquivos = os.listdir(PASTA_ALVO)

for arquivo in arquivos:

    pasta_origem = os.path.join(PASTA_ALVO, arquivo)
    nome, extensao = os.path.splitext(arquivo)
    if os.path.isdir(pasta_origem):
        continue 
    pasta_destino = "Outros"
    for nome_pasta, extensao_pasta in CATEGORIAS.items():
        if extensao in extensao_pasta:
            pasta_destino = nome_pasta
            break 
    caminho_pasta_destino = os.path.join(PASTA_ALVO, pasta_destino)
    if not os.path.isdir(caminho_pasta_destino):
        os.makedirs(caminho_pasta_destino)
        print(f"Nova pasta criada: {pasta_destino}")
    caminho_final_arquivo = os.path.join(caminho_pasta_destino, arquivo)
    shutil.move(pasta_origem, caminho_final_arquivo)
    print(f"Movido: {arquivo} -> {pasta_destino}/")
print ("Organização finalizada!")


