from django.core.management.base import BaseCommand
from main.models import Skill, Experience, Project
from datetime import date, datetime

class Command(BaseCommand):
    help = 'Populate database with initial portfolio data'

    def handle(self, *args, **kwargs):
        # Skills Data
        skills_data = [
            # Frontend
            {'name': 'HTML5', 'category': 'Frontend', 'proficiency': 90},
            {'name': 'CSS3', 'category': 'Frontend', 'proficiency': 85},
            {'name': 'JavaScript (ES6+)', 'category': 'Frontend', 'proficiency': 80},
            {'name': 'React.js', 'category': 'Frontend', 'proficiency': 75},
            {'name': 'Svelte', 'category': 'Frontend', 'proficiency': 70},
            {'name': 'Bootstrap', 'category': 'Frontend', 'proficiency': 85},
            {'name': 'Tailwind CSS', 'category': 'Frontend', 'proficiency': 80},
            
            # Backend
            {'name': 'Python', 'category': 'Backend', 'proficiency': 90},
            {'name': 'Django', 'category': 'Backend', 'proficiency': 85},
            {'name': 'Flask', 'category': 'Backend', 'proficiency': 80},
            {'name': 'PHP', 'category': 'Backend', 'proficiency': 70},
            {'name': 'Laravel', 'category': 'Backend', 'proficiency': 75},
            
            # Database
            {'name': 'MySQL', 'category': 'Backend', 'proficiency': 85}, # Grouping DB under Backend for now or change model choices
            
            # Tools
            {'name': 'Git', 'category': 'Tools', 'proficiency': 90},
            {'name': 'Azure DevOps', 'category': 'Tools', 'proficiency': 75},
            {'name': 'VS Code', 'category': 'Tools', 'proficiency': 95},
        ]
        
        # Note: Skill model uses choices: Frontend, Backend, Tools, Other. 
        # MySQL and MongoDB should technically be 'Backend' or I should add 'Database' to model choices?
        # The prompt model had "category (Frontend / Backend / Tools)". I will map Database to Backend or Tools.
        # Let's put Databases in 'Backend' or 'Other'. Or better, update model choices later if needed. For now 'Backend'.

        self.stdout.write('Populating Skills...')
        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill['name'],
                defaults={'category': skill['category'], 'proficiency': skill['proficiency']}
            )

        # Experience Data
        experiences = [
            {
                'role': 'Python Developer',
                'company': 'Tata Consultancy Services (TCS)',
                'start_date': date(2024, 9, 1),
                'end_date': None,
                'description': '''• Developing and maintaining backend modules using Python and Flask for automation and data management.
• Collaborating with cross-functional teams to optimize API performance and streamline business logic.
• Conducting code reviews to maintain high-quality standards and improve maintainability.
• Azure Devops for deployment.
Technologies: Python, Flask, SqlAlchemy, Azure Devops'''
            },
            {
                'role': 'Web Developer',
                'company': 'Continuous Excellence (CE)',
                'start_date': date(2024, 1, 1),
                'end_date': date(2024, 8, 30),
                'description': '''BIMSU, MineInfo and ME-website:
• Designed and implemented responsive applications using React.js, improving project delivery speed.
• Engineered transformers for enhanced data handling efficiency.
• Optimized code performance and UI responsiveness, ensuring smooth user experience.
Technologies: React, fast-api'''
            },
            {
                'role': 'Web Developer',
                'company': 'NBNminds',
                'start_date': date(2022, 3, 1),
                'end_date': date(2023, 2, 28),
                'description': '''Vector, Bursary and Golf:
• Developed key components using Svelte and Laravel, driving innovation in the Vector Project.
• Implemented CRUD operations and optimized database performance for large-scale data management.
• Managed cron jobs in the Bursary Project to automate reporting processes.
• Handled complex database migrations in the Golf Project, improving stability and load times.
• Contributed to no-code platform development with advanced file handling and modular structure.
Technologies: php, Laravel and Svelte'''
            }
        ]

        self.stdout.write('Populating Experience...')
        for exp in experiences:
            Experience.objects.get_or_create(
                company=exp['company'],
                role=exp['role'],
                defaults={
                    'start_date': exp['start_date'],
                    'end_date': exp['end_date'],
                    'description': exp['description']
                }
            )
            
        # Projects Data
        projects_data = [
            {
                'title': 'Jodhana Tourism',
                'description': 'A tourism website for Jodhpur city featuring booking and information services.',
                'tech_stack': 'Laravel, PHP, MySQL, Bootstrap',
                'github_url': 'https://github.com/ToshiJain15/jodhana',
                'live_demo_url': None
            },
            {
                'title': 'School Management System (Laravel)',
                'description': 'Comprehensive school management system handling student data, attendance, and reporting.',
                'tech_stack': 'Laravel, PHP, MySQL',
                'github_url': 'https://github.com/ToshiJain15/SchoolLaravel',
                'live_demo_url': None
            },
             {
                'title': 'School Management (Core PHP)',
                'description': 'Core PHP implementation of a school management system.',
                'tech_stack': 'PHP, MySQL, HTML/CSS',
                'github_url': 'https://github.com/ToshiJain15/Schoolphpcore',
                'live_demo_url': None
            },
            {
                'title': 'Machine Learning Experiments',
                'description': 'Collection of machine learning models and experiments.',
                'tech_stack': 'Python, Scikit-learn, Pandas',
                'github_url': 'https://github.com/ToshiJain15/machine_learning',
                'live_demo_url': None
            },
            {
                'title': 'OpenCV Computer Vision',
                'description': 'Computer vision projects using OpenCV library.',
                'tech_stack': 'Python, OpenCV',
                'github_url': 'https://github.com/ToshiJain15/opencv',
                'live_demo_url': None
            },
            {
                'title': 'Django Project',
                'description': 'A web application built with the Django framework.',
                'tech_stack': 'Django, Python, SQLite',
                'github_url': 'https://github.com/ToshiJain15/django_project',
                'live_demo_url': None
            },
             {
                'title': 'Crossword',
                'description': 'Crossword puzzle generator/solver.',
                'tech_stack': 'Python, AI',
                'github_url': 'https://github.com/ToshiJain15/crossword',
                'live_demo_url': None
            }
        ]
        
        self.stdout.write('Populating Projects...')
        for proj in projects_data:
            Project.objects.get_or_create(
                title=proj['title'],
                defaults={
                    'description': proj['description'],
                    'tech_stack': proj['tech_stack'],
                    'github_url': proj['github_url'],
                    'live_demo_url': proj['live_demo_url']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated portfolio data'))
