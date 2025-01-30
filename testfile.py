import hashlib
import re
from datetime import datetime

# Just a nonsense test file that'll get changed over time

def replace_time(text):
    utc_now = datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S UTC")
    
    def is_inside_quotes(index, text):
        in_single = in_double = False
        for i, char in enumerate(text):
            if char in "\"'" and (i == 0 or text[i-1] != '\\'):
                if char == '"': in_double = not in_double if not in_single else in_double
                if char == "'": in_single = not in_single if not in_double else in_single
            if i == index: return in_single or in_double
        return False

    return re.sub(r"<time>.*?</time>", lambda m: f"<time>{utc_now}</time>" if not is_inside_quotes(m.start(), text) else m.group(0), text)


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