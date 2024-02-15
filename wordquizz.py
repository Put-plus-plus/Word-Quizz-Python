import pandas as pd 
import numpy 
import logging
from googletrans import Translator  
from transliterate import translit  
from newspaper import Article
import queue
import threading
import random 
import tkinter as tk



class QuizzGlossary():

	def __init__(self, article_language_name, article_language_id):

		self.article_language_name = article_language_name
		self.article_language_id = article_language_id 
		self.launch_log() 
		self.create_glossary() 
		



	def launch_log(self):

		'''Launches an error log for the QuizzGlossary and QuizzWindow classes.'''

		self.logger = logging.getLogger(f'{self.article_language_id}_en_Logger')  
		self.logger.setLevel(logging.DEBUG)
		handler = logging.FileHandler(f'{self.article_language_id}_en_log.log')
		handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)




	def create_glossary(self):   

		'''Creates an empty pandas dataframe with three columns: a column for words (strings) in the article language, a column for the 
		article words transcribed (strings), and a column for the article words translated (strings) to English.'''

		try:
			self.glossary_df =  pd.DataFrame(columns = [self.article_language_name , 'transcribed', 'English'])   
		except:
			self.logger.exception(f'The {QuizzGlossary.create_glossary.__name__} method could not create a glosary.')  




	def extract_words_from_article(self, article_url):   

		'''Accepts the url (string) of an article. Returns a list with 50 unique words (strings) from the article.''' 

		try: 
			article = Article(article_url, language = self.article_language_id)   
			article.download()
			article.parse()
			title = article.title
			text = article.text 
			words = f'{title} {text}'
			words = words.split()
			words = [word.replace('"', '') for word in words]                                
			words = [word.strip('.,!?;()[]%:/-_0123456789') for word in words]      
			words = list(filter(None, words))                                                
			words = numpy.unique(words)             
			no_words = 50                                          
			words = words[:no_words]
			return(words)	   
		except:
			self.logger.exception(f'The {QuizzGlossary.extract_words_from_article.__name__} method could not extract a list of words from the article.')




	def add_word_to_glossary(self, word_queue):      

		'''Accepts a queue of article words (strings). A word eg Сонце (string), is transcribed eg sontse (string), and translated to 
		English eg sun (string). Finally, the word, its transcription, and its translation are added to the glosary (dataframe).'''

		try:
			while True:
				word = word_queue.get()   
				translator = Translator()
				word_transcribed = translit(word, self.article_language_id, reversed = True)                     
				word_translated = translator.translate(word, src = self.article_language_id, dest = 'en').text     
				glosary_entry = [word, word_transcribed, word_translated]
				self.glossary_df.loc[len(self.glossary_df)] = glosary_entry
				word_queue.task_done()
		except:
			self.logger.exception(f'The {QuizzGlossary.add_word_to_glossary.__name__} could not add a new word to the glossary.')




	def add_words_to_glossary_fast(self, article_url):   

		'''Accepts the url (string) of an article entered by the user into the GUI (QuizzWindow class). A list of words (strings)
		is created by calling extract_words_from_article(). The words are queued and added to the glossary (dataframe) by 
		calling add_word_to_glossary() in multiple threads.'''

		try:
			words = self.extract_words_from_article(article_url)
			no_threads = 5
			word_queue = queue.Queue()

			for n in range(no_threads):  
				t = threading.Thread(target=self.add_word_to_glossary, args=(word_queue,))    
				t.daemon = True
				t.start()

			for word in words:
				word_queue.put((word))

			word_queue.join()

		except:
			self.logger.exception(f'The {QuizzGlossary.add_words_to_glossary_fast.__name__} could not add new words to the glossary.')




	def select_word_from_glossary(self):   

		'''Returns an entry (row) from the glossary (dataframe) with an article word (string), the transcription of the word (string),
		and the translation of the word (string).'''

		try:
			random_index = random.randint(0, len(self.glossary_df)-1)       
			random_entry = self.glossary_df.iloc[[random_index]]     
			return(random_entry)                                        
		except:
			self.logger.exception(f'The {QuizzGlossary.select_word_from_glossary.__name__} could not select a random word from the glossary.')
		








