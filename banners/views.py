from rest_framework import viewsets, permissions
from .models import Banner
from .serializers import BannerSerializer


class BannerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Banners.
    Public read access, Admin write access.
    """
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer
    
    def get_queryset(self):
        # Admin sees all, users see active only
        if self.request.user.is_staff:
            return Banner.objects.all()
        return Banner.objects.filter(is_active=True)
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
