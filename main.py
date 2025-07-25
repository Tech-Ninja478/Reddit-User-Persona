# main.py
import argparse
from reddit_scraper import extract_username_from_url, get_user_data
from gemini_analyzer import get_gemini_persona
from pdf_generator import save_persona_as_pdf
import json
import os

def save_raw_data(user_data):
    os.makedirs("output", exist_ok=True)
    path = f"output/{user_data['username']}_raw.json"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, indent=2)
    print(f"[✓] Raw user data saved to: {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reddit Persona Generator")
    parser.add_argument("profile_url", help="Reddit user profile URL")
    args = parser.parse_args()

    username = extract_username_from_url(args.profile_url)
    print(f"[~] Fetching data for user: {username}")
    user_data = get_user_data(username)
    save_raw_data(user_data)

    print(f"[~] Generating persona using Gemini...")
    persona_text = get_gemini_persona(user_data)

    # Save persona text
    persona_path = f"output/{username}_persona.txt"
    with open(persona_path, "w", encoding="utf-8") as f:
        f.write(persona_text)

    print(f"[✓] Persona saved to {persona_path}")

    # Save PDF version
    save_persona_as_pdf(username, f"output/{username}_persona.txt")
