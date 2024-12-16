# Travel-SL-Chatbot
A tourism Q&amp;A chatbot for Sri Lanka built using Streamlit and HuggingFace LLM

This is a simple chatbot built using **Streamlit** and **HuggingFace LLM** to provide travel recommendations and information about Sri Lanka. Users can ask questions like *"What are the best beaches in Sri Lanka?"* and receive tailored responses.

---

## Features
- **Accurate and tailored travel recommendations** for Sri Lanka.
- Built using **Streamlit** for the frontend interface.
- Leverages **HuggingFace LLM** for intelligent natural language processing.
- Lightweight and easy to deploy.

---

## Installation and Setup

Follow these steps to run the application locally:

### Prerequisites
Ensure you have the following installed:
1. **Python** (>=3.8)
2. **pip** (Python package manager)
3. **Git**

### Steps to Run the App

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/travel-sl-chatbot.git
   cd travel-sl-chatbot
2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate
   Or on Windows use: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Set up HuggingFace API key:
   Get a HuggingFace API key from HuggingFace.
   Set the environment variable in your terminal:
   export HF_TOKEN=your_huggingface_api_key
   Or on Windows, use:
   set HF_TOKEN=your_huggingface_api_key

5. Run the Streamlit app:
   streamlit run app.py

6. Open the local URL provided in the terminal (e.g., http://localhost:8501).

---

## Folder Structure
travel-sl-chatbot/
│
├── app.py                  # Streamlit application
├── chatbot.py              # LLM logic and response generation
├── config.py               # API key configuration
├── prompt.py               # Prompt template for HuggingFace LLM
├── utils.py                # Input validation utility
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

## Dependencies 🛠️
The project uses the following Python libraries:

1. Streamlit: For building the frontend UI.
2. LangChain: To structure the LLM pipeline.
3. HuggingFace Hub: To connect and use the LLM model.

Install them via:
  pip install streamlit langchain langchain-huggingface huggingface_hub

## Example Usage
1. Run the app locally.
2. Enter a question like:
"What are the best beaches in Sri Lanka?"
3. Receive a detailed response with travel tips and recommendations.
