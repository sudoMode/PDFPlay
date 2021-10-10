# PDFPlay
```python
some tag line
```
---

![made-with-python](images/made-with-python.svg)
![built-with-<3](images/built-with-love.svg)
![open-source](images/open-source.svg)
![powered-by-coffee](images/powered-by-coffee.svg)

<p align="center">
    <a href="#">
        <img src="https://forthebadge.com/images/badges/made-with-python.svg"/>
    </a>
    <a href="#">
        <img src="https://forthebadge.com/images/badges/powered-by-coffee.svg"/>
    </a>
    <a href="#">
        <img src="https://forthebadge.com/images/badges/open-source.svg"/>
    </a>
    <a href="#">
        <img src="https://forthebadge.com/images/badges/built-with-love.svg"/>
    </a>
</p>

---

[comment]: <> (badges 2)

[comment]: <> (<p align="center">)

[comment]: <> (    <a href="https://www.codefactor.io/repository/github/sudomode/decat">)

[comment]: <> (        <img src="https://img.shields.io/codefactor/grade/github/sudomode/decat/master?style=for-the-badge"/>)

[comment]: <> (    </a>)

[comment]: <> (    <a href="#">)

[comment]: <> (        <img src="https://img.shields.io/github/v/release/sudomode/decat?style=for-the-badge"/>)

[comment]: <> (    </a>)

[comment]: <> (    <a href="#">)

[comment]: <> (        <img src="https://img.shields.io/github/languages/code-size/sudomode/decat?style=for-the-badge"/>)

[comment]: <> (    </a>)

[comment]: <> (    <a href="#">)

[comment]: <> (        <img src="https://img.shields.io/github/license/sudomode/decat?color=rgb%28100%2C%20150%2C%20150%29&style=for-the-badge"/>)

[comment]: <> (    </a>)

[comment]: <> (</p>)

---


[comment]: <> (Into)

[comment]: <> (***Decat*** is a Python package capable of de-concatenating strings that do not have)

[comment]: <> (white-spaces in them, or in other words, it allows the user to infer spaces)

[comment]: <> (programmatically. This is a simple utility that comes in handy with various modern)

[comment]: <> (Natural Language Processing&#40;NLP&#41; tasks such as cleaning, exploration or even manipulation)

[comment]: <> (of text. [Zipf's Law]&#40;https://en.wikipedia.org/wiki/Zipf%27s_law&#41; is)

[comment]: <> (at the)

[comment]: <> (core of this)

[comment]: <> (project, the aim is to provide an easy interface for programmers to extract meaningful)

[comment]: <> (information out of deformed pieces of texts.)


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
