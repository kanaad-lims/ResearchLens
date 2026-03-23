from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()


def validate_groq_api_key():
    """
    Validate that GROQ_API_KEY is set in environment.
    Required for Groq client initialization.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY environment variable not set mate!"
        )
    return api_key

def enhance_query(query: str):
    """
    Enhance the user query using an LLM to make it more effective for research paper retrieval.
    This could expand abbreviations, add relevant keywords, or rephrase for better search results.
    
    Requires GROQ_API_KEY environment variable to be set.
    """
    try:
        validate_groq_api_key()
        
        client = Groq()
        prompt = f"""
        You are a research query expansion assistant for academic paper retrieval.
        RULES:
        - Input may be casual or conversational — extract the core research intent first
        - Output ONLY 5-7 comma-separated technical keywords and short phrases
        - Do NOT explain, solve, or answer the query
        - Do NOT write sentences or paragraphs
        - Include: synonyms, related concepts, common acronyms, sub-domains

        Examples:
        Input: "I want to learn about how AI is being used in hospitals"
        Output: clinical AI, medical imaging, deep learning diagnostics, EHR, NLP clinical notes, patient outcome prediction, healthcare ML

        Input: "something about making LLMs faster and cheaper"
        Output: LLM inference optimization, model compression, quantization, knowledge distillation, efficient transformers, speculative decoding, pruning

        Input: "DL papers for finance"
        Output: deep learning, quantitative finance, stock market prediction, algorithmic trading, LSTM, portfolio optimization, time series forecasting

        Now enhance this query:
        Input: "{query}"
        Output:"""

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_completion_tokens=128,
            top_p=0.85,
            stream=False,
            stop=["<end>"]
        )
        enhanced_query = completion.choices[0].message.content.strip()
        return enhanced_query
    except ValueError as ve:
        # API key validation error
        print(f"Authentication Error: {ve}")
        raise
    except Exception as e:
        # Other API or request errors
        print(f"Query enhancement failed: {e}. \nFalling back to original query.")
        return query