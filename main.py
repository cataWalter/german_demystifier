from re import split, sub
from mtranslate import translate
from spacy import load
from mapping import pos_mapping, tense_mapping, number_form_mapping, number_mapping, case_mapping, gender_mapping


def parse_german_text(text):
    nlp = load("de_core_news_sm")
    return [(token.text,
             token.pos_,
             *{k: token.morph.get(k) for k in ["Case", "Gender", "Number", "Tense", "Person"]}.values(),
             translate(token.text, 'en', 'de'),
             translate(token.text, 'it', 'de'))
            for token in nlp(text)]


def format_colored_text(text, color):
    return f'<span style="color:{color}">{text}</span>'


def get_word_details(translations):
    translated_details = []
    for word, pos, case, gender, number, tense, number_form, english_translation, italian_translation in translations:
        if pos != "PUNCT":
            pos_info = pos_mapping.get(pos)
            grammatical_details = [pos_info[0]]
            if pos in {"VERB", "AUX"} and tense:
                grammatical_details.append(tense_mapping.get(tense[0]))
            if pos in {"VERB", "AUX"} and number_form:
                grammatical_details.append(f"{number_form_mapping.get(number_form[0])} Person")
            if number:
                grammatical_details.append(number_mapping.get(number[0]))
            if case:
                grammatical_details.append(case_mapping.get(case[0]))
            if gender:
                grammatical_details.append(gender_mapping.get(gender[0]))
            grammatical_details_str = ", ".join(grammatical_details)
            translated_details.append(format_colored_text(
                f'{word}:'
                f' {grammatical_details_str},'
                f' ({english_translation.lower()},'
                f' {italian_translation.lower()})',
                pos_info[1])
            )
    return "\n".join(translated_details)


def create_output_string(sentence):
    if sentence.startswith(' '):
        sentence = sentence.lstrip()
    output_string = (f"\n{sentence}\n"
                     f"{translate(sentence, 'en', 'de')}\n"
                     f"{translate(sentence, 'it', 'de')}\n\n"
                     f"{get_word_details(parse_german_text(sentence))}\n")
    print(output_string)
    return output_string


def analyze_paragraph(german_text):
    result = ""
    for sentence in split(r'(?<=[.!?])\s', german_text):
        result += create_output_string(sentence)
    return result


def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as input_file:
        return sub(r'\n', '', input_file.read())


def write_to_file(file_path, result):
    with open(file_path, "w", encoding="utf-8") as output_file:
        output_file.write(result)


def main():
    result = analyze_paragraph(read_text_from_file('in.txt'))
    write_to_file_enabled = True
    if write_to_file_enabled:
        write_to_file("out.md", result)


if __name__ == "__main__":
    main()
