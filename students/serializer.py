from rest_framework import serializers
from .models import Students

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        # fields = '__all__'
        fields = ['username','first_name','email','mat_number']