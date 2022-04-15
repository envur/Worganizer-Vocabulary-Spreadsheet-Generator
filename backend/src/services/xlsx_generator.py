import xlsxwriter
from src.schemas import words as w_schemas


def create_word_list(words):
    words_list = []
    for data in words:
        data = w_schemas.WordBase(**data.__dict__)
        words_list.append(data)
    return words_list

def get_keys(word_dict):
    keys = []
    for key, value in word_dict:
        key = key.capitalize()
        keys.append(key)
    return keys

def write_keys_in_file(keys, worksheet, header):
    col = 0
    for key in keys:
        worksheet.write(0, col, key, header)
        col += 1

def write_data_in_file(words_list, worksheet):
    row = 0
    for word_dict in words_list:
        col = 0
        for key, value in word_dict:
            worksheet.write(row + 1, col, value)
            col += 1
        row += 1

def xlsx_generator(words):
    workbook = xlsxwriter.Workbook('/tmp/Words.xlsx')
    worksheet = workbook.add_worksheet()
    
    header = workbook.add_format({'bold': True, 'bg_color': '#9fedb4', 'align': 'center', 'valign': 'middle', 'border': True})

    row = 0
    words_list = create_word_list(words)
    keys = get_keys(words_list[0])
    worksheet.set_column(0, 4, 30)
    
    write_keys_in_file(keys, worksheet, header)
    write_data_in_file(words_list, worksheet)

    workbook.close()