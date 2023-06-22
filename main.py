import difflib
import os

def processar_texto(texto_limpo, caminho_arquivo):
    if texto_limpo:
        print("Texto encontrado no arquivo:", caminho_arquivo)
    else:
        avisoFalha = f"Não foi possível identificar texto no arquivo {caminho_arquivo}."
        print(avisoFalha)

def ler_texto_notepad(caminho_arquivo):
    for nome_arquivo in os.listdir(caminho_arquivo):
        try:
            caminho_completo = os.path.join(caminho_arquivo, nome_arquivo)
            with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
                texto = arquivo.read()
                return texto
        except Exception as e:
            print(f"Erro ao ler o arquivo {caminho_completo}: {str(e)}")
            return None

def comparar_textos(caminho_texto1, caminho_texto2):
    texto1 = ler_texto_notepad(caminho_texto1)
    texto2 = ler_texto_notepad(caminho_texto2)

    if texto1 is not None and texto2 is not None:
        linhas_texto1 = texto1.split('\n')
        linhas_texto2 = texto2.split('\n')

        diferenca = difflib.ndiff(linhas_texto1, linhas_texto2)

        exclusivo_texto1 = []
        exclusivo_texto2 = []
        igual_texto1_texto2 = []

        for linha in diferenca:
            if linha.startswith('- '):
                exclusivo_texto1.append(linha[2:])
            elif linha.startswith('+ '):
                exclusivo_texto2.append(linha[2:])
            else:
                igual_texto1_texto2.append(linha[2:])

        with open('diferenca.txt', 'w', encoding='utf-8') as f:
            f.write('Linhas exclusivas no texto 1. Está faltando no texto 2:\n')
            for linha in exclusivo_texto1:
                f.write(f'{linha}\n')

            f.write('\nLinhas exclusivas no texto 2:\n')
            for linha in exclusivo_texto2:
                f.write(f'{linha}\n')

            f.write('\nLinhas iguais nos dois textos:\n')
            for linha in igual_texto1_texto2:
                f.write(f'{linha}\n')
                
# Caminhos dos arquivos de texto
caminho_texto1 = r"C:\Users\Rose\Documents\listComp\Diretorio1"
caminho_texto2 = r"C:\Users\Rose\Documents\listComp\Diretorio2"

comparar_textos(caminho_texto1, caminho_texto2)
