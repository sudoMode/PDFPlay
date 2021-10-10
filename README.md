# PDFPlay
```python
some tag line
```
---

[comment]: <> (badges 1)
<p align="center">
    <a href="#">
        <img src="https://raw.githubusercontent.com/sudoMode/PDFPlay/master/images/made-with-python.svg"/>
    </a>
    <a href="#">
        <img src="https://raw.githubusercontent.com/sudoMode/PDFPlay/master/images/powered-by-coffee.svg"/>
    </a>
    <a href="#">
        <img src="https://raw.githubusercontent.com/sudoMode/PDFPlay/master/images/open-source.svg"/>
    </a>
    <a href="#">
        <img src="https://raw.githubusercontent.com/sudoMode/PDFPlay/master/images/built-with-love.svg"/>
    </a>
</p>

---

[comment]: <> (badges 2)
<p align="center">
    <a href="https://www.codefactor.io/repository/github/sudomode/pdfplay">
        <img src="https://img.shields.io/codefactor/grade/github/sudomode/PDFPlay/master?style=for-the-badge"/>
    </a>
    <a href="https://github.com/sudoMode/PDFPlay/releases">
        <img src="https://img.shields.io/github/v/release/sudomode/pdfplay?style=for-the-badge"/>
    </a>
    <a href="#">
        <img src="https://img.shields.io/github/languages/code-size/sudomode/pdfplay?color=black&style=for-the-badge"/>
    </a>
    <a href="https://raw.githubusercontent.com/sudoMode/PDFPlay/master/LICENSE">
        <img src="https://img.shields.io/github/license/sudomode/pdfplay?color=pink&style=for-the-badge"/>
    </a>
</p>

---


[comment]: <> (Intro)

***Decat*** is a Python package capable of de-concatenating strings that do not have

white-spaces in them, or in other words, it allows the user to infer spaces

programmatically. This is a simple utility that comes in handy with various modern

Natural Language Processing(NLP) tasks such as cleaning, exploration or even manipulation

of text. [Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law) is

at the

core of this

project, the aim is to provide an easy interface for programmers to extract meaningful

information out of deformed pieces of texts.


[comment]: <> (## Get Started)

[comment]: <> (> ### Install It)

[comment]: <> (>>```python)

[comment]: <> (>> >> pip install decat)

[comment]: <> (>>```)

[comment]: <> (> ### Play With It)

[comment]: <> (>>```python)

[comment]: <> (>> >> decat -i someweirdtext)

[comment]: <> (>> >> ['some', 'weird', 'text'])

[comment]: <> (>>```)

[comment]: <> (>> or)

[comment]: <> (>>```python)

[comment]: <> (>> >> python -m decat -i justanotherstring)

[comment]: <> (>> >> ['just', 'another', 'string'])

[comment]: <> (>>```)

[comment]: <> (> ### Use It In Your Projects)

[comment]: <> (>> #### _Sample Code_)

[comment]: <> (>>> ```python)

[comment]: <> (>>> from decat import decat)

[comment]: <> (>>> )

[comment]: <> (>>> )

[comment]: <> (>>> weird_text = '“AnyfoolcanwritecodethatacomputercanunderstandGoodprogrammerswritecodethathumanscanunderstand.”–MartinFowler')

[comment]: <> (>>> weird_text_simplified = decat&#40;weird_text&#41;)

[comment]: <> (>>> print&#40;weird_text_simplified&#41;)

[comment]: <> (>>>```)

[comment]: <> (>> #### _Console_)

[comment]: <> (>>> ['any', 'fool', 'can', 'write', 'code', 'that', 'a', 'computer', 'can',)

[comment]: <> ('understand', 'good', 'programmers', 'write', 'code', 'that', 'humans', 'can',)

[comment]: <> ('understand', 'martin', 'fowler'])

[comment]: <> (## Features)

[comment]: <> (>> 🪶 A light weight package, built around the features available in standard library)

[comment]: <> (>)

[comment]: <> (>> 📚 An ever-expanding vocabulary, knows more than 300K English words)

[comment]: <> (>)

[comment]: <> (>> 🪃 Simplistic design, allows for easy expansion to new languages and custom vocabulary sets)

[comment]: <> (## Dependencies)

[comment]: <> (> ⭕️ ___None___ 🎉)

[comment]: <> (## Limitations)

[comment]: <> (> ❗ Requires Python >= 3.6)

[comment]: <> (>)

[comment]: <> (> ❗ ️All input will be treated as lower-case)

[comment]: <> (>>```python)

[comment]: <> (>> >> ATitleCaseString --> ['a', 'title', 'case', 'string'])

[comment]: <> (>>```)

[comment]: <> (> ❗️ Punctuation marks, numbers and special characters will be stripped from the input and)

[comment]: <> (> will not be preserved in the output)

[comment]: <> (>>```python)

[comment]: <> (>> >>  dummy.email1234@gmail.com --> ['dummy', 'email', 'gmail', 'com'])

[comment]: <> (>>```)

[comment]: <> (>)

[comment]: <> (## Credits)

[comment]: <> (>> [Generic Human]&#40;https://stackoverflow.com/users/1515832/generic-human&#41;)

[comment]: <> (>)

[comment]: <> (>> [Rachael Tatman]&#40;https://www.kaggle.com/rtatman&#41;)

## License
> ### MIT
