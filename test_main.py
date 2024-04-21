# test_main.py

from fastapi.testclient import TestClient
from main import app
import pytest
from unittest.mock import MagicMock

# Create a fixture to initialize the TestClient object
@pytest.fixture
def client():
    return TestClient(app)

# Create a fixture to mock the CourseManager instance
@pytest.fixture
def course_manager():
    return MagicMock()

# Create a fixture to mock the UserManager instance
@pytest.fixture
def user_manager():
    return MagicMock()

# Test case for the welcome endpoint
def test_welcome(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text.strip('"') == "Welcome to our miniCanvas!"

# Test case for the create_a_course endpoint
def test_create_a_course(client, user_manager, course_manager):
    # Add some users for testing
    user_manager.create_a_user = MagicMock(return_value=None)

    # Make a POST request to create a course
    response = client.post("/courses/CS101", json={"semester": "Spring 2022", "teacher_id_list": [1, 2]})
    
    # Assertions
    assert response.status_code == 200  # Expecting 200 OK for successful creation
    assert response.json()  # Optionally, assert the response body contains expected data

# Test case for the import_students endpoint
def test_import_students(client, course_manager):
    # Add a course for testing
    course_manager.create_a_course = MagicMock(return_value=None)

    # Make a PUT request to import students
    response = client.put("/courses/1/students", json={"student_id_list": [3, 4]})
    
    # Assertions
    assert response.status_code == 200  # Expecting 200 OK for successful import
    assert response.json()  # Optionally, assert the response body contains expected data

# Test case for the course not found scenario
def test_course_not_found(client, course_manager):
    # Mocking course_manager.find_a_course to return None for non-existing course
    course_manager.find_a_course = MagicMock(return_value=None)

    # Make a PUT request to import students to a non-existing course
    response = client.put("/courses/2/students", json={"student_id_list": [3, 4]})
    
    # Assertions
    assert response.status_code == 404  # Expecting 404 NOT FOUND for non-existing course
    assert response.json() == {"detail": "Course with ID 2 not found"}  # Verify error message