# LitMT

## KK TODO
- Clean up files:
    * [x] kindle_scanner.scpt
    * [x] ocr_pytesseract.py
    * [x] run_alignment.ipynb
    * [x] alignment_eval.ipynb
    * [x] generate_exp_dataset.ipynb
    * [x] exp_dataset_eval.ipynb
    * [x] fig_lang_id.ipynb
    * [ ] classification notebooks
    * [ ] scripts
    
- Data polishing:
    * [ ] Consolidate aligned book data
    * [ ] Clean up Dostoevsky literary idiom list
    * [ ] Polish modern Russian idiom list

- Github Site
    * [ ] Motivation
    * [ ] Obtaining Parallel Literary Data
    * [ ] Aligning Book Translations with Par3
    * [ ] Evaluating Paragraph-Level Alignments
    * [ ] Running Classification with mBERT
    * [ ] Idiom Dive
    * [ ] Style Transfer
    * [ ] Controllable MT
    * [ ] Code Breakdown + Instructions


## Code Breakdown + Instructions
### Dataset Creation + Paragraph Alignment
1. Kindle Books + Apple Scripts //
*file:* kindle_scanner.scpt
2. OCR'ing Scans to Text //
*file:* ocr_pytesseract.py
3. Google Translate Source Text
4. Text Alignment via Par3 //
*file:* run_alignment.ipynb
5. Semantic Similarity Evaluation //
*file:* alignment_eval.ipynb

### Translation Classification
1. Experiment Dataset Generation //
*file:* generate_exp_dataset.ipynb
2. Running Classification //
*file:* scripts/run_classification.py

### Figurative Language Analysis
1. Idiom Datasets //
*files:* ru_idioms.txt, dostoevsky_idioms.txt
2. Idiom Exploration //
*files:* fig_lang_id.ipynb
