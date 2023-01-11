from rest_framework import serializers
from school.models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'cpf', 'birth_date']

class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone', 'cpf', 'birth_date', 'image']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []

class StudentEnrollmentsListSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    type = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course', 'type']
    def get_type(self, obj):
        return obj.get_type_display()

class EnrolledStudentsListSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Enrollment
        fields = ['student_name']