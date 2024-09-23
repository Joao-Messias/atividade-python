import csv
from pathlib import Path
from db import adicionar_livro, listar_livros

EXPORT_FILE = Path('exports/livros_exportados.csv')

def exportar_para_csv():
    livros = listar_livros()
    with open(EXPORT_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Título', 'Autor', 'Ano de Publicação', 'Preço'])
        writer.writerows(livros)

def importar_de_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            adicionar_livro(row['Título'], row['Autor'], int(row['Ano de Publicação']), float(row['Preço']))
