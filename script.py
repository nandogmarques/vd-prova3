import pandas as pd
import re

# Carregar o CSV
file_path = "./tabela5938 - Tabela.csv"
df = pd.read_csv(file_path)

# Nome da coluna que contém cidade e estado
coluna_origem = "Município"  # Substitua pelo nome correto da coluna

# Função para extrair o estado e remover do nome
def extrair_estado(texto):
    match = re.search(r"\((.*?)\)", texto)
    if match:
        estado = match.group(1)  # Captura o estado dentro dos parênteses
        texto_sem_estado = re.sub(r"\s*\(.*?\)", "", texto)  # Remove o estado e os parênteses
        return texto_sem_estado.strip(), estado  # Retorna nome limpo e estado
    return texto.strip(), None

# Aplicar a função e separar os valores em duas colunas
df[["Município", "Estado"]] = df[coluna_origem].apply(lambda x: pd.Series(extrair_estado(x)))

# Salvar o resultado em um novo arquivo
output_path = "./tabela_estados.csv"
df.to_csv(output_path, index=False)

print(f"Arquivo processado e salvo em: {output_path}")
