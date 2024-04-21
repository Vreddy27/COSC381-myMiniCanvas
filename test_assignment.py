import pytest
from assignment import Assignment, Submission

# Fixture to create a sample assignment instance
@pytest.fixture
def sample_assignment():
    return Assignment(1, "2024-04-20", "COSC381")

# Test Assignment class
class TestAssignment:
    def test_assignment_init(self, sample_assignment):
        # Test __init__ method of Assignment class
        assert sample_assignment.assignment_id == 1
        assert sample_assignment.due_date == "2024-04-20"
        assert sample_assignment.course_id == "COSC381"
        assert sample_assignment.submission_list == []

    def test_submit_method(self, sample_assignment):
        # Test submit method of Assignment class
        submission = Submission(1, "Content")
        
        # Submit a submission
        sample_assignment.submit(submission)
        
        # Assert that submission is added to submission list
        assert len(sample_assignment.submission_list) == 1
        assert sample_assignment.submission_list[0] == submission

# Test Submission class
class TestSubmission:
    def test_submission_init(self):
        # Test __init__ method of Submission class
        submission = Submission(1, "Content")
        
        # Assert that attributes are initialized correctly
        assert submission.student_id == 1
        assert submission.submission == "Content"
        assert submission.grade == -1.0  # Initial grade should be -1.0