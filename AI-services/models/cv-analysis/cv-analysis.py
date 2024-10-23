import spacy
import re
import PyPDF2

nlp = spacy.load("en_core_web_sm")

# Đọc file CV từ PDF
def read_cv_from_pdf(filename):
    with open(filename, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text

# Hàm tiền xử lý văn bản 
def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', text) 
    text = text.strip().lower() 
    return text

# Sử dụng NER để trích xuất kỹ năng từ CV
def extract_skills_ner(cv_text):
    doc = nlp(cv_text)
    skills = []
    
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT"] or ent.root.pos_ == "PROPN":
            skills.append(ent.text)
    print(skills)
    return set(skills)

# Hàm trích xuất kỹ năng dựa trên từ khóa kỹ năng đã định sẵn
def extract_skills_keywords(cv_text):
    keywords = [
    # Ngôn ngữ lập trình
    "python", "java", "javascript", "c++", "c#", "php", "ruby", "swift", "kotlin", "typescript", 
    "go", "r", "scala", "rust", "perl", "matlab", "bash", "shell",
    
    # Phát triển web
    # Frontend
    "html", "css", "javascript", "typescript", "react", "angular", "vue.js", "bootstrap", "jquery", 
    "sass", "less",
    # Backend
    "node.js", "django", "flask", "express.js", "ruby on rails", "asp.net", "spring boot", 
    "laravel", "php", ".net core",
    
    # Cơ sở dữ liệu
    "mysql", "postgresql", "mongodb", "sqlite", "oracle", "microsoft sql server", "redis", 
    "cassandra", "couchdb", "mariadb", "dynamodb", "firebase realtime database", "elasticsearch",
    
    # Quản lý phiên bản và CI/CD
    "git", "github", "gitlab", "bitbucket", "jenkins", "travis ci", "circleci", "bamboo", 
    "docker", "kubernetes",
    
    # Công cụ DevOps và hạ tầng
    "aws", "amazon web services", "azure", "google cloud platform", "gcp", "terraform", "ansible", 
    "puppet", "chef", "vagrant", "nginx", "apache", "ci/cd pipelines", "jenkins", "gitops",
    
    # Phát triển ứng dụng di động
    "android development", "ios development", "react native", "flutter", "xamarin", "swift", 
    "kotlin", "java", "objective-c", "ionic",
    
    # Trí tuệ nhân tạo & Học máy
    "machine learning", "deep learning", "tensorflow", "pytorch", "scikit-learn", "keras", "opencv", 
    "nlp", "natural language processing", "nltk", "spacy", "reinforcement learning", 
    "computer vision", "data mining", "neural networks",
    
    # Dữ liệu lớn và phân tích
    "hadoop", "spark", "apache kafka", "hive", "pig", "hbase", "apache flink", "dask", "presto", 
    "bigquery", "data warehousing", "etl", "extract, transform, load", "data lakes",
    
    # Bảo mật thông tin
    "cybersecurity", "ethical hacking", "penetration testing", "firewall", "ids", "ips", 
    "intrusion detection system", "intrusion prevention system", "siem", 
    "security information and event management", "ssl", "tls", "vpn", "owasp", 
    "security auditing", "encryption", "malware analysis",
    
    # Cloud Computing
    "amazon web services", "aws", "microsoft azure", "google cloud platform", "gcp", "openstack", 
    "cloudformation", "lambda", "aws lambda", "cloud functions", "gcp cloud functions", 
    "elastic beanstalk", "heroku", "digitalocean", "serverless",
    
    # Hệ điều hành
    "linux", "unix", "windows server", "macos", "red hat", "centos", "ubuntu", "debian", "freebsd",
    
    # Công cụ kiểm thử
    "selenium", "junit", "mockito", "postman", "soapui", "cypress", "testng", "appium", 
    "loadrunner", "jmeter",
    
    # Kỹ năng mềm liên quan IT
    "agile", "scrum", "kanban", "project management", "technical writing", "code reviews", 
    "pair programming", "tdd", "test-driven development", "bdd", "behavior-driven development", 
    "problem solving", "communication skills",
    
    # Blockchain và công nghệ sổ cái phân tán
    "blockchain", "ethereum", "hyperledger", "smart contracts", "solidity", "bitcoin", 
    "cryptography", "consensus algorithms", "dapps", "decentralized applications",
    
    # IoT (Internet of Things)
    "arduino", "raspberry pi", "mqtt", "zigbee", "lorawan", "embedded systems", "sensor networks", 
    "m2m communication", "edge computing", "mqtt brokers",
    
    # Các kỹ năng phát triển phần mềm khác
    "api development", "restful services", "graphql", "microservices", "websockets", "webrtc", 
    "openapi", "swagger", "soap", "message queues", "rabbitmq", "kafka"
]

    
    # Xử lý văn bản trước khi tìm kiếm từ khóa
    processed_text = preprocess_text(cv_text)
    
    skills = set()
    for keyword in keywords:
        if keyword in processed_text:
            skills.add(keyword)
    
    return skills

def extract_skills(cv_text, output_file='skills_output.txt'):
    preprocessed_cv_text = preprocess_text(cv_text)
    
    ner_skills = extract_skills_ner(preprocessed_cv_text)
    
    keyword_skills = extract_skills_keywords(preprocessed_cv_text)
    
    all_skills = ner_skills.union(keyword_skills)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for skill in all_skills:
            f.write(skill + '\n')  
    
    return all_skills

cv_file = "cv.pdf"
cv_text = read_cv_from_pdf(cv_file)

cv_skills = extract_skills(cv_text)
