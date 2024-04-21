# test_course.py

import pytest
from course import Course, CourseManager

@pytest.fixture
def course_instance():
    # Fixture to create a Course instance with default values
    return Course(1, "COSC381", "Winter 2024", ["Teacher1", "Teacher2"])

@pytest.fixture
def course_manager_instance():
    # Fixture to create a CourseManager instance
    return CourseManager()

class TestCourse:
    def test_course_init(self, course_instance):
        # Test __init__ method of Course class
        course = course_instance
        
        # Assert that attributes are initialized correctly
        assert course.course_id == 1
        assert course.course_code == "COSC381"
        assert course.semester == "Winter 2024"
        assert course.teacher_list == ["Teacher1", "Teacher2"]
        assert course.student_list == []
        assert course.assignment_list == []
        assert course.module_list == []
        assert course.assignment_counter == 0

    def test_import_students_method(self, course_instance):
        # Test import_students method of Course class
        course = course_instance
        students = ["Student1", "Student2"]
        course.import_students(students)
        
        # Assert that students are imported correctly
        assert course.student_list == students

    def test_create_an_assignment_method(self, course_instance):
        # Test create_an_assignment method of Course class
        course = course_instance
        due_date = "2024-04-20"
        course.create_an_assignment(due_date)
        
        # Assert that an assignment is created correctly
        assert len(course.assignment_list) == 1
        assert course.assignment_list[0].due_date == due_date
        assert course.assignment_list[0].course_id == 1

    def test_generate_assignment_id_method(self, course_instance):
        # Test generate_assignment_id method of Course class
        course = course_instance
        assert course.generate_assignment_id() == 1
        assert course.generate_assignment_id() == 2
