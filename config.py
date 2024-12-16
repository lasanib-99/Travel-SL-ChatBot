# Configuration for API keys and constants

import os

# HF_API_KEY: Hugging Face API Key
HF_API_KEY = os.getenv("HF_TOKEN")

# MODEL_ID: Hugging Face model identifier for the Phi-3-mini-4k-instruct
MODEL_ID = "microsoft/Phi-3-mini-4k-instruct"

if HF_API_KEY is None:
    raise ValueError("Hugging Face API key is not found.. Please set the HF_TOKEN environment variable.")