# LitMT

## Motivation

### Problems in MT

- training models for complex, multi-sentence translation
- language translation doesn't have a one-to-one relationship: there is not one right answer. there is an element of style that generic translation misses out on. staying true to the original source material in a way beyond just semantics and grammatics. miss pragmatics, style, word choice, etc.
- translating on a larger scale: context matters beyond the sentence-level unit. looking at sentence-by-sentence, we lose meaning.
- hard to get expert-level, high-quality training data as it is, where do we get such data for this?

### Our Solution

- leverage an already-existing data source: literary translations and their translations
- literary works often with inherently complex language and meaning on the source side
- many classicial literary works have many translations into the target language. different translations strive to emphasize different elements of the source work in the target language: preserving meaning in the target language, preserving style, grammatical and stylitic choice, transferring the over-arching meaning of the work to the target-language reader.

### Ultimate Goal
- controllable machine translation: produce translation which emphasis on specific stylistic choices/needs
- contributing to digital humanities: introduce methods to obtain literary data, legally and more efficiently
- deeper dive into human translation analysis: perform machine exploration of how translations of different translations differ, capture and analyze stylistic differences that would be difficult to catch manually
- contribute dataset, dense in both num of translations per literary work and num of translations per translation, which is necessary for training a model for controllable mt and for more extensive data exploration

## Obtaining Parallel Literary Data

### Challenges
- good idea, but not without roadblocks
- some works have many translations, but not all of them are available in a digital format. some are scanned but not OCR'd into text, others scattered across private university library collections. with research find those that exist, but finding the actual translations is a task in itself, not always feasible
- copyright laws: many, sometimes most, of the translations fall under copyright restrictions. obtaining data might be difficult - can't copy and paste. you need to do it legally - not using illegal document databases. need work arounds to get text since can't copy and paste existing scanned documents + legally acquired translations.
- some languages have more translations than others. the most translations exist with english as the target language due to the english-centricity of the world at the moment. source language distribution depends on how difficult source translated to target - harder challenge, more people translated in attempt to do it "better"; historical factors like popularity of authors, works, cultural exchange of literary works between different languages, ideological and cultural movements, popularity of source language and amount of literary works produced in it, etc.

### Choosing Source Language, Literary Works, Authors
- wanted to get source language with most available data: most translated books and most translations per book, books with same original authors to distinguish author style style from translator styles
- our choice: russian-to-english literary translation, high density of translations per literary work - up to 15 translations into english of works of Dostoevsky (though not all available digitally). popularity of many russian authors in english-speaking society since introduction into the mainstream literary world in the early-20th century, complexity of translating languages with very different grammatical rules and permissible syntactic flexibility - very flexible slavic to inflexible english. also, one member of team is a native speaker of russian and english, more insight into original text versus translations.
- obviously want works with the most available digital translations, but don't want all translations of every book - that's a long list with sparsity of translator data. created a translator-book matrix to identify which works by which authors have recurring translators - chose the more dense books + authors + translators
- result is the following dataset matrix: 
- (insert figure here)

## Scanning Kindle Books via Apple Scripts (and fine-tuned OCR - TODO)

- first step, getting text data in consistent format and legally. oldest mainstream translation available free online on Gutenberg project. some non-copyrighted but not-mainstream translations available on other site - have to do a internet search dive. But most digital translations are copy-righted books - want a legal way to obtain. Not all but a number are available on amazon as kindle books.
- purchase kindle books, cannot copy-paste book, so need to scan it. our work-around: download kindle books on computer, and run apple script automation to get png scans of each page of the books.
- then run tesseract ocr to get the book text from the png scanned files
- #TODO: fine-tune tesseract ocr on kindle fonts bc kindle books have specific font choices for their books and tesseract doesn't inherently deal well with the kindle fonts, so ocr produces a number of mistakes
- need to do some manual formatting editting after getting the digit texts, so chapter/paragraphs separations are clean in the book text - inconsistent formatting book-by-book which is difficult to handle via ocr model fine-tuning. this is important to be able to align the books to map the parallel paragraphs in the translations.

## Aligning Book Translations with Par3
- use existing paragraph-level alignment method introduced by Karpinsi et al - par3
- (summarize how par3 works here)

## Evaluating Paragraph-Level Alignments
- BLEU, BLERT, BERT_Score, SIM score
- (include some examples)

## Running Classification with mBERT
### Generating Train/Test Data
### Filtering vs No Filtering
### Aligned vs Non-Aligned
### Results
### Comparison with SVM
### Takeaway

## Idiom Dive
- EPIE corpus
- Dostoevksy Literary Idioms
- Modern vs Literary Idioms

## Style Transfer and Controllable MT
- #TODO

## How to Reproduce Dataset
1. Kindle Books + Apple Scripts
2. Tesseract OCR to text
3. Text Alignment

