from rest_framework import serializers
from students.models import Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        exclude = ['candidate_of']