from rest_framework import serializers
from .models import Students, Teachers, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
