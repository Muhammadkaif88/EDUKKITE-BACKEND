from django.db import models

class Course(models.Model):
    """Model for learning content."""
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    thumbnail = models.ImageField(upload_to='courses/', blank=True, null=True)
    is_locked = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail.url
        return None
