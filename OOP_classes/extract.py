from langchain_core.prompts import ChatPromptTemplate
from OOP_classes.config import GENERATE_QUESTIONS_SYSTEM_PROMPT
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
class Extraction:
    def __init__(self,text:str,llm,schema):
        self.text = text
        self.llm = llm
        self.schema = schema

    def extract(self):
        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert extraction algorithm. "
                    "Only extract relevant information from the text. "
                    "If you do not know the value of an attribute asked to extract, "
                    "return null for the attribute's value.",
                ),
                
                ("human", "{text}"),
            ]
        )



        structured_llm = self.llm.with_structured_output(schema=self.schema)
        prompt = prompt_template.invoke({"text": self.text})
        result = structured_llm.invoke(prompt)



        return dict(result)
    

    
## This one is NON THINKINg,
class GenerateQuestions:
    def __init__(self,extracted_data,jobreqs,llm):
        self.extracted_data = extracted_data
        self.jobreqs = jobreqs
        self.llm = llm
    def generate_interview_questions(self):
        """
        Generate interview questions based on candidate data and job requirements  
        Args:
            extracted_data (dict): Dictionary containing candidate skills and experience
            job_requirements (str): String describing the job requirements
        
        Returns:
            str: Formatted interview questions
        """
        system_prompt = GENERATE_QUESTIONS_SYSTEM_PROMPT
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "Job Requirements:\n{requirements}"), 
            ("human", "Candidate Background:\n{input}")  
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "requirements": self.jobreqs,
            "input": str(self.extracted_data)
        })
        
        return response.content
    


        
 
 