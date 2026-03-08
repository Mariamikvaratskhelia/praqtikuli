from rest_framework import serializers
from .models import Student, Professor, Skill, RecommendationRequest, RecommendationLetter


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'university', 'created_at']
        read_only_fields = ['id', 'created_at']



class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'name', 'email', 'department', 'created_at']
        read_only_fields = ['id', 'created_at']



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']
        read_only_fields = ['id']



class RecommendationRequestSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    professor = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all())

    class Meta:
        model = RecommendationRequest
        fields = ['id', 'student', 'professor', 'message', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']



class RecommendationLetterSerializer(serializers.ModelSerializer):
    request = serializers.PrimaryKeyRelatedField(queryset=RecommendationRequest.objects.all())
    skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)

    class Meta:
        model = RecommendationLetter
        fields = ['id', 'request', 'content', 'skills', 'created_at']
        read_only_fields = ['id', 'created_at']