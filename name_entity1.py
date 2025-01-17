import streamlit as st
import spacy
from spacy import displacy
#from urllib.error import URLError
import en_core_web_sm
from newspaper import Article
nlp = en_core_web_sm.load()
from pprint import pprint

st.title("Named Entity Recognizer (NER)")


inp = st.radio ("Choose Input Type:", ("Text", "URL"))

if inp == "Text":
    
    text = st.text_area("Enter a paragraph")
    # Disable link input if text is chosen
  
elif inp == "URL":
    
    link = st.text_input("Enter a URL")
    # Disable text area if URL is chosen



if st.button("Submit"):
    
    if text:
       doc = nlp(text)
       ent_html = displacy.render(doc, style="ent", jupyter=False)
    
       st.markdown(ent_html, unsafe_allow_html=True)
    elif link:
         article= Article(link)
         article.download()
         article.parse()
         #print("Fetched text:", article.text) 
         doc=nlp(article.text)
         ent_html = displacy.render(doc, style="ent", jupyter=False)
         st.markdown(ent_html, unsafe_allow_html=True)