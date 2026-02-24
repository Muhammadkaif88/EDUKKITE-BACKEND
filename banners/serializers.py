from rest_framework import serializers
from .models import Banner

class BannerSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Banner
        fields = [
            'id', 'title', 'subtitle', 'image', 'image_url', 
            'bg_color', 'button_text', 'target_type', 'target_id', 
            'action_link', 'is_active', 'order', 'valid_from', 'valid_until'
        ]
        read_only_fields = ['id', 'image_url']
        
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
