from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, help_text="Comma separated technologies")
    github_url = models.URLField(blank=True, null=True)
    live_demo_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    video = models.FileField(upload_to='projects/videos/', blank=True, null=True, help_text="Project demo video")

    def __str__(self):
        return self.title

    @property
    def category(self):
        tech = self.tech_stack.lower()
        title = self.title.lower()
        
        # Tokenize tech stack to avoid substring matches (e.g. matching 'html' for 'ml')
        tech_words = [t.strip() for t in tech.replace(',', ' ').replace('+', ' ').split()]
        
        if 'opencv' in tech_words or 'opencv' in title:
            return 'Computer Vision'
        elif 'scikit' in tech_words or 'scikit-learn' in tech_words or 'ml' in tech_words or 'machine' in tech_words or 'learning' in tech_words or 'predictive' in tech_words:
            return 'Machine Learning & AI'
        elif 'react' in tech_words or 'react.js' in tech_words or 'svelte' in tech_words or 'html' in tech_words or 'html5' in tech_words or 'css' in tech_words or 'css3' in tech_words or 'javascript' in tech_words or 'js' in tech_words:
            if 'django' in tech_words or 'flask' in tech_words or 'laravel' in tech_words or 'fastapi' in tech_words or 'php' in tech_words:
                return 'Full Stack Development'
            return 'Frontend Development'
        elif 'django' in tech_words or 'flask' in tech_words or 'laravel' in tech_words or 'fastapi' in tech_words or 'php' in tech_words:
            return 'Backend Development'
        return 'Software Development'

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('AI/ML', 'AI / ML'),
        ('Tools', 'Tools'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveIntegerField(help_text="Percentage (0-100)", default=0)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='achievements/', blank=True, null=True, help_text="Certificate file (Image or PDF)")
    video = models.FileField(upload_to='achievements/videos/', blank=True, null=True, help_text="Short demo video")
    is_video = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title
