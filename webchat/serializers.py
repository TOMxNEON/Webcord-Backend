# serializers.py
from rest_framework import serializers
from .models import Conversation, Message
from accounts.models import UserAccount



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ['id', 'username', 'display_name', 'avatar']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'avatar' in data and data['avatar']:
            data['avatar'] = data['avatar'].replace(
                "https://www.webcord.site", "")
       

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = ['id','sender','content','timestamp']

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = '__all__'
