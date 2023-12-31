import re
import spacy
import mtranslate
import utils.io
import utils.constants


def parse_german_text(text):
    nlp = spacy.load("de_core_news_sm")
    return [(token.text,
             token.pos_,
             *{k: token.morph.get(k) for k in ["Case", "Gender", "Number", "Tense", "Person"]}.values(),
             mtranslate.translate(token.text, 'en', 'de'))
            for token in nlp(text)]


def format_colored_text(text, color):
    return f'<span style="color:{color}">{text}</span>'


def get_word_details(translations):
    translated_details = []
    for word, pos, case, gender, number, tense, number_form, english_translation in translations:
        if pos != "PUNCT":
            pos_info = utils.constants.part_of_speech.get(pos)
            grammatical_details = [pos_info[0]]
            if pos in {"VERB", "AUX"} and tense:
                grammatical_details.append(utils.constants.verb_tense.get(tense[0]))
            if pos in {"VERB", "AUX"} and number_form:
                grammatical_details.append(f"{utils.constants.verb_person.get(number_form[0])} Person")
            if number:
                grammatical_details.append(utils.constants.number.get(number[0]))
            if case:
                grammatical_details.append(utils.constants.declension.get(case[0]))
            if gender:
                grammatical_details.append(utils.constants.gender.get(gender[0]))
            grammatical_details_str = ", ".join(grammatical_details)
            translated_details.append(format_colored_text(
                f'{word}:'
                f' {grammatical_details_str},'
                f' {english_translation.lower()}',
                pos_info[1])
            )
    return "<br>\n".join(translated_details)


def create_output_string(sentence):
    if sentence.startswith(' '):
        sentence = sentence.lstrip()
    output_string = (f'<div style="display: flex; justify-content: space-between; flex-wrap: wrap;">\n'
                     f'    <div style="flex-basis: 48%;">\n'
                     f'        {sentence}<br>\n'
                     f'        <br>\n'
                     f'    </div>\n'
                     f'    <div style="flex-basis: 48%;">\n'
                     f'        {get_word_details(parse_german_text(sentence))}\n'
                     f'    </div>\n'
                     f'</div>\n'
                     f'<br />\n'
                     f'<br />\n'
                     f'\n')
    print(output_string)
    return output_string


def analyze_paragraph(german_text):
    return ''.join([create_output_string(sentence) for sentence in re.split(r'(?<=[.!?])\s', german_text)])


def main():
    result = analyze_paragraph(utils.io.read_text_from_file('in/in.txt'))
    utils.io.write("out/out.md", result, write_enabled=True)


main()
