from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from OOP_classes.config import q_chain_prompt_1,q_chain_prompt_2,q_chain_prompt_3,q_chain_prompt_4

class InterviewGenerator:
    def __init__(self,llm,resume,job_reqs):
        self.llm = llm
        self.resume = resume
        self.job_reqs = job_reqs
        self.chain = self.execute_chain()


    def execute_chain(self):

        prompt_1 = PromptTemplate(
            input_variables=['test_resume', 'test_job_description'],
            template = q_chain_prompt_1
        #     template="""
        # You are an expert interviewer. Based on the following job description and candidate profile, 
        # list 5-7 key areas to evaluate during an interview.

        # Job Description:
        # {test_job_description}

        # Candidate Profile:
        # {test_resume}

        # Return the areas as a bullet list.
        # """
        )

        prompt_2 = PromptTemplate(
            input_variables=['test_resume', 'test_job_description', 'output_1'],
            template = q_chain_prompt_2
        #     template="""
        # You are preparing a job interview. Based on these evaluation areas:

        # {output_1}

        # Create 2-3 interview questions for each area using the following job description and candidate profile.

        # Job Description:
        # {test_job_description}

        # Candidate Profile:
        # {test_resume}
        # """
        )

        prompt_3 = PromptTemplate(
            input_variables=['output_2', 'test_job_description'],
            template = q_chain_prompt_3
        #     template="""
        # You are a hiring manager. Evaluate the following interview questions based on relevance, insightfulness, and uniqueness. 
        # Score each from 1 to 5 and provide a brief justification for low scores.

        # Job Description:
        # {test_job_description}

        # Questions:
        # {output_2}
        # """
        )

        prompt_4 = PromptTemplate(
            input_variables=['output_3'],
            template = q_chain_prompt_4
        #     template="""
        # You are finalizing an interview. From the evaluated questions below, select the best 10-15 questions. 
        # Ensure a variety of question types and that the set is well-balanced. Rewrite if needed.

        # Evaluated Questions:
        # {output_3}
        # """
        )

        chain_1 = (
            RunnablePassthrough()
            | prompt_1
            | self.llm
            | StrOutputParser()
        )

        chain_2 = (
            RunnablePassthrough()
            | {
                "test_resume": RunnablePassthrough(),
                "test_job_description": RunnablePassthrough(),
                "output_1": RunnablePassthrough()
            }
            | prompt_2
            | self.llm
            | StrOutputParser()
        )

        chain_3 = (
            RunnablePassthrough()
            | {
                "output_2": RunnablePassthrough(),
                "test_job_description": RunnablePassthrough()
            }
            | prompt_3
            | self.llm
            | StrOutputParser()
        )

        chain_4 = (
            RunnablePassthrough()
            | prompt_4
            | self.llm
            | StrOutputParser()
        )

        full_chain = (
            RunnablePassthrough.assign(output_1=chain_1)
            .assign(output_2=chain_2)
            .assign(output_3=chain_3)
            .assign(output_4=chain_4)
            .with_config(run_name="InterviewQuestionPipeline")
        )

        result = full_chain.invoke({
            "test_resume": self.resume,
            "test_job_description": self.job_reqs
        })

        return result['output_4']