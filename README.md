# LitMT

This repo contains the instructions for how to reproduce the literary translation dataset from our paper "An Analysis of Literary Translation Style: Examining English Translations of Russian Classics" (Katsy, Vogler, Berg-Kirkpatrick).

We use the paragraph-level alignment method (par3)[https://github.com/katherinethai/par3] from ()"Exploring Document-Level Literary Machine Translation with Parallel Paragraphs from World Literature" (Thai et al., 2022))[[https://arxiv.org/pdf/2210.14250]] in our work.

## Code Breakdown + Instructions
### Dataset Creation + Paragraph Alignment
1. Obtaining Digital Books

Our dataset is composed of both non-copyrighted books (which can all be found in the **noncopyrighted_books** directory) and copyrighted translations which were purchased as Kindle books via Amazon. Links to the Kindle books on Amazon can be found in the file below.

*file:* [LitMT - Book List](https://docs.google.com/spreadsheets/d/1FgjpKv9vxqatny2Gryx_RLjGMwZ5EiJ8ugKAntYendQ/edit?usp=sharing)

2. Scanning Kindle Books with AppleScript

Download Kindle books on your Mac and open the book that you want to scan. Open `kindle_scanner.scpt` in your script editor and follow the instructions in the AppleScript file to get jpeg scans of the Kindle book pages.

*file:* `kindle_scanner.scpt`

3. OCR'ing Scans to Text

To get text out of the scanned jpeg pages, choose an OCR model of your choice. [We used Tesseract](https://github.com/tesseract-ocr/tesseract) for OCR; non fine-tuned tesseract produces text with some errors that need to be post-processed. Other options for OCR include [TrOCR](https://huggingface.co/docs/transformers/en/model_doc/trocr) and [docTR](https://github.com/mindee/doctr).

*file:* `ocr_pytesseract.py`

4. Google Translate translation of Source Text

In order to run alignment between the source and translation text, we need a Google Translate translation of the source text (Section 2.2 of the [par3 paper](https://arxiv.org/pdf/2210.14250)). This can be done through the GT API, which can be quite costly. An easier/free way is to use Google Spreadsheets for translation: copy/paste the entire book into a spreadsheet and use the `=GOOGLETRANSLATE(A2, "ru", "en")` cell command. An example is included below.

*file:* [GT Translation Example](https://docs.google.com/spreadsheets/d/1VAXqmaf_g9Y9V4qzbWQLNzIpgMnXADt-Z7U0fsXZhNw/edit?usp=sharing)

5. Text Alignment via Par3

To prepare for paragraph alignment organize create a directory for each book formatted in the following structure:
 ```
BookTitle_ru
├── src_txts
│   └── BookTitle_src.txt
└── trans_txts
    ├── BookTitle_gt.txt
    ├── BookTitle_Translator1.txt
    └── BookTitle_Translator2.txt
``` 
Pass the directory containing the book subdirectories into `run_alignment.ipynb`. Post-alignment you will get a pickle file in each book subdirectory containing the paragraph alignments. Follow the notebook instructions to re-organize the aligned data into one file containing alignments for all of the books in the dataset.

*file:* `run_alignment.ipynb`

6. Semantic Similarity Evaluation 

The quality of the paragraph alignments can be evaulated automatically using semantic similarity metrics: translations of the same source paragraph should contain the same semantic information regardless of wording. We looked at: 

- BLEU: [BLEU: a Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040.pdf)
- BERTScore: [BERTScore: Evaluating Text Generation with BERT](https://arxiv.org/pdf/1904.09675)
- BLEURT: [BLEURT: Learning Robust Metrics for Text Generation](https://arxiv.org/pdf/2004.04696)
- SIM score: [Beyond BLEU: Training Neural Machine Translation with Semantic Similarity](https://arxiv.org/pdf/1909.06694)

*file:* `alignment_eval.ipynb`

### Translation Classification
1. Experiment Dataset Generation 

Having aligned our book source and translated text and implemented paragraph sorting/filtering based on semantic similarity, we can now generate the train/val/test datasets for our translator classification experiments with multilingual-BERT. We holdout a couple books from the train dataset to create the val/test datasets; we choose the holdout books to maintain a reasonable train/val/test percentage and so that each translator is seen in both the train and holdout sets.

In our experiments we want to compare various input/data settings:
- Filtered vs unfiltered paragraph alignments - we hypothesize that removing poor alignments will improve translator classification performance.
- multilingual-BERT tokenization - we explore if passing the Russian source with its English translation improves performances compared to only passing just the English translated paragraph.

Code to perform the filtering and classification dataset generation is included in the jupyter notebook below.

*file:* `generate_exp_dataset.ipynb`

2. Running Classification 

Run translator classification with `run_classification.py` - update classification run settings in the python file. Run data is logged to wandb.

*file:* `scripts/run_classification.py`, `scripts/helpers.py`

### Figurative Language Analysis
1. Idiom Datasets 

For English idioms, we used the [MAGPIE corpus](https://github.com/hslh/magpie-corpus)
We compiled two Russian idiom lists found from sources on the web:
- Russian Contemporary Idioms: copied from one of the many lists of idioms on the web
- Russian Literary Idioms: We found a [list of idioms from Dostoevsky's *Crime and Punishment* created by a Belarusian school teacher](https://www.calameo.com/read/002288629daa1e5f14e61). No other corpus of its kind exists on the internet, as per our research. We manually copied the idioms to a text file. 

*files:* `idiom_datasets/ru_idioms.txt`, `idiom_datasets/dostoevsky_idioms.txt`

2. Idiom Exploration 

We performed automatic idiom identification on our aligned book dataset: we identified cases of both the English and Russian idioms within our dataset using rudimentary fuzzy matching. Identifying idioms within the source and translation allows us to explore how idioms were used in the source and translated literary works. 

*files:* fig_lang_id.ipynb

## Russian Literary Translation Resources

While creating our dataset, we researched and compiled all the existing English translations of major Russian literary works. Unfortunately, many of the translations are not digitally-available or easily-obtainable - however, perhaps that could change in the future. This data is available over the web but scattered throughout. 

Here is the complete, organized list that we compiled:[List of Translations of Major Russian Literary Works](https://docs.google.com/spreadsheets/d/1Fsw31_Gx6mfqb1bj26jXYAHsq2aHBykhDEf84foKYhc/edit?gid=0#gid=0)