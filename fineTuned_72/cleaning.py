from bs4 import BeautifulSoup
import re
from SIH.Model_without_fineTune.translate import translated

def cleaning(text):
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(r'[^\w\s]', '', text)


cleaned_text= cleaning(translated)