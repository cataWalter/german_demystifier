# Multilingual Text Analysis Tool

## Overview

The **Multilingual Text Analysis Tool** is a versatile utility designed to assist users in the analysis of German text.
It offers features like part-of-speech tagging, translation, and word frequency analysis. This project comprises two dis
tinct components: the German text analysis and word frequency analysis.

## German Text Analysis

### Features

- **Part-of-Speech Tagging**: Utilizes the `spacy` library to identify the part of speech for each word in German text.
- **Morphological Analysis**: Provides detailed morphological information including case, gender, number, tense, and per
son for verbs.
- **Multilingual Translation**: Translates the German text into English and Italian for better comprehension.

### How to Use

1. Input a German text.
2. The tool breaks the text into sentences and provides detailed analysis for each sentence.
3. It displays the translated text in English and Italian.
4. Provides word-level analysis, including part of speech, grammatical details, and translations.

## Word Frequency Analysis

### Features

- **Word Frequency Count**: Counts the occurrences of each word in the input text.
- **Translation Threshold**: Translates frequently occurring words (count > 50) into English and Italian.
- **Percentage Calculation**: Calculates the percentage of each word's occurrence in the text.

### How to Use

1. Input a text document.
2. The tool counts word frequencies and calculates percentages.
3. Translates frequently occurring words into English and Italian.
4. Outputs word frequency analysis in tabular format.

## Example Outputs

### German Text Analysis

Input:
```text
Wie froh bin ich, daß ich weg bin! Bester Freund, was ist das Herz des Menschen! Dich zu verlassen, den ich so liebe, von dem ich unzertrennlich war, und froh zu sein!
```

Output:

Wie froh bin ich, daß ich weg bin!
How glad I am that I'm gone!
Quanto sono felice di non esserci più!

<span style="color:orange">Wie: Adverb, (how, come)</span>
<span style="color:orange">froh: Adverb, (glad, lieto)</span>
<span style="color:olive">bin: Verb, Present, None Person, Singular, (am, sono)</span>
<span style="color:purple">ich: Pronoun, Singular, Nominative, (i, io)</span>
<span style="color:maroon">daß: Subordinating conjunction, (that, quello)</span>
<span style="color:purple">ich: Pronoun, Singular, Nominative, (i, io)</span>
<span style="color:orange">weg: Adverb, (away, lontano)</span>
<span style="color:olive">bin: Verb, Present, None Person, Singular, (am, sono)</span>

Bester Freund, was ist das Herz des Menschen!
Best friend, what is the heart of man!
Migliore amico, qual è il cuore dell'uomo!

<span style="color:purple">Bester: Adjective, Singular, Nominative, Masculine, (best, migliore)</span>
<span style="color:silver">Freund: Noun, Singular, Nominative, Masculine, (friend, amico)</span>
<span style="color:purple">was: Pronoun, Singular, Nominative, Neuter, (what, che cosa)</span>
<span style="color:olive">ist: Verb, Present, None Person, Singular, (is, è)</span>
<span style="color:navy">das: Determiner, Singular, Nominative, Neuter, (the, il)</span>
<span style="color:silver">Herz: Noun, Singular, Nominative, Neuter, (heart, cuore)</span>
<span style="color:navy">des: Determiner, Singular, Genitive, Masculine, (of, di)</span>
<span style="color:silver">Menschen: Noun, Singular, Genitive, Masculine, (people, persone)</span>

Dich zu verlassen, den ich so liebe, von dem ich unzertrennlich war, und froh zu sein!
To leave you, whom I love so much, from whom I was inseparable, and be happy!
Lasciarti, che amo tanto, dal quale ero inseparabile, ed essere felice!

<span style="color:purple">Dich: Pronoun, Singular, Accusative, Masculine, (you, voi)</span>
<span style="color:aqua">zu: Particle, (to, a)</span>
<span style="color:olive">verlassen: Verb, (leave, partire)</span>
<span style="color:purple">den: Pronoun, Singular, Accusative, Masculine, (the, il)</span>
<span style="color:purple">ich: Pronoun, Singular, Nominative, (i, io)</span>
<span style="color:orange">so: Adverb, (so, così)</span>
<span style="color:olive">liebe: Verb, Present, None Person, Singular, (love, amore)</span>
<span style="color:teal">von: Preposition, (from, da)</span>
<span style="color:purple">dem: Pronoun, Singular, Dative, Masculine, (dem, dem)</span>
<span style="color:purple">ich: Pronoun, Singular, Nominative, (i, io)</span>
<span style="color:orange">unzertrennlich: Adverb, (inseparable, inseparabile)</span>
<span style="color:olive">war: Verb, Past, None Person, Singular, (was, era)</span>
<span style="color:maroon">und: Coordinating conjunction, (and, e)</span>
<span style="color:orange">froh: Adverb, (glad, lieto)</span>
<span style="color:aqua">zu: Particle, (to, a)</span>
<span style="color:olive">sein: Verb, (be, essere)</span>



### Word Frequency Analysis

Input:
```text
"D is a sample text. It contains multiple words. This is a simple text!"
```

Output:
```text
Total Characters: 66
Total Words: 12
+--------+--------------+--------------+-----------------------+-----------------------+
|  Word  | Occurrences  | Percentage   | English Translation   | Italian Translation   |
+========+==============+==============+=======================+=======================+
|  this  | 3            | 25.00%       |                       |                       |
+--------+--------------+--------------+-----------------------+-----------------------+
|  is    | 2            | 16.67%       |                       |                       |
+--------+--------------+--------------+-----------------------+-----------------------+
|  a     | 2            | 16.67%       |                       |                       |
...
```
## Getting Started

1. Clone this repository.
2. Install the necessary dependencies.
3. Run the desired analysis script.

## Dependencies

- `spacy` for German text analysis.
- `mtranslate` for translation services.
- `tabulate` for creating tabular output.
- `collections` for word frequency analysis.
- `re` for text parsing.

## License

This project is released under the [MIT License](LICENSE). Feel free to use and modify it for your needs.

## Contributions

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or submit a pull re
quest.

## Author

- Walter Catalfamo
- cata.walter@gmail.com

## Acknowledgments

Special thanks to the developers of `spacy`, `mtranslate`, and `tabulate` for their incredible open-source contributions
.

Enjoy using the Multilingual Text Analysis Tool! We hope it enhances your text analysis capabilities.
