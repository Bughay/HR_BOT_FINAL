### Later
# AI Interview Question Generator
## Overview

This Python-based AI agent generates personalized interview questions by analyzing a candidate's resume against specific job requirements. The system extracts information from PDFs, stores candidate data in SQLite, and uses advanced prompting techniques (Tree of Thought) to generate relevant interview questions.


## Features

    PDF Processing: Extracts text from resumes and job requirement documents

    Data Storage: Stores candidate information in SQLite database

    AI-Powered Question Generation: Uses LLMs to generate 10-15 tailored interview questions

    Modular OOP Design: Clean architecture for easy maintenance and extension

    Multi-LLM Support: Compatible with multiple language model providers

    LangSmith Support: Traces langchain functions and LLm calls through Langsmith

## Use Cases

The generated questions could be used to brain storm possible candidate questions, due to the projects clean architecture. it is fairly easy to customize Tree of Thought in order to manipulate the outputs as seen fit.


if you are a candidate you can use this bot to generate and practice possible interview questions. I suggest candidates update the Tree of thought prompts in order to maximize efficiency.

The bot also extracts information which is saved locally in the file as 'database.db' for later use of analysis. The schema can be found in Sqlite/schema.sql


## Projects file architecture
```
📦 AI-Interview-Question-Generator
├── 📂 OOP_classes
        - config.py 
        - database.py
        - extract.py
        - extractor_schemas.py
        - langsmith.py
        - models.py
        - questions_generator.py
        - test_mong_db.py
        - test_sql_alchemy.py
    ├── 📂 PDF
        - pdf_extractor.py
        - resume.pdf
        - requirements.pdf
    ├── 📂 sqlite
        - schema.sql
├── 📜 .env               # stores environment variables
│
├── 📜 main.py               # CLI entry point
├── 📜 mvp.py               # test easy mvp version.
├── 📜 README.md             # This documentation
├── 📜 requirements.txt      # Python dependencies
└── 📜 database.db           # SQLite database file

```

## Projects Modules

### OOP_classes/config.py
    Stores the following configuration variables which can easily be manipulated.
    Stores the Database url,file_paths and the prompts
### OOP_classes/database.py
    Stores classes incharge of calling the sqlite database and methods to save data in sqlite database
### OOP_classes/extract.py
    Stores algorithms used to extract data from the pdf file. (personal_info, skills, pastjobs) etc
    The classes are created so that they can easily take in the correct schemas based on what they need to extract
### OOP_classes/extractor_schemas.py
    Stores BaseModel classes which are then Inherited into the extracted classes.
## OOP_classes/langsmith.py
    Stores class that allows the program to be traced and evaluated through LangSmith
## OOP_classes/models.py
    Stores classes which can inherit majority of current LLM. Only Deepseek is currently as default
## OOP_classes/questions_generator.py
    Stores the main Tree of Thought algorithm which can be used to generate interview questions
## pdf/pdf_extractor
    extracts pdf 

## How to use

All the main functions are mentioned in the `main.py` file. simply run the file
However we will need to update 2 variables found in the OOP_classes/config.py file
(MUST BE PDF)
file_path_resume = 'fill the path to the resume here'
file_path_job_reqs = 'fill the path to the job description here'



## MVP version

you can try the mvp version which simply generates interview questions.
to do so, run the mvp.py file in the main directory


## BEWARE

the program is currently intended for local usage, it is not compatible with API calls or production for the reason that it is susceptible to SQL injection attacks, To avoid that we will update it to sql_alchemy and MongoDB in the future.

Also we will update raw SQL calls in a way that SQL injection attacks will not be possible.








