from django.db import models


class Banner(models.Model):
    """Model for promotional banners."""
    
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='banners/')
    bg_color = models.CharField(max_length=10, help_text="Hex color code e.g. 0xFFE040FB", default="0xFF000000")
    button_text = models.CharField(max_length=50, blank=True)
    action_link = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
        
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return None
