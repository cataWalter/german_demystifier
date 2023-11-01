import colorama

pos_mapping = {
    "ADJ": ("Adjective", colorama.Fore.GREEN),
    "ADP": ("Preposition", colorama.Fore.YELLOW),
    "ADV": ("Adverb", colorama.Fore.CYAN),
    "AUX": ("Verb", colorama.Fore.GREEN),
    "CCONJ": ("Coordinating conjunction", colorama.Fore.BLUE),
    "DET": ("Determiner", colorama.Fore.LIGHTRED_EX),
    "INTJ": ("Interjection", colorama.Fore.WHITE),
    "NOUN": ("Noun", colorama.Fore.BLUE),
    "NUM": ("Numeral", colorama.Fore.LIGHTGREEN_EX),
    "PART": ("Particle", colorama.Fore.LIGHTYELLOW_EX),
    "PRON": ("Pronoun", colorama.Fore.LIGHTCYAN_EX),
    "PROPN": ("Proper noun", colorama.Fore.LIGHTBLUE_EX),
    "PUNCT": ("Punctuation", colorama.Fore.RED),
    "SCONJ": ("Subordinating conjunction", colorama.Fore.LIGHTWHITE_EX),
    "SYM": ("Symbol", colorama.Fore.YELLOW),
    "VERB": ("Verb", colorama.Fore.GREEN),
    "X": ("Other", colorama.Fore.RESET)
}
case_mapping = {
    "Nom": "Nominative",
    "Gen": "Genitive",
    "Dat": "Dative",
    "Acc": "Accusative",
    "Abl": "Ablative",
    "Voc": "Vocative"
}
gender_mapping = {
    "Masc": "Masculine",
    "Fem": "Feminine",
    "Neut": "Neuter",
}
number_mapping = {
    "Sing": "Singular",
    "Plur": "Plural"
}
tense_mapping = {
    "Pres": "Present",
    "Past": "Past",
    "Fut": "Future",
    "PresPart": "Present Participle",
    "PastPart": "Past Participle",
    "PresCont": "Present Continuous",
    "PastCont": "Past Continuous",
    "FutCont": "Future Continuous",
    "PresPerf": "Present Perfect",
    "PastPerf": "Past Perfect",
    "FutPerf": "Future Perfect",
    "PresPerfCont": "Present Perfect Continuous",
    "PastPerfCont": "Past Perfect Continuous",
    "FutPerfCont": "Future Perfect Continuous",
    "Cond": "Conditional",
    "CondPerf": "Conditional Perfect",
    "Imp": "Imperative",
    "SubjPres": "Subjunctive Present",
    "SubjPast": "Subjunctive Past",
    "SubjPresCont": "Subjunctive Present Continuous",
    "SubjPastCont": "Subjunctive Past Continuous",
    "SubjPresPerf": "Subjunctive Present Perfect",
    "SubjPastPerf": "Subjunctive Past Perfect",
    "SubjPresPerfCont": "Subjunctive Present Perfect Continuous",
    "SubjPastPerfCont": "Subjunctive Past Perfect Continuous",
}
number_form_mapping = {
    "1s": "1st person singular",
    "2s": "2nd person singular",
    "3s": "3rd person singular",
    "1p": "1st person plural",
    "2p": "2nd person plural",
    "3p": "3rd person plural"
}
