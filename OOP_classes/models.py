from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DEEPSEEK_API')

class LLMConfig:
    def __init__(self, model: str, temperature: float, max_tokens: int, 
                 api_key: str, timeout: int = None, max_retries: int = 2):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries

class LLM:
    def __init__(self, llm_provider,config: LLMConfig ):
 
        self.config = config
        self.model = llm_provider(
            model=config.model,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            api_key=config.api_key,
            timeout=config.timeout,
            max_retries=config.max_retries
        )

    def get_llm(self):
        return self.model
    

llm_config = LLMConfig(
    model="deepseek-chat",
    temperature=0,
    max_tokens=2000,
    api_key=api_key
)

llm = LLM(ChatDeepSeek,llm_config).get_llm()





