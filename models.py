from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    tech_stack = models.CharField(
        max_length=255,
        help_text="Example: HTML, CSS, JavaScript, Python, Django"
    )

    category = models.CharField(
        max_length=100,
        default="Web Development",
        help_text="Example: Web Development, Mobile App, School Project"
    )

    github_link = models.URLField(
        blank=True,
        null=True,
        help_text="GitHub repository link"
    )

    live_demo = models.URLField(
        blank=True,
        null=True,
        help_text="Live website link (optional)"
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title