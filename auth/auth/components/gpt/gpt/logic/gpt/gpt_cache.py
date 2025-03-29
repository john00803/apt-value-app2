# gpt/gpt_cache.py

import openai
import hashlib
import os

CACHE_DIR = ".gpt_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_path(prompt: str) -> str:
    key = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{key}.txt")

def gpt_run_with_cache(prompt: str) -> str:
    cache_path = get_cache_path(prompt)
    
    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message["content"].strip()

    with open(cache_path, "w", encoding="utf-8") as f:
        f.write(result)

    return result
