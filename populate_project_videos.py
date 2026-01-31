
import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Project

VIDEO_DIR = Path('media/websites')
PROJECT_MAPPING = {
    'Jodhana Trip Advisor.webm': 'Jodhana Tourism',
    'Home _ Desi Potato Post.webm': 'Desi Potato Post',
    'Home _ Rent As Buddy.webm': 'Rent As Buddy',
    'Vendor Management System.webm': 'Vendor Management System',
    'Home - My Portfolio.webm': 'Personal Portfolio',
    'Bimsu.webm': 'Bimsu App',
    'Dashboard.webm': 'Analytics Dashboard',
    'ME-website.webm': 'ME Website',
    'Mine-Info.webm': 'Mine Info Platform'
}

# Create a mapping for existing projects to avoid duplicates if titles differ slightly
existing_projects = {p.title.lower(): p for p in Project.objects.all()}

if not VIDEO_DIR.exists():
    print("Video directory not found.")
    exit()

for video_file in VIDEO_DIR.iterdir():
    if video_file.name not in PROJECT_MAPPING:
        print(f"Skipping unknown video: {video_file.name}")
        continue
        
    target_title = PROJECT_MAPPING[video_file.name]
    video_rel_path = f"websites/{video_file.name}"
    
    # Check if project exists
    project = existing_projects.get(target_title.lower())
    
    if project:
        print(f"Updating video for existing project: {project.title}")
        project.video.name = video_rel_path
        project.save()
    else:
        print(f"Creating new project: {target_title}")
        project = Project.objects.create(
            title=target_title,
            description="A comprehensive web application demonstrating full-stack capabilities.",
            tech_stack="Python, Django, HTML, CSS, JavaScript", # Default
            video=video_rel_path
        )
    
print("Project videos updated.")
