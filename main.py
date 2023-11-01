from re import split
import colorama
from mtranslate import translate
from spacy import load
from mapping import pos_mapping, tense_mapping, number_form_mapping, number_mapping, case_mapping, gender_mapping

colorama.init()


def parse_german_text(text):
    nlp = load("de_core_news_sm")
    return [(token.text,
             token.pos_,
             *{k: token.morph.get(k) for k in ["Case", "Gender", "Number", "Tense", "Person"]}.values(),
             translate(token.text, 'en', 'de'),
             translate(token.text, 'it', 'de'))
            for token in nlp(text)]


def print_word_details(translations):
    for word, pos, case, gender, number, tense, number_form, english_translation, italian_translation in translations:
        if pos != "PUNCT":
            pos_info = pos_mapping.get(pos, (pos, colorama.Fore.RESET))
            print(
                f'{pos_info[1]}{word}{colorama.Fore.RESET},'
                f' {pos_info[1]}{pos_info[0]}{colorama.Fore.RESET},'
                f' {pos_info[1]}{", ".join(filter(None, [tense_mapping.get(tense[0], tense[0]) if pos in {"VERB", "AUX"} and tense else "", f"{number_form_mapping.get(number_form[0], number_form[0])} Person" if pos in {"VERB", "AUX"} and number_form else "", number_mapping.get(number[0], number[0]) if number else "", case_mapping.get(case[0], case[0]) if case else "", gender_mapping.get(gender[0], gender[0]) if gender else ""]))}{colorama.Fore.RESET}'
                f'{f"({english_translation.lower()}, {italian_translation.lower()})" if english_translation and italian_translation else ""}')


def analyse_paragraph(german_text):
    for sentence in split(r'(?<=[.!?])\s', german_text):
        print('\n{}\n{}\n{}\n'.format(
            sentence,
            translate(sentence, 'en', 'de'),
            translate(sentence, 'it', 'de')
        ))
        print_word_details(parse_german_text(sentence))
    colorama.deinit()


analyse_paragraph(
    ""
    "Das ist ein Beispieltext für die Demonstration der Wortarten. Das ist der zweite Satz! Und hier kommt der dritte Satz?"
    ""
)
