DATABASE_URL = 'database.db'

file_path_resume = 'pdf/mark_resume.pdf'
file_path_job_reqs = 'pdf/requirements.pdf'


##this is for future, to add encapsulation which will allow to switch from different databases (e.g choose to save in sql or mongodb)
THINKING = True
WHICH_DATABASE = 'sqlite3'

GENERATE_QUESTIONS_SYSTEM_PROMPT = """You are an interview question generator. 
        Create exactly:
        - 5 technical questions about how the candidate's skills match the job
        - 5 behavioral questions about their work experience
        
        The questions should specifically assess fit for the position described.
        
        Format cleanly with two sections:
        
        Technical Questions:
        1. Question...
        2. Question...
        
        Behavioral Questions:
        1. Question...
        2. Question..."""

q_chain_prompt_1 = """
        You are an expert interviewer. Based on the following job description and candidate profile, 
        list 5-7 key areas to evaluate during an interview.

        Job Description:
        {test_job_description}

        Candidate Profile:
        {test_resume}

        Return the areas as a bullet list.
        """

q_chain_prompt_2 = """
        You are preparing a job interview. Based on these evaluation areas:

        {output_1}

        Create 2-3 interview questions for each area using the following job description and candidate profile.

        Job Description:
        {test_job_description}

        Candidate Profile:
        {test_resume}
        """

q_chain_prompt_3 = """
        You are a hiring manager. Evaluate the following interview questions based on relevance, insightfulness, and uniqueness. 
        Score each from 1 to 5 and provide a brief justification for low scores.

        Job Description:
        {test_job_description}

        Questions:
        {output_2}
        """

q_chain_prompt_4 = """
        You are finalizing an interview. From the evaluated questions below, select the best 10-15 questions. 
        Ensure a variety of question types and that the set is well-balanced. Rewrite if needed.

        Evaluated Questions:
        {output_3}
        """



