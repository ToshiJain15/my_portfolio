
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Achievement

updates = {
    'Algorithmic Toolbox Certificate': {
        'title': 'Algorithmic Toolbox',
        'description': 'Course completed on Coursera (UC San Diego). Covered greedy algorithms, dynamic programming, and divide & conquer.'
    },
    'Azure Ai Fundamentals': {
        'title': 'Microsoft Azure AI Fundamentals',
        'description': 'Foundational certification demonstrated knowledge of common ML and AI workloads on Azure.'
    },
    'Certificate Of Completion Pythn Progate': {
        'title': 'Python Programming Course',
        'description': 'Completed comprehensive Python programming curriculum on Progate.'
    },
    'Coincent Ai Training': {
        'title': 'AI Training Workshop',
        'description': 'Specialized training program in Artificial Intelligence conducted by Coincent.'
    },
    'Coincent Participation': {
        'title': 'Tech Event Participation',
        'description': 'Certificate of participation in technical workshops organized by Coincent.'
    },
    'Data Science Foundation Bootcamp': {
        'title': 'Data Science Foundation',
        'description': 'Bootcamp covering the core concepts of Data Science, Statistics, and Python for Data Analysis.'
    },
    'Essential 101  Certifiation Program In Data Science': {
        'title': 'Data Science Essentials',
        'description': 'Certification program covering the 101s of Data Science and Analytics.'
    },
    'Essential 101  Certifiation Program In Data Science (1)': {
        'title': 'Data Science Advanced',
        'description': 'Advanced module of the Data Science certification program.'
    },
    'Expertise In Docker Training Completion Certificate': {
        'title': 'Docker & Kubernetes Training',
        'description': 'Comprehensive training on Containerization, Docker, and Orchestration.'
    },
    'Game Development Workshop': {
        'title': 'Game Development Workshop',
        'description': 'Hands-on workshop focused on game design principles and development tools.'
    },
    'Oracle Administer': {
        'title': 'Oracle Database Administration',
        'description': 'Training and certification in Oracle Database Administration.'
    },
    'Oracle Architect': {
        'title': 'Oracle Cloud Architect',
        'description': 'Oracle Cloud Infrastructure Architect Associate certification.'
    },
    'Oraclefoundation Associate': {
        'title': 'Oracle Cloud Foundations',
        'description': 'Oracle Cloud Infrastructure Foundations Associate certification level.'
    },
     'Goeduhub': {
        'title': 'Machine Learning Training',
        'description': 'Training completion at Goeduhub Technologies.'
    },
     'Goeduhub2': {
        'title': 'Python Training',
        'description': 'Python programming training at Goeduhub Technologies.'
    },
     'Goeduhub3': {
        'title': 'Data Analytics Training',
        'description': 'Data Analytics training session at Goeduhub Technologies.'
    },
}

for old_title, data in updates.items():
    try:
        ach = Achievement.objects.get(title=old_title)
        ach.title = data['title']
        ach.description = data['description']
        ach.save()
        print(f"Updated: {ach.title}")
    except Achievement.DoesNotExist:
        print(f"Skipped (Not Found): {old_title}")
