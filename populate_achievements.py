
import os
import django
from django.core.files import File
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Achievement

# Directory containing achievements
ACHIEVEMENTS_DIR = Path('media/achievements')

# Clear existing achievements
Achievement.objects.all().delete()
print("Cleared existing achievements.")

# List of files to ignore
IGNORE = {'Oracle Architect_files'}

if not ACHIEVEMENTS_DIR.exists():
    print(f"Directory {ACHIEVEMENTS_DIR} does not exist.")
    exit()

def clean_title(filename):
    # Remove extension and underscores
    name = Path(filename).stem
    name = name.replace('_', ' ').replace('-', ' ')
    # Captalize words
    return name.title()

for item in ACHIEVEMENTS_DIR.iterdir():
    if item.name in IGNORE or item.is_dir():
        continue
    
    title = clean_title(item.name)
    print(f"Adding: {title}")
    
    # Create object
    ach = Achievement(title=title)
    
    # Open file and save to model
    # We copy the file logic or just point to it. 
    # Since they are already in media/achievements, and FieldFile won't move them if we set value manually, 
    # BUT Django's FileField usually expects to save a file which might duplicate it if we aren't careful.
    # To avoid duplication since they are ALREADY in the right folder, we can assign the relative path.
    
    relative_path = f"achievements/{item.name}"
    ach.file.name = relative_path
    ach.save()

print("Done populating achievements.")
