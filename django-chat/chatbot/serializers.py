from rest_framework import serializers

class ConversationSerializer(serializers.Serializer):
    prompt = serializers.CharField()
    response = serializers.CharField()