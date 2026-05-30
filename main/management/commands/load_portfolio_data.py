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
            {'name': 'FastAPI', 'category': 'Backend', 'proficiency': 85},
            {'name': 'PHP', 'category': 'Backend', 'proficiency': 70},
            {'name': 'Laravel', 'category': 'Backend', 'proficiency': 75},
            {'name': 'SQLAlchemy', 'category': 'Backend', 'proficiency': 80},
            {'name': 'MySQL', 'category': 'Backend', 'proficiency': 85},
            {'name': 'MongoDB', 'category': 'Backend', 'proficiency': 75},
            {'name': 'SQLite', 'category': 'Backend', 'proficiency': 80},
            
            # AI / ML
            {'name': 'Scikit-learn', 'category': 'AI/ML', 'proficiency': 85},
            {'name': 'OpenCV', 'category': 'AI/ML', 'proficiency': 80},
            {'name': 'Pandas', 'category': 'AI/ML', 'proficiency': 85},
            {'name': 'NumPy', 'category': 'AI/ML', 'proficiency': 80},
            {'name': 'Matplotlib', 'category': 'AI/ML', 'proficiency': 75},
            
            # Tools
            {'name': 'Git', 'category': 'Tools', 'proficiency': 90},
            {'name': 'Azure DevOps', 'category': 'Tools', 'proficiency': 75},
            {'name': 'Postman', 'category': 'Tools', 'proficiency': 85},
            {'name': 'VS Code', 'category': 'Tools', 'proficiency': 95},
            {'name': 'Jupyter Notebook', 'category': 'Tools', 'proficiency': 80},
            {'name': 'Linux', 'category': 'Tools', 'proficiency': 80},
        ]
        
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
                'end_date': date(2026, 5, 22),
                'description': '''○ Led migration from deprecated Azure AD APIs to Microsoft Graph APIs, ensuring uninterrupted enterprise identity-management and authentication workflows.
○ Investigated and resolved production issues involving user provisioning, UPN validation, and permission synchronization, improving platform reliability and reducing recurring support incidents.
○ Developed and maintained Python-based automation scripts and backend services supporting cybersecurity and access-management operations for Sodexo internal platforms.
○ Performed PostgreSQL query analysis and troubleshooting for service requests, accelerating issue resolution and improving operational efficiency across business-critical workflows.
○ Collaborated with cross-functional teams to perform root-cause analysis, implement fixes, and validate production deployments while meeting SLA commitments.
Stack: Python, Microsoft Graph API, Azure AD, MySQL, REST APIs, Azure DevOps'''
            },
            {
                'role': 'Web Developer',
                'company': 'Continuous Excellence (CE)',
                'start_date': date(2024, 1, 1),
                'end_date': date(2024, 8, 31),
                'description': '''○ Engineered 3 responsive React.js applications (BIMSU, MineInfo, ME-Website) serving 500+ concurrent users, accelerating project delivery speed by 20%.
○ Designed and implemented a custom FastAPI data-transformer middleware layer, reducing large-scale data-ingestion latency by 40%.
○ Optimised component-level rendering and bundle sizes across all three products, slashing initial page-load time by 35% through targeted performance profiling.
Stack: React.js, FastAPI, Python, HTML5, CSS3'''
            },
            {
                'role': 'Web Developer',
                'company': 'NBNminds',
                'start_date': date(2022, 3, 1),
                'end_date': date(2023, 2, 28),
                'description': '''○ Developed core features for the Vector no-code platform using Svelte and Laravel, contributing to a 15% reduction in client onboarding time.
○ Automated cron-job reporting for the Bursary project, eliminating 8+ hours of weekly manual effort and reducing reporting errors to near zero.
○ Executed complex MySQL schema migrations for the Golf project, improving query performance by 20% and measurably reducing page-load latency.
○ Designed modular CRUD APIs with optimised indexing and cursor-based pagination, reliably supporting 100,000+ records without performance degradation.
Stack: PHP, Laravel, Svelte, MySQL'''
            }
        ]
 
        self.stdout.write('Populating Experience...')
        for exp in experiences:
            Experience.objects.update_or_create(
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
                'title': 'Jodhana',
                'description': 'Built a community platform using PHP/Laravel with role-based authentication, content workflows, and a fully normalised MySQL schema (12+ tables), achieving sub-100 ms query response times under load.\nResolved 15+ deployment issues and streamlined the onboarding process, reducing new-contributor environment-setup time by 50%.',
                'tech_stack': 'PHP, Laravel, MySQL, HTML5, CSS3',
                'github_url': 'https://github.com/ToshiJain15/jodhana',
                'video_file': 'websites/Jodhana Trip Advisor.webm'
            },

            {
                'title': 'Modern React Web App',
                'description': 'A scalable and responsive web application built with React, focusing on component-based architecture.',
                'tech_stack': 'React JavaScript CSS',
                'github_url': None,
                'video_file': 'websites/ME-website.webm'
            },
            {
                'title': 'Admin Portal - Exam Scheduling',
                'description': 'An interface for teachers to manage student performance, grading, and course materials.',
                'tech_stack': 'Django + React',
                'github_url': None,
                'video_file': 'websites/Admin.webm'
            },
            {
                'title': 'Student Portal - College System',
                'description': 'An interface for students to manage student performance, grading, and course materials.',
                'tech_stack': 'Django + React',
                'github_url': None,
                'video_file': 'websites/Student.webm'
            },
            {
                'title': 'College Website',
                'description': 'A dedicated portal for students to track attendance, grades, and school announcements.',
                'tech_stack': 'Django + React',
                'github_url': None,
                'video_file': 'websites/React App.webm'
            },

            {
                'title': 'Guru Chairs',
                'description': 'A high-end, luxury furniture showcase website with elegant design and premium product displays.',
                'tech_stack': 'HTML CSS JavaScript Bootstrap',
                'github_url': None,
                'video_file': 'websites/GURU CHAIRS _ Ultra Luxury Furniture.webm'
            },
            {
                'title': 'Jain Masala',
                'description': 'A pure Indian heritage food brand website focusing on traditional spices and flavor storytelling.',
                'tech_stack': 'HTML CSS JavaScript',
                'github_url': None,
                'video_file': 'websites/Jain Masala _ Pure Indian Heritage.webm'
            },
            {
                'title': 'Machine Learning Projects Collection',
                'description': 'Built COVID-19 forecasting and house-price prediction models (Scikit-learn) achieving R2 > 0.85; developed an ad click-through classifier reaching 88% accuracy via gradient-boosting pipelines.',
                'tech_stack': 'Python, Scikit-learn, Pandas, Matplotlib, Jupyter Notebook',
                'github_url': 'https://github.com/ToshiJain15/machine_learning',
                'live_demo_url': 'https://toshijain15.github.io/machine_learning/',
                'image_file': 'projects/machine_learning.png',
                'video_file': None
            },
            {
                'title': 'OpenCV Computer Vision Suite',
                'description': 'Implemented a real-time face-detection and social-distancing monitor in Python and OpenCV capable of processing live video at 25+ FPS; proximity-alert logic achieved 92% detection accuracy.',
                'tech_stack': 'Python, OpenCV, NumPy, Jupyter Notebook',
                'github_url': 'https://github.com/ToshiJain15/opencv',
                'live_demo_url': 'https://toshijain15.github.io/opencv/',
                'image_file': 'projects/opencv.png',
                'video_file': None
            },
             {
                'title': 'Crossword',
                'description': 'Crossword puzzle generator/solver.',
                'tech_stack': 'Python AI',
                'github_url': 'https://github.com/ToshiJain15/crossword',
                'live_demo_url': 'https://toshijain15.github.io/crossword/lab/index.html',
                'image_file': 'projects/crossword.png',
                'video_file': 'websites/crossword.webm'
            },
            {
                'title': 'Potato Post',
                'description': 'Delivered a full-featured Django social platform with authentication, posts, likes, and user profiles; optimised static-file serving to achieve a 30% reduction in page-load time.',
                'tech_stack': 'Python, Django, SQLite, HTML5, CSS3',
                'github_url': 'https://github.com/ToshiJain15/potato_post',
                'video_file': 'websites/Home _ Desi Potato Post.webm'
            },
             {
                'title': 'Rent As Buddy',
                'description': 'A platform to rent a buddy for social events or company.',
                'tech_stack': 'Django Python HTML CSS',
                'github_url': None,
                'video_file': 'websites/Home _ Rent As Buddy.webm'
            },
             {
                'title': 'Vendor Management System',
                'description': 'System to manage vendors, orders, and inventory efficiently.',
                'tech_stack': 'Django Python HTML CSS',
                'github_url': None,
                'video_file': 'websites/Vendor Management System.webm'
            },
 
             {
                'title': 'Bimsu App',
                'description': 'A web application for Bimsu services.',
                'tech_stack': 'React Python',
                'github_url': None,
                'video_file': 'websites/Bimsu.webm'
            },
             {
                'title': 'Analytics Dashboard',
                'description': 'A data visualization dashboard for business analytics.',
                'tech_stack': 'React D3.js Python',
                'github_url': None,
                'video_file': 'websites/Dashboard.webm'
            },
             {
                'title': 'Mine Info Platform',
                'description': 'Information platform for mining industry data.',
                'tech_stack': 'React Python',
                'github_url': None,
                'video_file': 'websites/Mine-Info.webm'
            }
        ]
        
        self.stdout.write('Populating Projects...')
        processed_titles = []
        for proj in projects_base:
            defaults = {
                'description': proj['description'],
                'tech_stack': proj['tech_stack'],
                'github_url': proj.get('github_url'),
                'live_demo_url': proj.get('live_demo_url')
            }
            if proj.get('video_file'):
                defaults['video'] = proj['video_file']
            if proj.get('image_file'):
                defaults['image'] = proj['image_file']
            
            Project.objects.update_or_create(
                title=proj['title'],
                defaults=defaults
            )
            processed_titles.append(proj['title'])
            
        # Clean up projects not in the list anymore
        Project.objects.exclude(title__in=processed_titles).delete()

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
