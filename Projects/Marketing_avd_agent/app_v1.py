# streamlit_app.py

import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq
import io
from fpdf import FPDF

# Load environment variables
load_dotenv(override=True)

# Marketing and advertising
# prompt = f"""
# You are a Marketing and Advertising Specialist with expertise in product positioning, target audience analysis, and campaign strategy.

# Given the following information:

# Product/Service Description:
# {product_description}


# Marketing Objective (e.g., increase awareness, boost conversions, promote launch):
# {marketing_objective}

# Platform/Medium for Promotion (e.g., Instagram, Email, YouTube, Google Ads):
# {promotion_platform}

# Please provide a comprehensive marketing strategy covering the following:

# 1. **Target Audience Fit (Rating 1-10)**: How well does this product/service match the given target audience?
# 2. **Unique Value Proposition (UVP)**: A single, compelling sentence that summarizes why this product is uniquely valuable to this audience.
# 3. **Ad Copy Hook**: A short, engaging headline or hook (under 20 words) tailored to the specified promotion platform.
# 4. **Top Marketing Message**: A persuasive paragraph (~2-3 sentences) to be used in the core message or description of the product.
# 5. **Visual/Creative Direction**: Specific creative suggestions (e.g., imagery, tone, design elements) suitable for the platform.
# 6. **Emotional Appeal Strategy**: What emotions should the campaign evoke and how?
# 7. **Call-to-Action (CTA)**: A strong, action-oriented sentence customized to the platform and objective.
# 8. **Notable Risk/Challenge**: One potential obstacle in marketing this to the given audience and how to overcome it.
# 9. **A/B Test Ideas**: Suggest two variations for testing to optimize performance (e.g., copy vs. image, long-form vs. short-form).
# 10. **Complementary Channels**: Two additional marketing channels or platforms that could support the campaign effectively.

# Be concise but insightful. Provide real value as a creative marketing consultant.
# """


# Helper to check for API keys
def check_api_key(key_name):
    key = os.getenv(key_name)
    return key if key else None

# Run prompt on available models
def run_prompt_on_available_models(prompt):
    """
    Run a prompt on all available AI models based on API keys.
    Continues processing even if some models fail.
    """
    results = {}
    api_response = [{"role": "user", "content": prompt}]
     
    # Google
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
       
    if check_api_key('GOOGLE_API_KEY'):
        try:
            model_name = "gemini-2.5-flash-preview-04-17"
            google_api_key = os.getenv('GOOGLE_API_KEY')
            gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
            response = gemini.chat.completions.create(model=model_name, messages=api_response)
            results[model_name] = response.choices[0].message.content
            print(f"✓ Got response from {model_name}")
        except Exception as e:
            print(f"⚠️ Error with {model_name}: {str(e)}")

    # Groq
    if check_api_key('GROQ_API_KEY'):
        try:
            model_name = "llama-3.3-70b-versatile"
            groq_api_key = os.getenv('GROQ_API_KEY')
            groq = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")
            response = groq.chat.completions.create(model=model_name, messages=api_response)
            results[model_name] = response.choices[0].message.content
            print(f"✓ Got response from {model_name}")
        except Exception as e:
            print(f"⚠️ Error with {model_name}: {str(e)}")

    if check_api_key('GROQ_API_KEY'):
        try:
            model_name = "deepseek-r1-distill-llama-70b"
            groq_api_key = os.getenv('GROQ_API_KEY')
            groq = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")
            response = groq.chat.completions.create(model=model_name, messages=api_response)
            results[model_name] = response.choices[0].message.content
            print(f"✓ Got response from {model_name}")
        except Exception as e:
            print(f"⚠️ Error with {model_name}: {str(e)}")

    if check_api_key('GROQ_API_KEY'):
        try:
            model_name = "qwen-qwq-32b"
            groq_api_key = os.getenv('GROQ_API_KEY')
            groq = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")
            response = groq.chat.completions.create(model=model_name, messages=api_response)
            results[model_name] = response.choices[0].message.content
            print(f"✓ Got response from {model_name}")
        except Exception as e:
            print(f"⚠️ Error with {model_name}: {str(e)}")
    
    # Check if we got any responses
    if not results:
        print("⚠️ No models were able to provide a response")
    
    return results

# Get responses from all available models
# model_responses = run_prompt_on_available_models(prompt)

# Display the results
# for model, answer in model_responses.items():
#     display(Markdown(f"## Response from {model}\n\n{answer}"))

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
    synthesis_prompt = f"""
    Here are the responses from different models:
    """

    # Add each model's response to the synthesis prompt without mentioning model names
    for index, (model, response) in enumerate(results.items()):
        synthesis_prompt += f"\n--- Response {index+1} ---\n{response}\n"

    synthesis_prompt += """
    Please synthesize these responses into one comprehensive answer that:
    1. Captures the best insights from each response
    2. Resolves any contradictions between responses
    3. Presents a clear and coherent final answer
    4. Maintains the same format as the original responses (numbered list format)
    5.Compiles all additional places mentioned by all models 

    Your synthesized response:
    """

    # Create the synthesis
    if check_api_key('GROQ_API_KEY'):
        try:
            groq = Groq()
            synthesis_response = groq.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role": "user", "content": synthesis_prompt}]
            )
            synthesized_answer = synthesis_response.choices[0].message.content
            print("✓ Successfully synthesized responses with llama-4-scout-17b-16e-instruct")
            
            # Display the synthesized answer
            # display(Markdown("## Synthesized Answer\n\n" + synthesized_answer))
        except Exception as e:
            print(f"⚠️ Error synthesizing responses with llama-4-scout-17b-16e-instruct: {str(e)}")
    else:
        print("⚠️ Groq API key not available, cannot synthesize responses")

    for model, response in results.items():
        # st.subheader(f"Response from {model}")
        st.markdown(synthesized_answer)

    # def create_pdf(text):
    #     pdf = FPDF()
    #     pdf.add_page()
    #     pdf.set_auto_page_break(auto=True, margin=15)
    #     pdf.set_font("Arial", size=12)
    #     for line in text.split('\n'):
    #         pdf.multi_cell(0, 10, line)
    #     pdf_output = io.BytesIO()
    #     pdf.output(pdf_output)
    #     pdf_output.seek(0)
    #     return pdf_output

    def create_pdf(text):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Add a Unicode-compatible font
        font_path = "DejaVuSans.ttf"
        if not os.path.exists(font_path):
            raise FileNotFoundError("DejaVuSans.ttf not found. Download it and place it in the app directory.")

        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", size=12)

        for line in text.split('\n'):
            pdf.multi_cell(0, 10, line)

        pdf_output = io.BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)
        return pdf_output

    if 'synthesized_answer' in locals() and synthesized_answer:
        pdf_bytes = create_pdf(synthesized_answer)
        st.download_button(
            label="Download Synthesized Answer as PDF",
            data=pdf_bytes,
            file_name="marketing_strategy.pdf",
            mime="application/pdf"
        )

    # Add download PDF button for each individual model response
    for model, response in results.items():
        pdf_bytes = create_pdf(response)
        st.download_button(
            label=f"Download {model} Response as PDF",
            data=pdf_bytes,
            file_name=f"{model}_marketing_strategy.pdf",
            mime="application/pdf"
        )