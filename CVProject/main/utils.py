from django.template.loader import render_to_string
import pdfkit
from main.models import CV
import openai
import os
import json


def generate_cv_pdf(cv: CV) -> bytes:
    html = render_to_string("cv_pdf.html", {"cv": cv})
    pdf = pdfkit.from_string(html, False)
    return pdf


def translate_cv_content(cv: CV, target_language: str) -> dict:
    """
    Translate CV content to the specified language using OpenAI.
    Returns a dictionary with translated content.
    """
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    content_to_translate = {
        "firstname": cv.firstname,
        "lastname": cv.lastname,
        "bio": cv.bio,
        "skills": cv.skills,
        "projects": cv.projects,
        "contacts": cv.contacts,
    }

    prompt = f"""
    Translate the following CV content to {target_language}. 
    Return the result as a JSON object with the same structure.
    Only translate the text content, keep the structure and keys the same.
    
    Content to translate:
    {content_to_translate}
    
    Return only the JSON object, no additional text.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional translator. Translate the given CV content to the specified language while maintaining the JSON structure.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )

        translated_content = response.choices[0].message.content.strip()

        return json.loads(translated_content), True

    except Exception as e:
        print(f"Translation error: {e}")
        return content_to_translate, False
