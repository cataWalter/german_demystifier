from re import split
import colorama
from mtranslate import translate
from spacy import load

from mapping import pos_mapping, tense_mapping, number_form_mapping, number_mapping, case_mapping, gender_mapping

colorama.init()


def parse_german_text(text):
    nlp = load("de_core_news_sm")
    doc = nlp(text)
    translations = []
    for token in doc:
        # morph_analysis = token.morph.to_dict()
        word = token.text
        pos = token.pos_
        case = token.morph.get("Case")
        gender = token.morph.get("Gender")
        number = token.morph.get("Number")
        tense = token.morph.get("Tense")
        number_form = token.morph.get("Person")
        english_translation = translate(word, 'en', 'de')
        italian_translation = translate(word, 'it', 'de')
        translations.append(
            (word, pos, case, gender, number, tense, number_form, english_translation, italian_translation))
    return translations


def print_word_details(translations):
    for word, pos, case, gender, number, tense, number_form, english_translation, italian_translation in translations:
        if pos != "PUNCT":
            pos_info = pos_mapping.get(pos, (pos, colorama.Fore.RESET))
            pos_name, pos_color = pos_info
            output_string = f'{pos_color}{word}{colorama.Fore.RESET}, {pos_color}{pos_name}{colorama.Fore.RESET}'
            if pos == "VERB" or pos == "AUX":
                if tense:
                    output_string += f', {pos_color}{tense_mapping.get(tense[0], tense[0])}{colorama.Fore.RESET}'
                if number_form:
                    output_string += f', {pos_color}{number_form_mapping.get(number_form[0], number_form[0])} Person{colorama.Fore.RESET}'
            if number:
                output_string += f', {pos_color}{number_mapping.get(number[0], number[0])}{colorama.Fore.RESET}'
            if case:
                output_string += f', {pos_color}{case_mapping.get(case[0], case[0])}{colorama.Fore.RESET}'
            if gender:
                output_string += f', {pos_color}{gender_mapping.get(gender[0], gender[0])}{colorama.Fore.RESET}'
            if english_translation and italian_translation:
                output_string += f', ({english_translation.lower()}, {italian_translation.lower()})'
            print(output_string)


def analyse_paragraph(german_text):
    for sentence in split(r'(?<=[.!?])\s', german_text):
        print()
        print(sentence)
        translated_text_en = translate(sentence, 'en', 'de')
        translated_text_it = translate(sentence, 'it', 'de')
        print(translated_text_en)
        print(translated_text_it)
        print()
        print_word_details(parse_german_text(sentence))
    colorama.deinit()


analyse_paragraph(
    ""
    "Das ist ein Beispieltext für die Demonstration der Wortarten. Das ist der zweite Satz! Und hier kommt der dritte Satz?"
    ""
)
