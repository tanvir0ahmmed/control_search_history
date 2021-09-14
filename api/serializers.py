from rest_framework import serializers
from .models import UserSearchHistory, Smartphone

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSearchHistory
        fields = ['id', 'username', 'search_keyword', 'searched_at']
        
class SmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphone
        fields = ['id', 'name', 'description']