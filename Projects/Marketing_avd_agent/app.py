import streamlit as st
import os
import io
import re
import markdown
import pdfkit
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq

# Load environment variables
load_dotenv(override=True)

# Helper to check for API keys
def check_api_key(key_name):
    key = os.getenv(key_name)
    return key if key else None

# Run prompt on available models
def run_prompt_on_available_models(prompt):
    results = {}
    api_response = [{"role": "user", "content": prompt}]
    
    if check_api_key('GOOGLE_API_KEY'):
        try:
            model_name = "gemini-2.0-flash"
            google_api_key = os.getenv('GOOGLE_API_KEY')
            gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
            response = gemini.chat.completions.create(model=model_name, messages=api_response)
            results[model_name] = response.choices[0].message.content
            print(f"✓ Got response from {model_name}")
        except Exception as e:
            print(f"⚠️ Error with {model_name}: {str(e)}")

        try:
            model_name = "gemini-2.5-flash-preview-04-17"
            response = gemini.chat.completions.create(model=model_name, messages=api_response)
            results[model_name] = response.choices[0].message.content
            print(f"✓ Got response from {model_name}")
        except Exception as e:
            print(f"⚠️ Error with {model_name}: {str(e)}")

    if check_api_key('GROQ_API_KEY'):
        groq_api_key = os.getenv('GROQ_API_KEY')
        groq = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")
        for model_name in ["llama-3.3-70b-versatile", "deepseek-r1-distill-llama-70b", "qwen-qwq-32b"]:
            try:
                response = groq.chat.completions.create(model=model_name, messages=api_response)
                results[model_name] = response.choices[0].message.content
                print(f"✓ Got response from {model_name}")
            except Exception as e:
                print(f"⚠️ Error with {model_name}: {str(e)}")
    
    if not results:
        print("⚠️ No models were able to provide a response")
    
    return results

# PDF generation using pdfkit
def create_pdf(content):
    # Convert markdown-like input to HTML using markdown package
    html_body = markdown.markdown(content)

    html_template = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            h1 {{ font-size: 18px; color: #2c3e50; }}
            h2 {{ font-size: 16px; color: #34495e; }}
            p {{ font-size: 12px; color: #333; line-height: 1.5; }}
            ul {{ margin-left: 20px; }}
            li {{ margin-bottom: 6px; }}
            body {{ font-family: Arial, sans-serif; padding: 30px; }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    # Convert HTML to PDF using pdfkit
    pdf_bytes = pdfkit.from_string(html_template, False)
    return io.BytesIO(pdf_bytes)

# Streamlit UI
st.title("Marketing & Advertising Strategy Generator")

with st.form("marketing_form"):
    product_description = st.text_area("Product Description", "A subscription-based meditation app with guided sessions, sleep stories, and mood tracking.")
    marketing_objective = st.text_input("Marketing Objective", "Increase app downloads by 20% over the next quarter")
    promotion_platform = st.text_input("Promotion Platform", "Instagram")
    submitted = st.form_submit_button("Generate Strategy")

if submitted:
    prompt = f"""
You are a Marketing and Advertising Specialist with expertise in product positioning, target audience analysis, and campaign strategy.

Given the following information:

Product/Service Description:
{product_description}

Marketing Objective:
{marketing_objective}

Platform/Medium for Promotion:
{promotion_platform}

Please provide a comprehensive marketing strategy covering the following:

1. **Target Audience Fit (Rating 1-10)**
2. **Unique Value Proposition (UVP)**
3. **Ad Copy Hook**
4. **Top Marketing Message**
5. **Visual/Creative Direction**
6. **Emotional Appeal Strategy**
7. **Call-to-Action (CTA)**
8. **Notable Risk/Challenge**
9. **A/B Test Ideas**
10. **Complementary Channels**
"""

    st.markdown("### Generating responses from AI models...")
    results = run_prompt_on_available_models(prompt)

    # Create a synthesis prompt
    synthesis_prompt = "Here are the responses from different models:\n"
    for index, (model, response) in enumerate(results.items()):
        synthesis_prompt += f"\n--- Response {index+1} ---\n{response}\n"

    synthesis_prompt += """
Please synthesize these responses into one comprehensive answer that:
1. Captures the best insights from each response
2. Resolves any contradictions between responses
3. Presents a clear and coherent final answer
4. Maintains the same format as the original responses (numbered list format)
5. Compiles all additional places mentioned by all models

Your synthesized response:
"""

    # Synthesize using Groq
    synthesized_answer = ""
    if check_api_key('GROQ_API_KEY'):
        try:
            groq = Groq()
            synthesis_response = groq.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role": "user", "content": synthesis_prompt}]
            )
            synthesized_answer = synthesis_response.choices[0].message.content
            print("✓ Successfully synthesized responses with llama-4-scout-17b-16e-instruct")
        except Exception as e:
            print(f"⚠️ Error synthesizing responses: {str(e)}")
    else:
        print("⚠️ GROQ API key not available")

    # Display synthesized answer
    if synthesized_answer:
        st.markdown("### Synthesized Strategy")
        st.markdown(synthesized_answer)

        # Download synthesized strategy as PDF
        pdf_bytes = create_pdf(synthesized_answer)
        st.download_button(
            label="Download Synthesized Answer as PDF",
            data=pdf_bytes,
            file_name="marketing_strategy.pdf",
            mime="application/pdf"
        )

    # PDF download for individual model responses
    for model, response in results.items():
        pdf_bytes = create_pdf(response)
        st.download_button(
            label=f"Download {model} Response as PDF",
            data=pdf_bytes,
            file_name=f"{model}_marketing_strategy.pdf",
            mime="application/pdf"
        )
