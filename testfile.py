import hashlib
import re
from datetime import datetime

# Just a nonsense test file that'll get changed over time

def replace_time(text):
    """Replaces <time>29-01-2025 09:25:55 UTC</time> with <time>29-01-2025 09:25:55 UTC</time>."""
    utc_now = datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S UTC")
    pattern = r"<time>29-01-2025 09:25:55 UTC</time>"
    
    return re.sub(pattern, f"<time>29-01-2025 09:25:55 UTC</time>", text)

def get_sha256(file_path):
    """Returns the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


with open("testfile.py", "r") as f:
    s = f.read()

with open("testfile.py", "w") as f:
    changed = replace_time(s)
    f.write(changed)
    print("Time updated")

with open("hash.txt", "w") as f:
    h = get_sha256(__file__)
    f.write(str(h))
    print("Hash written")

# The last time this was updated was <time>29-01-2025 09:25:55 UTC</time>

print("Test complete")