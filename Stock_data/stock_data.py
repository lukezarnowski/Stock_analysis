import os

def load_csv_files_from_folder(directory_path: str):
    ceny_akcji_dla_firm_z_folderu = []

    for file_name in os.listdir(directory_path):
        cena_akcji_firmy = load_data(f'{directory_path}/{file_name}')
        ceny_akcji_dla_firm_z_folderu.append(cena_akcji_firmy)

    return ceny_akcji_dla_firm_z_folderu


def load_data(path) -> list:
    with open(path, 'r') as file:
        lines = file.readlines()
        rows = []
        for line in lines:
            line = line.strip()
            row = line.split(',')
            rows.append(row)
        return rows


def dodaj_kolumne_ze_zmiana_ceny_akcji(ceny_akcji_firmy):
    ceny_akcji_firmy[0].append('zmiana kursu akcji w %')
    for i in range(1, len(ceny_akcji_firmy)):
        close = float(ceny_akcji_firmy[i][4])
        open = float(ceny_akcji_firmy[i][1])
        change = (close - open) / open
        ceny_akcji_firmy[i].append(f'{change}')
    return ceny_akcji_firmy


def save_data_to_file(data, path):
    csv_rows = []
    for row in data:
        csv_row = ','.join(row)
        csv_rows.append(csv_row)

    csv_string = '\n'.join(csv_rows)

    with open(path, 'w') as file:
        file.write(csv_string)


def nowe_nazwy_dla_plikow():
    return os.listdir(f'data')


def zmien_nazwe(lista_nazw, indeks_nazwy_pliku):
    nowa = lista_nazw[indeks_nazwy_pliku]
    nowa = nowa[:-4] + 'ze_zmiana_proc.'
    return nowa


if __name__ == '__main__':
    nazwy = nowe_nazwy_dla_plikow()
    i = 0
    for ceny_firmy in load_csv_files_from_folder('data'):
        zmienione_ceny_firmy = dodaj_kolumne_ze_zmiana_ceny_akcji(ceny_firmy)
        save_data_to_file(zmienione_ceny_firmy, f'data/{zmien_nazwe(nazwy,i)}.csv')
        i = i + 1