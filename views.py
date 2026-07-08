from django.shortcuts import render
from .models import Project

def portfolio_index(request):
    projects = Project.objects.all()
    
    # Optional: Hardcoded context for skills/bio if you don't want them in the DB yet
    context = {
        'projects': projects,
        'name': 'Jason',
        'tagline': 'Computer Science Student & Aspiring Red Team Cybersecurity Specialist',
        'skills': ['Python', 'PHP', 'MySQL', 'Offensive Security', 'Penetration Testing'],
    }
    return render(request, 'portfolio/index.html', context)