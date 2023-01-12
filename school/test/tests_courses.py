from django.http import response
from rest_framework.test import APITestCase
from school.models import Course
from django.urls import reverse
from rest_framework import status

class CoursesTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course_1 = Course.objects.create(
            course_code='CTT1', description='Course 1', level='B'
        )
        self.course_2 = Course.objects.create(
            course_code='CTT2', description='Course 2', level='A'
        )

    def test_list_courses_success(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_course_success(self):
        data = {
            'course_code':'CTT3',
            'description':'Course 3',
            'level':'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_course_not_allowed(self):
        response = self.client.delete('/courses/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_course_success(self):
        data = {
            'course_code':'CTT1',
            'description':'Course 1 Updated',
            'level':'A'
        }
        response = self.client.put('/courses/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)