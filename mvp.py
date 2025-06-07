from OOP_classes.extract import *
from OOP_classes.models import llm
from OOP_classes.extractor_schemas import *
from OOP_classes.questions_generator import InterviewGenerator
from pdf.pdf_extractor import text, job_reqs
from OOP_classes.langsmith import LangSmithInitiation
def main():
    LangSmithInitiation.langsmith_trace()

    llm_answer = InterviewGenerator(llm,text,job_reqs).chain

    print('----------------------------------------')
    questions_extractor = Extraction(llm_answer,llm,QuestionExtractor).extract()
    print(questions_extractor)
    questions = questions_extractor['questions']
    print(questions)
    for index,question in enumerate(questions,1):
        print(index)
        print(question)
    print('!!!!!program completed!!!!!!!')
if __name__ == "__main__":
    main()


