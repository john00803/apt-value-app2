# logic/auto_analysis.py

import openai
from gpt.gpt_cache import gpt_run_with_cache
from gpt.make_prompt import make_prompt

def analyze_apartment(apt_name: str, apt_data: dict) -> str:
    prompt = make_prompt(apt_name, apt_data)
    return gpt_run_with_cache(prompt)
