import pandas as pd
from googletrans import Translator

# Đọc file CSV
df = pd.read_csv("D:\Workspace\job-cv-ai\AI-services\data\job_listings.csv", delimiter='\t')
print(df.head())
# Khởi tạo bộ dịch tự động (Google Translator)
translator = Translator()

# Dịch các mô tả công việc sang tiếng Anh nếu cần
def translate_job_description(description):
    try:
        translated = translator.translate(description, src='vi', dest='en')
        return translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return description

# Dịch các mô tả công việc tiếng Việt sang tiếng Anh
df['Job_Description_Translated'] = df['ProjectDescription'].apply(translate_job_description)

