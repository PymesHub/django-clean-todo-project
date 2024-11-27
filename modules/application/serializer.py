from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True)
    completed = serializers.BooleanField(default=False)