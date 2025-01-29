import re
from datetime import datetime

def replace_time(text):
    """Replaces <time>...</time> with <time>UTC time now</time>."""
    utc_now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")  # Get UTC timestamp
    
    # Regex to match <time>...</time>
    pattern = r"<time>.*?</time>"
    
    # Replace with updated timestamp
    return re.sub(pattern, f"<time>{utc_now}</time>", text)


with open("testfile.py", "r") as f:
    s = f.read()

with open("testfile.py", "w") as f:
    changed = replace_time(s)
    f.write(changed)