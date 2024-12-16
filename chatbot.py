# LLM logic and response generation

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from config import HF_API_KEY, MODEL_ID
from prompt import TOURISM_PROMPT
import re
import logging

# Initialize the Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id = MODEL_ID,
    huggingfacehub_api_token = HF_API_KEY,
    temperature = 0.3,
    max_length = 100,   
)

# Logging for exception handling in the response
logging.basicConfig(level = logging.ERROR)

# Create the LangChain chain (a prompt template with the user's question)
prompt_template = PromptTemplate(template = TOURISM_PROMPT, input_variables = ["user_question"])
llm_chain = LLMChain(llm = llm, prompt = prompt_template)

# Create the sequence of prompt and LLM
prompt_sequence = prompt_template | llm

# Define a funtion to get the response
def get_response(user_question: str) -> str:
    # Generate a response for the given user question

    try:
        # Generate and return the response
        response = prompt_sequence.invoke({"user_question": user_question}).strip()

        # Manually remove any text after defined stop words or tokens to clean output
        stops = ["User Question:", "Answer:", "\n"]
        for stop in stops:
            response = response.split(stop)[0].strip()

        # Remove markdown formatting and excess line breaks
        cleaned_response = re.sub(r"^\*\*.*?\*\*:", "", response).strip()
        cleaned_response = re.sub(r"\n+", " ", cleaned_response)
        
        return cleaned_response        
    
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return "Sorry, something went wrong!"