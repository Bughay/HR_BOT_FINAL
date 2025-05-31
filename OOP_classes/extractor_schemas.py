from typing import Optional, List
from pydantic import BaseModel, Field

class PersonalInfoExtractor(BaseModel):  # Changed class name to follow PEP8
    """Information about a person's personal details."""

    first_name: str = Field(description='The first_name of the person')
    last_name: str = Field(description='The last_name of the person')
    date_of_birth: Optional[str] = Field(  # Now optional
        description='The person\'s date of birth, when they were born',
        default=None  # Explicitly set default to None
        )
    education: Optional[str] = Field(  # Now optional
        description='What type of education does the person have? E.g., Computer Science, Mathematics, etc.',
        default=None  # Explicitly set default to None
        )
    country: Optional[str] = Field(
        description='Which country is the person from, prioritize their passport but if you cant find it then place of birth. E.g Russian Federation, Italy',
        default=None
    )


class Department_extractor(BaseModel):
    """Information about a which department the person works in."""


    department: str = Field(description="""The most relevant department for the candidate based on their resume. Strictly choose only one of the four options. Rules:\n- 'IT': If the resume contains technical skills (e.g., programming, AI, cloud computing, cybersecurity, data analysis, IT infrastructure) or roles like Software Engineer, Data Scientist, DevOps, etc.\n- 'Sales': If the resume emphasizes revenue generation, business development, account management, or metrics like 'increased sales by X%'. Common roles: Sales Executive, Account Manager, BDR.\n- 'Customer Support': If the resume focuses on client service, helpdesk, troubleshooting, or customer success. Common roles: Support Agent, CSR, Helpdesk Technician.\n- 'Legal': If the resume includes law-related experience (e.g., contracts, compliance, litigation, corporate law) or qualifications like JD, LLB, or paralegal certification.""",
    enum=['IT','Sales'])





class PastJob(BaseModel):
    """Information about a past job position."""
    company: str = Field(description="Name of the company (e.g., Microsoft, Google)")
    role: str = Field(description="Brief description of what they did (e.g., 'Frontend Development', 'Sales Manager')")


class SkillsJobHistoryExtractor(BaseModel):
    """Extracted information about skills and job history."""
    technical_stack: List[str] = Field(
        description="List of technical skills (e.g., Python, SQL, React, AWS). Extract all relevant tools, languages, and frameworks.",
        default = 'no technical skills',
    )
    non_technical_skills: List[str] = Field(
        description="List of soft skills (e.g., Communication, Leadership, Sales). Include non-technical abilities.",
        default_factory=list
    )
    past_jobs: List[PastJob] = Field(
        description="List of previous jobs with company name and role description.",
        default_factory=list
    )

class ExtractorData(BaseModel):
    extractor: SkillsJobHistoryExtractor


class QuestionExtractor(BaseModel):
    questions: List[str] = Field(
        description="List of extracted questions, each ending with '?",
    )


    
