import pytest
from course import Course, CourseManager
import unittest


@pytest.fixture
def course_instance():
    # Fixture to create a Course instance with default values
    return Course(1, "COSC381", "Winter 2024", ["Teacher1", "Teacher2"])

@pytest.fixture
def course_manager_instance():
    # Fixture to create a CourseManager instance
    return CourseManager()

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course_id = 1
        self.course_code = "CS101"
        self.semester = "Spring"
        self.teacher_list = ["John Doe", "Jane Smith"]
        self.student_list = ["Alice", "Bob"]
        self.course = Course(self.course_id, self.course_code, self.semester, self.teacher_list)

    def test_course_init(self):
        # Test __init__ method of Course class
        course = self.course
        
        # Assert that attributes are initialized correctly
        self.assertEqual(course.course_id, 1)
        self.assertEqual(course.course_code, "CS101")
        self.assertEqual(course.semester, "Spring")
        self.assertEqual(course.teacher_list, ["John Doe", "Jane Smith"])
        self.assertEqual(course.student_list, [])
        self.assertEqual(course.assignment_list, [])
        self.assertEqual(course.module_list, [])
        self.assertEqual(course.assignment_counter, 0)

    def test_import_students_method(self):
        # Test import_students method of Course class
        course = self.course
        students = ["Student1", "Student2"]
        course.import_students(students)
        
        # Assert that students are imported correctly
        self.assertEqual(course.student_list, students)

    def test_create_an_assignment_method(self):
        # Test create_an_assignment method of Course class
        course = self.course
        due_date = "2024-04-20"
        course.create_an_assignment(due_date)
        
        # Assert that an assignment is created correctly
        self.assertEqual(len(course.assignment_list), 1)
        self.assertEqual(course.assignment_list[0].due_date, due_date)
        self.assertEqual(course.assignment_list[0].course_id, 1)

    def test_generate_assignment_id_method(self):
        # Test generate_assignment_id method of Course class
        course = self.course
        self.assertEqual(course.generate_assignment_id(), 1)
        self.assertEqual(course.generate_assignment_id(), 2)

    def test_validate_teacher_list_method(self):
        # Test validate_teacher_list method of Course class
        course = self.course
        
        # Assert that the teacher list is initially valid
        self.assertTrue(course.validate_teacher_list())

        # Add a non-string teacher to the list
        course.teacher_list.append(123)
        
        # Assert that the teacher list is no longer valid
        self.assertFalse(course.validate_teacher_list())

    def test_validate_student_list_method(self):
        # Test validate_student_list method of Course class
        course = self.course

        # Assert that the student list is initially valid
        self.assertTrue(course.validate_student_list())

        # Add a non-string student to the list
        course.student_list.append(456)

        # Assert that the student list is no longer valid
        self.assertFalse(course.validate_student_list())

if __name__ == '__main__':
    unittest.main()