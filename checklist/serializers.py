from rest_framework import serializers
from .models import ChecklistItem, ChecklistGroup, ChecklistDetail

class ChecklistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistItem
        fields = ['id', 'description']


class ChecklistDetailSerializer(serializers.ModelSerializer):
    item_description = serializers.ReadOnlyField(source='item.description')
    user_username = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = ChecklistDetail
        fields = ['id', 'car_plate', 'item', 'item_description', 'status', 'user', 'user_username', 'created_at', 'group']
        read_only_fields = ['created_at']


class ChecklistGroupSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    details = ChecklistDetailSerializer(many=True, source='group', read_only=True)
    
    class Meta:
        model = ChecklistGroup
        fields = ['id', 'car_plate', 'user', 'user_username', 'created_at', 'status', 'assinatura_token', 'assinatura_confirmada', 'details']
        read_only_fields = ['assinatura_token', 'created_at']
