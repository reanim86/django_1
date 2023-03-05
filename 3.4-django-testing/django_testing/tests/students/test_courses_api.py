import pytest
from model_bakery import baker
from random import randint


from rest_framework.test import APIClient

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert data[0]['name'] == course[0].name

@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    course = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert len(course) == len(data)

@pytest.mark.django_db
def test_id_course(client, course_factory):
    course = course_factory(_quantity=10)
    n = randint(0, 9)
    response = client.get('/api/v1/courses/?id=1')
    # response = client.get('/api/v1/courses/')
    data = response.json()
    assert len(data['id'][0]) == course[0].name
    # assert len(data) == 1

