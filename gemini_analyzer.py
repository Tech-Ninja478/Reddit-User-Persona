# gemini_analyzer.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Limit content to ~6000 characters to stay within Gemini's input limits
def format_user_content(posts, comments, max_length=6000):
    content_blocks = []

    for p in posts:
        content_blocks.append(
            f"[Post in r/{p['subreddit']}]\nTitle: {p['title']}\nText: {p['text']}\nURL: {p['url']}\n"
        )

    for c in comments:
        content_blocks.append(
            f"[Comment in r/{c['subreddit']}]\n{c['text']}\nURL: {c['url']}\n"
        )

    full_text = "\n\n".join(content_blocks)
    return full_text[:max_length]

def get_gemini_persona(user_data):
    try:
        model = genai.GenerativeModel("models/gemini-2.5-pro")

        prompt = f"""
You are a behavioral analyst tasked with building a detailed user persona from Reddit activity.

Based on the posts and comments provided, generate a structured persona including:

1. **Age group** (e.g. 18-24, 25-34, etc.)
2. **Gender** (if determinable)
3. **Interests and hobbies**
4. **Personality traits**
5. **Writing style and tone**
6. **Political/social/worldview leanings**
7. **Possible profession or background**
8. **Top subreddits & what they imply**
9. **Any unique behavior patterns**
10. For each insight, include a short citation from the content (quote or URL).

User's Reddit activity:
{format_user_content(user_data['posts'], user_data['comments'])}
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"[ERROR] Gemini API call failed: {e}")
        return "Error generating persona."
