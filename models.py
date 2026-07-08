<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }} | Portfolio</title>

    <style>
        body{
            font-family: Arial, sans-serif;
            background:#f4f4f4;
            margin:0;
            padding:0;
        }

        header{
            background:#0f172a;
            color:white;
            text-align:center;
            padding:50px;
        }

        section{
            background:white;
            width:80%;
            max-width:900px;
            margin:30px auto;
            padding:30px;
            border-radius:10px;
            box-shadow:0 5px 15px rgba(0,0,0,.1);
        }

        h2{
            color:#0f172a;
        }

        ul{
            list-style:none;
            padding:0;
        }

        li{
            background:#2563eb;
            color:white;
            display:inline-block;
            margin:5px;
            padding:8px 15px;
            border-radius:20px;
        }

        footer{
            background:#0f172a;
            color:white;
            text-align:center;
            padding:20px;
            margin-top:30px;
        }
    </style>
</head>
<body>

<header>
    <h1>{{ name }}</h1>
    <h3>{{ tagline }}</h3>
</header>

<section>
    <h2>About Me</h2>

    <p>{{ about }}</p>
</section>

<section>
    <h2>Education</h2>

    <p>{{ education }}</p>
</section>

<section>
    <h2>Skills</h2>

    <ul>
        {% for skill in skills %}
            <li>{{ skill }}</li>
        {% endfor %}
    </ul>
</section>

<section>
    <h2>Projects</h2>

    {% for project in projects %}

        <h3>{{ project.title }}</h3>

        <p>{{ project.description }}</p>

        <p><strong>Tech Stack:</strong> {{ project.tech_stack }}</p>

        <hr>

    {% empty %}

        <p>No projects added yet.</p>

    {% endfor %}
</section>

<section>
    <h2>Contact</h2>

    <p>Email: {{ email }}</p>
</section>

<footer>
    <p>&copy; 2026 {{ name }}. All Rights Reserved.</p>
</footer>

</body>
</html>