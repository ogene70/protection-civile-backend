import pytest


def test_example():
    #SET UP TO INITIALISE VARIABLES
    a: int = 9
    b: int = 8 
    result_to_test: float = a+b
    #ACTION PART TO LAUNCH THE SCRIPT TO TEST
     
    #ASSERT PART TO VERIFY A RESULT
    assert type(result_to_test)==int
    # with pytest.raises(TypeError) as excinfo:
    #     result_to_test == float
    # assert "les nombres à calculer doivent être des nombres entiers" in str(excinfo.value)
