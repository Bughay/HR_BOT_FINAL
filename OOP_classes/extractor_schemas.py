from typing import Optional, List
from pydantic import BaseModel, Field

class PersonalInfoExtractor(BaseModel): 
    """Information about a person's personal details."""

    first_name: str = Field(description='The first_name of the person')
    last_name: str = Field(description='The last_name of the person')
    date_of_birth: Optional[str] = Field(  
        description='The person\'s date of birth, when they were born',
        default=None  
        )
    education: Optional[str] = Field(  
        description='What type of education does the person have? E.g., Computer Science, Mathematics, etc.',
        default=None 
        )
    country: Optional[str] = Field(
        description='Which country is the person from, prioritize their passport but if you cant find it then place of birth. E.g Russian Federation, Italy',
        default=None
    )


class Department_extractor(BaseModel):
    """Information about a which department the person works in."""


    department: str = Field(description="""The most relevant department for the candidate based on their resume. Strictly choose only one of the four options. Rules:\n- 'IT': If the resume contains technical skills (e.g., programming, AI, cloud computing, cybersecurity, data analysis, IT infrastructure) or roles like Software Engineer, Data Scientist, DevOps, etc.\n- 'Sales': If the resume emphasizes revenue generation, business development, account management, or metrics like 'increased sales by X%'. Common roles: Sales Executive, Account Manager, BDR.\n- 'Customer Support': If the resume focuses on client service, helpdesk, troubleshooting, or customer success. Common roles: Support Agent, CSR, Helpdesk Technician.\n- 'Legal': If the resume includes law-related experience (e.g., contracts, compliance, litigation, corporate law) or qualifications like JD, LLB, or paralegal certification.""",
    enum=['IT','Sales'])





class PastJobs(BaseModel):
    """Information about a past job position."""
    company: List[str] = Field(description="Name of the company (e.g., Microsoft, Google)")
    position: List[str] = Field(description="Brief description of what they did (e.g., 'Frontend Development', 'Sales Manager')")


class SkillsJobHistoryExtractor(BaseModel):
    """Extracted information about skills and job history."""
    technical_skills: List[str] = Field(
        description="List of technical skills (e.g., Python, SQL, React, AWS). Extract all relevant tools, languages, and frameworks.",
        default = 'no technical skills',
    )
    non_technical_skills: List[str] = Field(
        description="List of soft skills (e.g., Communication, Leadership, Sales). Include non-technical abilities.",
        default = 'no soft skills'
    )
    






class QuestionExtractor(BaseModel):
    questions: List[str] = Field(
        description="List of extracted questions, each ending with '?",
        default = None
    )




### DONE IT WORKED BUT I WILL KEEP THE BELOW CODE TO REMIND MYSELF HOW BAD IT WAS
## -------------------------------------------------------------------------------------------------------
# WE CAN ADJUST THE FUNCTIONS TO HAVE ALL THE QUESTIONS STORED HERE AS A LIST AND THEN EXTRACT THAT LIST 
## -------------------------------------------------------------------------------------------------------
# class QuestionExtractor(BaseModel):
#     "extract questions 1 to 15"
#     q_1: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_2: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_3: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_4: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_5: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_6: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_7: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_8: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_9: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_10: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_11: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_12: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_13: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_14: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
#     q_15: str = Field(
#         description="Extracted question, ending with '?'",
#         default=None
#     )
