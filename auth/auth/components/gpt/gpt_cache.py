# gpt/gpt_cache.py

import openai
import os
import hashlib
import json


CACHE_DIR = "gpt_cache"
os.makedirs(CACHE_DIR, exist_ok=True)


def _hash_prompt(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def _cache_path(prompt: str) -> str:
    return os.path.join(CACHE_DIR, _hash_prompt(prompt) + ".json")


def gpt_response_with_cache(prompt: str, model="gpt-3.5-turbo") -> str:
    cache_file = _cache_path(prompt)

    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)["response"]

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result_text = response["choices"][0]["message"]["content"]

    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump({"prompt": prompt, "response": result_text}, f, ensure_ascii=False, indent=2)

    return result_text
