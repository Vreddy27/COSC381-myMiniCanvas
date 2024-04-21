import pytest
from user import UserManager, User

@pytest.fixture
def user_manager():
    return UserManager()

def test_generate_id(user_manager):
    # Generate IDs and check if they are unique
    id_set = set()
    for _ in range(10):
        new_id = user_manager.generate_id()
        assert new_id not in id_set
        id_set.add(new_id)

def test_create_a_user(user_manager):
    # Create a user
    user_manager.create_a_user("John", "password", "student")

    # Check if the user list contains the created user
    assert len(user_manager.user_list) == 1
    assert user_manager.user_list[0].name == "John"
    assert user_manager.user_list[0].password == "password"
    assert user_manager.user_list[0].user_type == "student"  # Change 'type' to 'user_type'


def test_find_users(user_manager):
    # Create some users
    user_manager.create_a_user("Alice", "password1", "teacher")
    user_manager.create_a_user("Bob", "password2", "student")
    user_manager.create_a_user("Charlie", "password3", "admin")

    # Find users by their IDs
    users_found = user_manager.find_users([1, 3])
    assert len(users_found) == 2
    assert users_found[0].name == "Alice"
    assert users_found[1].name == "Charlie"

    # Find users by their IDs (non-existent ID)
    users_found = user_manager.find_users([4])
    assert len(users_found) == 0

    # Find users by their IDs (empty list)
    users_found = user_manager.find_users([])
    assert len(users_found) == 0


