from PyPDF2 import PdfReader
from OOP_classes.config import file_path_resume,file_path_job_reqs


def pdf_extractor(file_path):
    reader = PdfReader(file_path)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text


text = pdf_extractor(file_path_resume)

job_reqs = pdf_extractor(file_path_job_reqs)