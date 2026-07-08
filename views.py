from django.shortcuts import render
from .models import Project

def portfolio_index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,

        # Personal Information
        'name': 'Kyle Andrei Amador',
        'tagline': 'Graduate of Holy Angel University | Aspiring Web Developer',

        'about': '''
        Hello! I'm Kyle Andrei Amador, a graduate of Holy Angel University.
        I am passionate about web development and continuously improving my
        programming skills. I enjoy creating responsive websites and learning
        technologies such as Python, Django, HTML, CSS, JavaScript, Git,
        and GitHub.
        ''',

        'education': 'Holy Angel University',

        'email': 'andreiamador10@gmail.com',

        'skills': [
            'HTML',
            'CSS',
            'JavaScript',
            'Python',
            'Django',
            'Git',
            'GitHub'
        ],
    }

    return render(request, 'portfolio/index.html', context)