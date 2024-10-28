import sys, fitz
import spacy
import csv

fname = 'Uploaded_Resumes/CV2.pdf'
doc = fitz.open(fname)

# doc = [page for page in doc]
# print(doc)

text = ""
for page in doc:
    text = text + str(page.get_text())

text = text.strip()
text = ' '.join(text.split())

model_path = "D:\Workspace\job-cv-ai\AI-services\models\cv-parser\model-best"
nlp = spacy.load(model_path)
doc = nlp(text)

with open("extracted_cv_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Ghi header cho file CSV
    writer.writerow(["Entity", "Label"])

    # Ghi từng entity và nhãn của nó vào file CSV
    for ent in doc.ents:
        writer.writerow([ent.text, ent.label_])

print("Data has been saved to extracted_cv_data.csv")