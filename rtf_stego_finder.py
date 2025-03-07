import re
import argparse  # Importing argparse for command-line argument parsing

def extract_different_font_chars(rtf_text):
    # Регулярное выражение для поиска команд смены шрифта и текста между ними
    pattern = re.compile(r'\\f(\d+)(.*?)(?=\\f\d+|$)', re.DOTALL)
    
    # Основной шрифт (предположим, что это \f0)
    main_font = '0'
    
    # Список для хранения символов другого шрифта
    different_font_chars = []
    
    # Поиск всех совпадений
    matches = pattern.findall(rtf_text)
    
    for match in matches:
        font_number, text = match
        if font_number != main_font:
            # Убираем RTF-команды и служебные данные из текста
            clean_text = re.sub(r'\\[a-zA-Z0-9]+', '', text)  # Удаляем все RTF-команды
            clean_text = re.sub(r'\{.*?\}', '', clean_text)    # Удаляем блоки в {}
            clean_text = re.sub(r'\s+', ' ', clean_text)       # Убираем лишние пробелы
            clean_text = clean_text.strip()                    # Убираем пробелы по краям
            
            # Если текст не пустой, добавляем его в список
            if clean_text:
                different_font_chars.append(clean_text)
    
    # Возвращаем символы другого шрифта в виде строки
    return ''.join(different_font_chars)

# получим объект файла
def read_my_file(args):
    file_name=str(args.rtf)
    with open(file_name,"r",encoding="utf-8") as f:
        lines = f.read()
    return lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reading text rtf")
    parser.add_argument("-w", "--rtf", help="text to analyze")
    args = parser.parse_args()

# Извлекаем символы другого шрифта
    result = extract_different_font_chars(read_my_file(args))
    print("Символы другого шрифта:", result)
