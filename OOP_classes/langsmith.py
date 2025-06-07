from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DEEPSEEK_API')
trace_key = os.getenv('LANGSMITH_API')


class LangSmithInitiation:

    def langsmith_trace():
            os.environ["LANGCHAIN_TRACING_V2"] = "true"  
            os.environ["LANGCHAIN_API_KEY"] = trace_key
            os.environ["LANGCHAIN_PROJECT"] = "HR_BOT"  

            os.environ["DEEPSEEK_API_KEY"] = api_key