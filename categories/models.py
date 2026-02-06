from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Model for product categories."""
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    icon_name = models.CharField(max_length=50, blank=True, null=True)
    color_hex = models.CharField(max_length=10, blank=True, null=True)
    order_index = models.IntegerField(default=0, help_text="Order in which categories are displayed")
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order_index', 'name']
        
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    @property
    def image_url(self):
        """Return the image URL if image exists."""
        if self.image:
            return self.image.url
        return None
