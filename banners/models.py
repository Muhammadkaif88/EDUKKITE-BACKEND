from django.db import models
from django.utils import timezone

class Banner(models.Model):
    TARGET_CHOICES = [
        ('product', 'Product'),
        ('category', 'Category'),
        ('url', 'External URL'),
        ('none', 'None'),
    ]
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='banners/')
    bg_color = models.CharField(max_length=10, help_text="Hex color code e.g. 0xFFE040FB", default="0xFF42A5F5")
    button_text = models.CharField(max_length=50, blank=True, default="View Now")
    
    # Navigation logic
    target_type = models.CharField(max_length=20, choices=TARGET_CHOICES, default='none')
    target_id = models.CharField(max_length=100, blank=True, help_text="ID of product or category")
    action_link = models.CharField(max_length=255, blank=True, null=True, help_text="External URL if target_type is url")
    
    # Status and Order
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    # Scheduling
    valid_from = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title
