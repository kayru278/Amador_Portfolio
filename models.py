from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="e.g., Python, PHP, MySQL, Django")
    role = models.CharField(max_length=150, blank=True, help_text="e.g., Lead Developer, Team Leader")
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title