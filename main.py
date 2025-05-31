from OOP_classes.extract import *
from OOP_classes.models import llm
from OOP_classes.extractor_schemas import *
from OOP_classes.questions_generator import InterviewGenerator
from pdf import text, job_reqs
def main():

    run = InterviewGenerator(llm,text,job_reqs).chain
    questions_extractor = Extraction(run,llm,QuestionExtractor)

    print(run)
    extracted_dict = questions_extractor.extract()
    print(extracted_dict)


if __name__ == "__main__":
    main()


# extractor = Extraction(text,llm,Department_extractor)
# extractor_2 = Extraction(text,llm,PersonalInfoExtractor)
# extractor_3 = Extraction(text,llm,SkillsJobHistoryExtractor)
# result = extractor.extract()
# result_2 = extractor_2.extract()
# result_3 = extractor_3.extract()
# result_t = {'technical_stack': ['Microsoft Office Suite'], 'non_technical_skills': ['Analytical thinking and planning', 'Strong verbal and personal communication skills', 'Accuracy and attention to details', 'Organization and prioritization skills', 'Problem analysis', 'Use of judgment and ability to solve problems efficiently', 'Strong administrative and time management skills', 'Ability to maintain confidentiality', 'Enthusiastic', 'Flexible', 'Capable of working on own initiative'], 'past_jobs': [PastJob(company='BCD Travel Russia (JSC Aeroclub)', role='Senior Sales Manager'), PastJob(company='Indian Embassy Moscow', role='Marketing Assistant/ Translator at Economic and Commercial Wing'), PastJob(company='LLC “Caudalie”', role='Assistant to Finance and Marketing'), PastJob(company='Delegation of European Union to Russian Federation', role='Financial Assistant at the Press and Information Section'), PastJob(company='British Embassy Moscow', role='Locally Engaged Entry Clearance Assistant'), PastJob(company='Nakheel Marketing and Advertising Services', role='Assistant to General Manager /Marketing Manager'), PastJob(company='Zain Sudan (Telecom)', role='Trainee in the IT Department'), PastJob(company='Zain Sudan (Telecom)', role='Trainee in the Marketing Department')]}


# run = InterviewGenerator(llm,text,job_reqs).chain
# questions_extractor = Extraction(text,job_reqs,SkillsJobHistoryExtractor)
# result = questions_extractor.extract()
# print(run)

# print(questions_extractor)