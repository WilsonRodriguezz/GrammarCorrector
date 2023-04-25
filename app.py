##Import the nltk library 
import nltk
##import the language_tool_python library
import language_tool_python
##Required library
nltk.download('averaged_perceptron_tagger')
##Required library
nltk.download('words')
from flask import Flask, render_template, request
nltk.download('punkt')
app = Flask(__name__, template_folder='./template')

##Function
def correct_grammar(text):

    tool = language_tool_python.LanguageTool('en-US')
  
    sentences = nltk.sent_tokenize(text)

    corrected_sentences = []
  
    for sentence in sentences:
       
        corrected_sentence = tool.correct(sentence)
 
        corrected_words = nltk.word_tokenize(corrected_sentence)
       
        corrected_sentences.append(corrected_words)
   
    corrected_text = ' '.join([' '.join(words) for words in corrected_sentences])
  
    return corrected_text
    

##Routing    
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text = correct_grammar(text)
        return render_template('index.html', text=text, corrected_text=corrected_text)
    return render_template('index.html')