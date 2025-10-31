import pdfplumber
import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    doc = nlp(text)
    name = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    emails = re.findall(r'\S+@\S+', text)
    skills = re.findall(r'\b(Python|Java|C\+\+|SQL|HTML|CSS|JavaScript|Machine Learning|Data Science)\b', text, re.I)
    
    return {
        "Name": name[0] if name else "Not Found",
        "Email": emails[0] if emails else "Not Found",
        "Skills": list(set(skills))
    }
