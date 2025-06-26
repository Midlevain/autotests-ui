def test_user_login():
    print("Hello!")

class TestUserLogin:
    def test_1(selfs):
        ...

    def test_2(self):
        ...

    #///python -m pytest -s -v -k "___"///
    # assert 2 == 2, 2 == 4.
    # assert 2 != 4



def test_assert_positive_case():
    assert (2 + 2) == 4
    assert (3 + 3) == 6
    assert (4 + 4) == 8


def test_assert_negative_case():
    assert (2 + 2) == 5, "(2 + 2 ) != 5"
