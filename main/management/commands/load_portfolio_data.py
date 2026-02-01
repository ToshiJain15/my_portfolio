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
        # We define base metadata here, and then enhance it with video paths if they exist
        projects_base = [
            {
                'title': 'Jodhana Tourism',
                'description': 'A tourism website for Jodhpur city featuring booking and information services.',
                'tech_stack': 'Laravel, PHP, MySQL, Bootstrap',
                'github_url': 'https://github.com/ToshiJain15/jodhana',
                'video_file': 'websites/Jodhana Trip Advisor.webm'
            },
            {
                'title': 'School Management System (Laravel)',
                'description': 'Comprehensive school management system handling student data, attendance, and reporting.',
                'tech_stack': 'Laravel, PHP, MySQL',
                'github_url': 'https://github.com/ToshiJain15/SchoolLaravel',
                'video_file': None
            },
             {
                'title': 'School Management (Core PHP)',
                'description': 'Core PHP implementation of a school management system.',
                'tech_stack': 'PHP, MySQL, HTML/CSS',
                'github_url': 'https://github.com/ToshiJain15/Schoolphpcore',
                'video_file': None
            },
            {
                'title': 'Machine Learning Experiments',
                'description': 'Collection of machine learning models and experiments.',
                'tech_stack': 'Python, Scikit-learn, Pandas',
                'github_url': 'https://github.com/ToshiJain15/machine_learning',
                'video_file': None
            },
            {
                'title': 'OpenCV Computer Vision',
                'description': 'Computer vision projects using OpenCV library.',
                'tech_stack': 'Python, OpenCV',
                'github_url': 'https://github.com/ToshiJain15/opencv',
                'video_file': None
            },
             {
                'title': 'Crossword',
                'description': 'Crossword puzzle generator/solver.',
                'tech_stack': 'Python, AI',
                'github_url': 'https://github.com/ToshiJain15/crossword',
                'video_file': None
            },
            {
                'title': 'Desi Potato Post',
                'description': 'A comprehensive news or blog aggregation platform with a localized focus.',
                'tech_stack': 'Django, Python, HTML, CSS',
                'github_url': None,
                'video_file': 'websites/Home _ Desi Potato Post.webm'
            },
             {
                'title': 'Rent As Buddy',
                'description': 'A platform to rent a buddy for social events or company.',
                'tech_stack': 'Django, Python, HTML, CSS',
                'github_url': None,
                'video_file': 'websites/Home _ Rent As Buddy.webm'
            },
             {
                'title': 'Vendor Management System',
                'description': 'System to manage vendors, orders, and inventory efficiently.',
                'tech_stack': 'Django, Python, HTML, CSS',
                'github_url': None,
                'video_file': 'websites/Vendor Management System.webm'
            },
             {
                'title': 'Personal Portfolio',
                'description': 'My personal portfolio website showcasing my skills and projects.',
                'tech_stack': 'Django, Python, Bootstrap',
                'github_url': None,
                'video_file': 'websites/Home - My Portfolio.webm'
            },
             {
                'title': 'Bimsu App',
                'description': 'A web application for Bimsu services.',
                'tech_stack': 'React, Python',
                'github_url': None,
                'video_file': 'websites/Bimsu.webm'
            },
             {
                'title': 'Analytics Dashboard',
                'description': 'A data visualization dashboard for business analytics.',
                'tech_stack': 'React, D3.js, Python',
                'github_url': None,
                'video_file': 'websites/Dashboard.webm'
            },
             {
                'title': 'ME Website',
                'description': 'Corporate website for ME.',
                'tech_stack': 'React, Python',
                'github_url': None,
                'video_file': 'websites/ME-website.webm'
            },
             {
                'title': 'Mine Info Platform',
                'description': 'Information platform for mining industry data.',
                'tech_stack': 'React, Python',
                'github_url': None,
                'video_file': 'websites/Mine-Info.webm'
            }
        ]
        
        self.stdout.write('Populating Projects...')
        for proj in projects_base:
            defaults = {
                'description': proj['description'],
                'tech_stack': proj['tech_stack'],
                'github_url': proj.get('github_url'),
                'live_demo_url': None
            }
            if proj.get('video_file'):
                defaults['video'] = proj['video_file']
            
            Project.objects.update_or_create(
                title=proj['title'],
                defaults=defaults
            )

        # Achievements Data (Merged from populate_achievements.py and update_achievements.py)
        # Import Achievement dynamically to ensure model availability
        from main.models import Achievement
        from pathlib import Path

        self.stdout.write('Populating Achievements...')
        
        # Hardcoded list of achievements to ensure order and metadata is preserved
        # This replaces the dynamic file scanning which is fragile on deployment if files aren't perfectly named
        achievements_data = [
            {'title': 'University Grants Commission (UGC)-NET', 'file': 'achievements/University Grants Commission (UGC)-NET _ India.pdf', 'description': 'Qualified UGC-NET for Assistant Professor.', 'order': 1},
            {'title': 'GATE ScoreCard', 'file': 'achievements/Gate_ScoreCard.pdf', 'description': 'Qualified GATE Exam.', 'order': 2},
            {'title': 'Algorithmic Toolbox', 'file': 'achievements/Algorithmic Toolbox Certificate.pdf', 'description': 'Course completed on Coursera (UC San Diego). Covered greedy algorithms, dynamic programming, and divide & conquer.', 'order': 3},
            {'title': 'Microsoft Azure AI Fundamentals', 'file': 'achievements/Azure AI fundamentals.pdf', 'description': 'Foundational certification demonstrated knowledge of common ML and AI workloads on Azure.', 'order': 4},
            {'title': 'Oracle Cloud Architect', 'file': 'achievements/Oracle Architect.jfif', 'description': 'Oracle Cloud Infrastructure Architect Associate certification.', 'order': 5},
            {'title': 'Oracle Cloud Foundations', 'file': 'achievements/OracleFoundation Associate.pdf', 'description': 'Oracle Cloud Infrastructure Foundations Associate certification level.', 'order': 6},
             {'title': 'Oracle Database Administration', 'file': 'achievements/Oracle Administer.pdf', 'description': 'Training and certification in Oracle Database Administration.', 'order': 7},
            {'title': 'Startups & Innovation Workshop', 'file': 'achievements/game development workshop.pdf', 'description': 'Workshop on game development and startup innovation.', 'order': 8}, # Mapping 'game development workshop'
            {'title': 'Data Science Foundation', 'file': 'achievements/Data Science Foundation bootcamp.pdf', 'description': 'Bootcamp covering the core concepts of Data Science, Statistics, and Python for Data Analysis.', 'order': 9},
            {'title': 'Data Science Essentials', 'file': 'achievements/Essential 101_ Certifiation Program in Data Science.pdf', 'description': 'Certification program covering the 101s of Data Science and Analytics.', 'order': 10},
            {'title': 'Data Science Advanced', 'file': 'achievements/Essential 101_ Certifiation Program in Data Science (1).pdf', 'description': 'Advanced module of the Data Science certification program.', 'order': 11},
             {'title': 'AI Training Workshop', 'file': 'achievements/coincent_ai_training.pdf', 'description': 'Specialized training program in Artificial Intelligence conducted by Coincent.', 'order': 12},
             {'title': 'Tech Event Participation', 'file': 'achievements/coincent Participation.pdf', 'description': 'Certificate of participation in technical workshops organized by Coincent.', 'order': 13},
             {'title': 'Python Programming Course', 'file': 'achievements/certificate_of_completion_pythn_progate.pdf', 'description': 'Completed comprehensive Python programming curriculum on Progate.', 'order': 14},
             {'title': 'Docker & Kubernetes Training', 'file': 'achievements/EXPERTISE IN DOCKER TRAINING COMPLETION CERTIFICATE.pdf', 'description': 'Comprehensive training on Containerization, Docker, and Orchestration.', 'order': 15},
             {'title': 'Machine Learning Training', 'file': 'achievements/Goeduhub.jfif', 'description': 'Training completion at Goeduhub Technologies.', 'order': 16},
             {'title': 'Python Training', 'file': 'achievements/Goeduhub2.jfif', 'description': 'Python programming training at Goeduhub Technologies.', 'order': 17},
             {'title': 'Data Analytics Training', 'file': 'achievements/Goeduhub3.jfif', 'description': 'Data Analytics training session at Goeduhub Technologies.', 'order': 18},
        ]

        for ach in achievements_data:
            Achievement.objects.update_or_create(
                title=ach['title'],
                defaults={
                    'file': ach['file'],
                    'description': ach['description'],
                    'order': ach['order']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated portfolio data'))
