import utils.io
import collections
import tabulate
import re
import mtranslate


def translate_word(word, language, count):
    if count <= 50:
        return ""
    elif language == 'english':
        return mtranslate.translate(word, 'en', 'de').lower()
    elif language == 'italian':
        return mtranslate.translate(word, 'it', 'de').lower()
    else:
        return word


def main():
    text = utils.io.read_text_from_file('in/in.txt')
    word_counts = collections.Counter(re.findall(r'\b[a-zA-Z]+\b', text.lower()))
    total_words = sum(word_counts.values())

    table_data = []
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        translations = [translate_word(word, lang, count) for lang in ['english', 'italian']]
        table_data.append([word, count, f'{(count / total_words) * 100:.2f}%', *translations])

    table_headers = ['Word', 'Occurrences', 'Percentage', 'English Translation', 'Italian Translation']
    table_str = tabulate.tabulate(table_data, headers=table_headers, tablefmt='grid')

    output_str = f"Total Characters: {len(text)}\n" \
                 f"Total Words: {total_words}\n" \
                 f"{table_str}"

    utils.io.write("out/word_frequencies.md", output_str, write_enabled=True)


main()
