# PDFPlay
```python
Watermark PDF files!
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

***PDFPlay*** is a Python package that aims to provide easy-to-use utilities to manipulate
PDF documents. Currently there's just one utility available, which is to "watermark" 
PDF files.

## Get Started
> ### Install it
>```python
>>> pip install pdf-play
>```

> ### Play With It
>```python
>>> watermark oto -t watermark text -i sample.pdf
>```

> ### Use It In Your Projects
> ```python
> from pdf_play import watermark
> 
> # set some variables
> wm_text = 'use this text as the watermark!'
> target_file = 'MyPC/Downloads/PDFFiles/sample.pdf'
> output_file = 'MyPC/Downloads/PDFFiles/sample_watermarked.pdf'
> font_name = 'Helvetica'
> font_size = 'medium'
> text_alignment = 'horizontal'
> 
> # call the watermark function
> watermark(wm_text, target_file, output_file, font_name=font_name, 
> font_size=font_size, text_alignment=text_alignment)
>```

## Features
>> 🍥 Provides easy-to-use functions to code against and a neat CLI to work directly in 
> your terminal.
>
>> 🀄️ Provides a bunch of configurable options with each command to set things just right.
> 
>> 🌈 Designed to be flexible, provides easy intergration for new commands & user-options.

## Dependencies
>> [PyPDF4 >= 1.27.0](https://pypi.org/project/PyPDF4/)
> 
>> [reportlab >= 3.6.1](https://pypi.org/project/reportlab/)
> 

## Limitations
>> ❗️ Requires [Python >= 3.6](https://python.org)
> 
>> ❗️ "watermark" is the only command available as of now.
> 

## Get Help
>> ```python
   >> pdf-play -h
>>```
>
>> ```python
   >> watermark -h
>>```
>

## License
> ### [MIT](https://raw.githubusercontent.com/sudoMode/PDFPlay/master/LICENSE)
