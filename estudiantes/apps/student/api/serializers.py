from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('autoevaluation',)

    def validate(self, attrs):
            autoevaluation = attrs.get('autoevaluation', '')
            
            if autoevaluation < 0:
                raise ValidationError("solo se permite de 0 a 5")
            if autoevaluation > 5:
                raise ValidationError("solo se permite de 0 a 5")
            return attrs


class AdminDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('note',)
        
    def validate(self, attrs):
            note = attrs.get('note', '')

            if note < 0:
                raise ValidationError("solo se permite de 0 a 5")
            if note > 5:
                raise ValidationError("solo se permite de 0 a 5")
            return attrs
