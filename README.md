## Description 
A foreign language learning tool that quizzes you on the meaning of words extracted from a news article of choice. Consists of the QuizzGlossary Class and the graphical user interface QuizzWindow class. The `QuizzGlossary` class has a `launch_log()` method for launching an error log, an `create_glossary()` for creating an empty glossary, an `extract_words_from_article()` method for extracting words from a news article article, a `add_word_to_glossary()` method for adding an extracted word to the glossary (), an `add_words_to_glossary_fast()` method for adding multiple extracted words fast calling the other method, an and a `select_word_from_glossary()` method for selecting words from the glossary. The `QuizzWindow` class has a `launch_entry()` method, `launch_radiobutton()` method, `launch_label()` method, `launch_button()` and  `create_word_quizz()` method for creating a x from the user's input the url of a news article of interest, and a `display_word_quizz_question()` and `display_word_quizz_answer()`  method for allowng the user to interact and display the questions and answers. 

THIS TEXT HAS TO BE REVISED AS THE DESCRIPTION DO NOT MATCH CODE ENTIRELY. 

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

