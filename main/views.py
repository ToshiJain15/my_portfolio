from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Experience, Achievement
from .forms import ContactForm

def home(request):
    achievements = Achievement.objects.all()[:6]  # Get latest 6 achievements
    return render(request, 'main/home.html', {'achievements': achievements})

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects_list})

def skills(request):
    # Group skills by category
    skills_data = {}
    categories = Skill.CATEGORY_CHOICES
    for cat_key, cat_name in categories:
        skills_data[cat_name] = Skill.objects.filter(category=cat_key)
    
    
    # Fetch HackerRank Data
    from .utils import get_hackerrank_data
    # You can change this username to your actual HackerRank username
    hackerrank_data = get_hackerrank_data('ToshiJain15')
    
    return render(request, 'main/skills.html', {'skills_data': skills_data, 'hackerrank': hackerrank_data})

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'main/experience.html', {'experiences': experiences})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def achievements_list(request):
    achievements = Achievement.objects.all()
    return render(request, 'main/achievements.html', {'achievements': achievements})
