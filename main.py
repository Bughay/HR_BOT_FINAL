from OOP_classes.extract import *
from OOP_classes.models import llm
from OOP_classes.extractor_schemas import *
from OOP_classes.questions_generator import InterviewGenerator
from OOP_classes.database import *
from OOP_classes.config import DATABASE_URL
from pdf.pdf_extractor import text, job_reqs
from OOP_classes.langsmith import LangSmithInitiation
def main():
    ##### THE PRINT IS ONLY INPUT IN ORDER TO TEST THROUGHT THE COMMAND LINE, DELETE IT AND TEST THROUGH LANGSMITH
    LangSmithInitiation.langsmith_trace()
    db = Database(DATABASE_URL)
    print('----------------------------------------')
    print('Generating interview questions!.')
    print('----------------------------------------')
    llm_answer = InterviewGenerator(llm,text,job_reqs).chain
    print(llm_answer)
    print('Interview Generator completed.')
    print('----------------------------------------')
    print('Extracting Personal Info')
    print('----------------------------------------')
    personal_info_extractor = Extraction(text,llm,PersonalInfoExtractor).extract()
    print(personal_info_extractor)
    print('Personal Info successfully extracted')
    print('----------------------------------------')
    print('Extracting Department Info')
    print('----------------------------------------')
    department_extractor = Extraction(text,llm,Department_extractor).extract()
    print(department_extractor)
    print('Department Info successfully extracted')
    print('----------------------------------------')
    print('Extracting Skills Info')
    print('----------------------------------------')
    skills_extractor = Extraction(text,llm,SkillsJobHistoryExtractor).extract()
    print(skills_extractor)
    print('Skills Info successfully extracted')
    print('----------------------------------------')
    print('Extracting questions Info')
    print('----------------------------------------')
    questions_extractor = Extraction(llm_answer,llm,QuestionExtractor).extract()
    print(questions_extractor)
    print('questions  Info successfully extracted')
    print('----------------------------------------')
    print('Extracting past jobs Info')
    print('----------------------------------------')
    past_extractor = Extraction(text,llm,PastJobs).extract()
    print(personal_info_extractor)
    print('past job Info successfully extracted')




    columns = ['users','department','skills','questions','pastjobs']
    print('----------------------------------------')
    print('Saving to database Personal Info')
    print('----------------------------------------')
    personal_script = Sqlscripts(columns[0],personal_info_extractor).save_personal()
    department_script = Sqlscripts(columns[1],department_extractor).save_personal()
    skills_script = Sqlscripts(columns[2],skills_extractor).save_personal()
    questions_script = Sqlscripts(columns[3],questions_extractor).save_personal()
    past_script = Sqlscripts(columns[4],past_extractor).save_personal()

    

    db.execute_script(personal_script)
    db.execute_script(department_script)
    db.execute_script(skills_script)
    db.execute_script(questions_script)
    db.execute_script(past_script)
    db.close_script()
    print('data has been succesfully extracted and saved!')


if __name__ == "__main__":
    main()


