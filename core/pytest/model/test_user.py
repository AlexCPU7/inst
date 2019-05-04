import pytest

from core.models.user import User


class TestUser:
    @pytest.fixture
    def user(self):
        user = User.objects.create(
            first_name='first_name_test',
            last_name='last_name_test',
            email='test@gmail.com',
            date_birth='2019-05-04',
        )
        return user

    def test_get_full_name(self, user):
        result = user.get_full_name()
        assert result == 'last_name_test first_name_test'

    def test_get_short_name(self, user):
        result = user.get_short_name()
        assert result == 'first_name_test'
