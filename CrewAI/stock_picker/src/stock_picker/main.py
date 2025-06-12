#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
import os
from stock_picker.crew import StockPicker
from dotenv import load_dotenv

load_dotenv(override=True)



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
    Run the research crew.
    """
    inputs = {
        'sector': 'Technology',
        # "current_date": str(datetime.now())
    }

    # Create and run the crew
    result = StockPicker().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)


if __name__ == "__main__":
    run()
