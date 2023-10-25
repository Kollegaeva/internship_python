import string
import re

def text_stat(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        # Удаляем пунктуацию и приводим текст к нижнему регистру
        text = re.sub(r'[{}]'.format(string.punctuation), '', text).lower()

        # Удаляем лишние пробелы, оставляя только один пробел между словами
        text = re.sub(" +", " ", text)

        # Разделяем текст на слова и подсчитываем количество абзацев
        words = text.split()
        if text == '':
            paragraphs_count = 0
        elif text[-1] == '\n':
            paragraphs_count = len(text.split('\n')) - 1
        else:
            paragraphs_count = len(text.split('\n'))

        # Создаем словарь с частотой каждой буквы в тексте
        letter_counts = {letter: text.count(letter) for letter in text if letter != ' ' and letter != '\n'}

        # Подсчитываем общее количество слов в тексте
        word_count = len(words)

        # Подсчитываем долю слов
        frequency_letters = [word for word in letter_counts for i in text.split() if word in i]
        words_with_letter_count = {i: frequency_letters.count(i)/word_count for i in frequency_letters}

        # Находим слова, в которых есть буквы из обоих алфавитов
        rus_en_word_count = [word for word in words if bool(re.search('[a-zA-Z]', word)) and bool(re.search('[а-яА-ЯёЁ]', word))]

        result = {letter: (count, words_with_letter_count.get(letter, 0))for letter, count in letter_counts.items()}
        result['word_amount'] = word_count
        result['paragraph_amount'] = paragraphs_count
        result['bilingual_word_amount'] = len(rus_en_word_count)
        return result
    
    except Exception as e:
        return {'error': str(e)}
