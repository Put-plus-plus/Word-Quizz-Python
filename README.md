## Description 
When learning a foreign language, reading news articles can be a great way of building your vocabulary. THIS TEXT HAS TO BE REVISED AS THE NAMES AND DESCRIPTION DO NOT MATCH CODE ENTIRELY. 


Learning a foreign language can be a bit tricky, particularly scientific terminology used in that language. The user chooses a news article from BBC, that might be in a foreign language, interesting to learn but might not entirely comprehend all of the vocabulary.The project is a set of flashcards for learning a foreign language, with the user first choosing to be asked glossary in English or in the foreign language. Digital flashcards, that first ask you what I word means in a different language and then gives you the answer, is a convenient way of learning a foreign language. Asked in English, the answer appears in transcribed Ukra as well as in uk chyr letters, using tkinter, gogole trans, and transcribe. In python. Consisting of the Glosary Class and the Flashcards class. 

The `Glosary` class has an `initiate_glosary()` for creating an empty glossary, an `extract_words()` method for extracting words from a news article article, a `create_glosary()` method for adding the extracted words to the glossary (), and a `select_word()` method for selecting words from the glossary. The `Flashcards` class has a `create_flashcards()` method for creating a x from the user's input the url of a news article of interest, and a `display_flashcards()` method for allowng the user to interact and display the questions and answers. 

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

