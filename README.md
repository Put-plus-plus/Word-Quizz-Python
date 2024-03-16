## Description 
A foreign language learning tool that quizzes you on the meaning of words extracted from a news article of your choice. Consists of the `QuizzGlossary` class that holds the glossary, and the `QuizzWindow` class that holds the graphical user interface. The `QuizzGlossary` class has a `launch_log()` method for launching an error log, a `create_glossary()` for creating an empty glossary; an `extract_words_from_article()` method for extracting words from a news article, an `add_word_to_glossary()` method for adding an extracted word and its translation to the glossary, an `add_words_to_glossary_fast()` method for adding words fast by calling `add_word_to_glossary()` in multiple threads, and a `select_word_from_glossary()` method for selecting words from the glossary for the user to be quizzed on. The `QuizzWindow` class has `launch_entry()`, `launch_radiobutton()`, `launch_label()`, and `launch_button()` for launching widgets for user interaction. If the user inputs the url of a news article of choice and interacts with a button widget, the `create_word_quizz()` method is called to create a Word Quizz. If the user then interacts with the radiobutton widgets and a button widget, the `display_word_quizz_question()` method is called to display a word, and the `display_word_quizz_answer()` method is called to display the meaning of the word after a four second delay to give the user time to think of the answer. 

## Dependencies 
* Microsoft Windows 10.0.19045
* Python 3.9.1
* pandas 1.2.2, numpy 1.22.2, logging 0.5.1.2, googletrans 4.0.0-rc.1, transliterate 1.10.2, newspaper 0.2.8, queue (built-in), threading (built-in), random (built-in), tkinter (built-in) 

## Execution - word quizz example  
```python
from wordquizz import *

bbc_article_language_name = 'Ukrainian'
bbc_article_language_id = 'uk'    
QuizzWindow(bbc_article_language_name, bbc_article_language_id)

# enter into GUI: https://www.bbc.com/ukrainian/features-66562788
```
 
## Animation - word quizz example
https://github.com/Put-plus-plus/Word-Quizz-Python/assets/153921921/dad9689f-094c-442f-b042-451beb4cd966

