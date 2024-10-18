import spacy
import re
import PyPDF2

nlp = spacy.load("en_core_web_sm")

# Đọc file CV
def read_cv_from_pdf(filename):
    with open(filename, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text

# Trích xuất kỹ năng từ CV
def extract_skills(cv_text):
    doc = nlp(cv_text)
    skills = []
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN": 
            skills.append(token.text)
    return set(skills)

def extract_skills(cv_text, output_file='skills_output.txt'):
    doc = nlp(cv_text)
    
    skills = []
    
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            skills.append(token.text)
    
    unique_skills = set(skills)
    
    # Lưu kỹ năng vào file
    with open(output_file, 'w', encoding='utf-8') as f:
        for skill in unique_skills:
            f.write(skill + '\n')  
    
    return unique_skills

cv_file = "cv.pdf"  
cv_text = read_cv_from_pdf(cv_file)

cv_skills = extract_skills(cv_text)
print(cv_skills)