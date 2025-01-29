import google.generativeai as genai
import os
import datetime


API_KEY = os.environ["API_KEY"]
genai.configure(api_key=API_KEY)


OUTPUT_DIR = "docs/blog/posts/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to generate tech blog topics
def generate_blog_topic():
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "Generate a unique and interesting blog post topic about modern technology trends."
    
    response = model.generate_content(prompt)
    return response.text.strip() if response.text else None

# Function to generate blog content
def generate_blog_post(topic):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Write a detailed technical blog post about '{topic}' in Markdown format. Include code snippets if relevant."
    
    response = model.generate_content(prompt)
    return response.text.strip() if response.text else None


def format_title_for_filename(title):
    return title.replace(" ", "-").replace(",", "").replace("'", "").lower()

# Function to save the blog post
def save_blog_post(title, content):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Front matter
    front_matter = f"""---
date:
  created: {date_str}
title: "{title}"
---
"""

    filename = f"{OUTPUT_DIR}/{date_str}-{format_title_for_filename(title)}.md"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(front_matter + "\n" + content)
    
    print(f"Blog post saved: {filename}")


print("Generating blog topic...")
topic = generate_blog_topic()

if topic:
    print(f"Selected topic: {topic}")

    # Generate blog content
    print("Generating blog content...")
    content = generate_blog_post(topic)

    if content:
        save_blog_post(topic, content)
    else:
        print("Failed to generate blog content.")
else:
    print("Failed to generate a blog topic.")