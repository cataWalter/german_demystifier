import utils.io
import collections
import re
import mtranslate


def translate_word(word, language, count):
    if count <= 50:
        return "", ""
    elif language == 'english':
        english_translation = mtranslate.translate(word, 'en', 'de').lower()
        italian_translation = mtranslate.translate(word, 'it', 'de').lower()
        return english_translation, italian_translation
    elif language == 'italian':
        english_translation = mtranslate.translate(word, 'en', 'de').lower()
        italian_translation = mtranslate.translate(word, 'it', 'de').lower()
        return english_translation, italian_translation
    else:
        return "", ""


def main():
    text = utils.io.read_text_from_file('in/in.txt')
    word_counts = collections.Counter(re.findall(r'\b[a-zA-Z]+\b', text.lower()))
    total_words = sum(word_counts.values())

    output_str = f"Total Characters: {len(text)}\n" \
                 f"Total Words: {total_words}\n"

    is_blue = True  # Set to True to make the first line blue
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        english_translation, italian_translation = translate_word(word, 'english', count)
        percentage = f'{(count / total_words) * 100:.2f}%'

        if is_blue:
            output_str += f"<span style='color: blue;'>{word} ({english_translation}, {italian_translation}) {count} {percentage}</span>\n"
        else:
            output_str += f"{word} ({english_translation}, {italian_translation}) {count} {percentage}\n"

        is_blue = not is_blue  # Toggle the line color

    utils.io.write("out/word_frequencies.md", output_str, write_enabled=True)


main()
