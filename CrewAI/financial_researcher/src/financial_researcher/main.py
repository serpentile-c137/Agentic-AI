#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher
import os
from dotenv import load_dotenv

load_dotenv(override=True)

import os

# Check if API keys are set
required_keys = ["GEMINI_API_KEY", "GROQ_API_KEY", "SERPER_API_KEY"]
for key in required_keys:
    if os.getenv(key):
        print(f"✅ {key} is set")
    else:
        print(f"❌ {key} is not set")

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'company': 'Tesla'
    }
    
    try:
        result = FinancialResearcher().crew().kickoff(inputs=inputs)
        print(result.raw)
        print(f"Research completed successfully. Output saved to: output/report.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()