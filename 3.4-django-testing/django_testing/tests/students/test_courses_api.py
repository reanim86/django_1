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
    response = client.get('/api/v1/courses/', {'id': f'{course[0].id}'})
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
    response = client.get('/api/v1/courses/', {'id': f'{course[n].id}'})
    data = response.json()
    assert data[0]['name'] == course[n].name

@pytest.mark.django_db
def test_name_course(client, course_factory):
    course = course_factory(_quantity=10)
    n = randint(0, 9)
    response = client.get('/api/v1/courses/', {'name': f'{course[n].name}'})
    data = response.json()
    assert data[0]['name'] == course[n].name

@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', {'name': 'some_course'})
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_patch_course(client, course_factory):
    course = course_factory(_quantity=1)
    response_patch = client.patch(f'/api/v1/courses/{course[0].id}/', {'name': 'change_name'})
    response_get = client.get('/api/v1/courses/', {'id': f'{course[0].id}'})
    data = response_get.json()
    assert data[0]['name'] == 'change_name'

@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    response_delete = client.delete(f'/api/v1/courses/{course[0].id}/')
    # response_get = client.get('/api/v1/courses/', {'id': f'{course[0].id}'})
    # data = response_get.json()
    assert response_delete.status_code == 204

