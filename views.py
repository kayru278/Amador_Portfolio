from django.shortcuts import render

def portfolio_index(request):
    context = {
        "name": "Kyle Andrei Amador",
        "tagline": "Graduate of Holy Angel University | Aspiring Web Developer",
        "about": "Hello! I'm Kyle Andrei Amador. I am passionate about web development and enjoy learning HTML, CSS, JavaScript, Python, and Django.",

        "education": "Holy Angel University",

        "email": "andreiamador10@gmail.com",

        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "Python",
            "Django",
            "Git",
            "GitHub"
        ]
    }

    return render(request, "portfolio/index.html", context)