class QuizzWindow():   

	def __init__(self, article_language_name, article_language_id):
		self.article_language_name = article_language_name
		self.article_language_id = article_language_id
		self.launch_log() 
		self.window = tk.Tk() 
		self.window.title('Word Quizz')                           
		self.window.geometry("850x450")                  
		self.bg_colour = 'lightgreen'       
		self.std_font = ('Segoe UI', 14)               
		self.bold_font = ('Segoe UI', 14, 'bold')
		self.std_font_colour = 'black'
		self.busy_font_colour = 'red'
		self.btn_colour = 'white' 
		self.btn_border = 1
		self.window.configure(bg = self.bg_colour)       
		self.launch_entry()
		self.launch_radiobutton()
		self.launch_label() 
		self.launch_button()
		self.window.mainloop()                                     
		



	def launch_log(self):   

		'''Launches an error log for the QuizzGlossary and QuizzWindow classes.'''

		self.logger = logging.getLogger(f'{self.article_language_id}_en_Logger')
		self.logger.setLevel(logging.DEBUG)
		handler = logging.FileHandler(f'{self.article_language_id}_en_log.log')
		handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)




	def launch_entry(self):

		'''Launches a tkinter entry widget that allows for the user to enter the url of an article.'''

		try:
			self.user_url_input = tk.Entry(self.window, width = 40)
			self.user_url_input.place(x = 250, y = 125)  

		except:
			self.logger.exception(f'The {QuizzWindow.launch_entry.__name__} could not launch entry widget.')




	def launch_radiobutton(self): 

		'''Launches tkinter radiobutton widgets that allow for the user to choose the setting of the word quizz, ie either the questions are in 
		English and the answers are in the article language, or the questions are in the article language and the answers are in English.'''

		try:
			en_to_article_txt = f'English to {self.article_language_name}'   
			article_to_en_txt = f'{self.article_language_name} to English'   
			self.user_language_choice = tk.IntVar(None, 1) 
			self.user_language_choice_btn1 = tk.Radiobutton(self.window, text = en_to_article_txt, bg = self.bg_colour, variable = self.user_language_choice, value = 1)
			self.user_language_choice_btn1.place(x = 220, y = 270) 
			self.user_language_choice_btn2 = tk.Radiobutton(self.window, text = article_to_en_txt, bg = self.bg_colour, variable = self.user_language_choice, value = 2)
			self.user_language_choice_btn2.place(x = 365, y = 270) 

		except:
			self.logger.exception(f'The {QuizzWindow.launch_radiobutton.__name__} could not launch radio button widgets.')




	def launch_label(self):   

		'''Launches tkinter label widgets that instruct the user how to use the word quizz, as well as a label widget that displays the questions and 
		answers of the word quizz.'''

		try:
			self.instruction_1_txt = f'''To create a Word Quizz with {self.article_language_name} words, \n enter the url of a {self.article_language_name} news article and click 'create quizz'!'''
			self.instruction_1_lbl = tk.Label(self.window, text = self.instruction_1_txt, bg = self.bg_colour, fg = self.std_font_colour, font = self.std_font)
			self.instruction_1_lbl.place(x = 150, y = 50) 

			self.instruction_2_txt = f'''To get started with your Word Quizz, select an option below and click 'next question'.\n You've got two seconds to think of the answer before it's displayed!'''
			self.instruction_2_lbl = tk.Label(self.window, text = self.instruction_2_txt, bg = self.bg_colour, fg = self.std_font_colour, font = self.std_font) 
			self.instruction_2_lbl.place(x = 75, y = 200) 

			self.display_word_quizz_lbl = tk.Label(self.window, text = '', bg = self.bg_colour, fg = self.std_font_colour, font = self.bold_font) 
			self.display_word_quizz_lbl.place(x = 300, y = 350)

		except:
			self.logger.exception(f'The {QuizzWindow.launch_label.__name__} could not launch label widgets.')




	def launch_button(self):

		'''Launches a tkinter button widget that allows for the user to create a word quizz, as well as a button widget for the user to ask for the next word of the word quizz to be displayed.'''

		try:
			self.create_word_quizz_btn = tk.Button(self.window, text = 'create quizz', bd = self.btn_border, bg = self.btn_colour, fg = self.std_font_colour, command=self.create_word_quizz)
			self.create_word_quizz_btn.place(x = 525, y = 125) 

			self.display_word_quizz_btn = tk.Button(self.window, text = 'next question', bd = self.btn_border, bg = self.btn_colour, fg = self.std_font_colour, command=self.display_word_quizz_question)
			self.display_word_quizz_btn.place(x = 525, y = 270)

		except:
			self.logger.exception(f'The {QuizzWindow.launch_button.__name__} could not launch button widgets.')




	def create_word_quizz(self):    

		'''Lets user create a word quizz by creating a QuizzGlossary object and calling QuizzGlossary.add_words_to_glossary_fast().'''

		try:
			# article_url = self.user_url_input.get()                                      
			self.quizz_glossary = QuizzGlossary(self.article_language_name, self.article_language_id)    
			self.quizz_glossary.add_words_to_glossary_fast(self.user_url_input.get())   
			self.user_url_input.delete(0, 'end')  
		except:
			self.display_word_quizz_lbl.configure(text = 'Sorry, something went wrong. Please try adding another article.')
			self.logger.exception(f'The {QuizzWindow.create_word_quizz.__name__} method could not be used by the user to create a word quizz.')




	def display_word_quizz_question(self): 

		'''Lets user ask for the next word of the word quizz to be displayed by calling QuizzGlossary.select_word_from_glossary(). Once the word has
		been displayed, there is a four second delay and then the answer is displayed by calling display_word_quizz_answer().'''

		try:
			glosary_entry = self.quizz_glossary.select_word_from_glossary()
			word = glosary_entry[self.article_language_name].to_string(index=False)
			word_transcribed = glosary_entry['transcribed'].to_string(index=False)
			word = f'{word} (transcribed: {word_transcribed})'
			word_translated = glosary_entry['English'].to_string(index=False)

			if self.user_language_choice.get() == 1: 
				question, answer = word_translated, word 

			if self.user_language_choice.get() == 2:
				question, answer = word, word_translated

			self.display_word_quizz_lbl.configure(text = f'What does {question} mean?')
			self.display_word_quizz_lbl.after(4000, lambda: self.display_word_quizz_answer(answer))

		except: 
			self.display_word_quizz_lbl.configure(text = 'Sorry, something went wrong.')
			self.logger.exception(f'The {QuizzWindow.display_word_quizz_question.__name__} method could not be used by the user to ask for the next word of the word quizz to be displayed.')




	def display_word_quizz_answer(self, answer): 

		'''Accepts the answer of a word quizz question (string) and displays the answer to the user.'''

		self.display_word_quizz_lbl.configure(text=f'It means {answer}', fg = self.busy_font_colour)







 