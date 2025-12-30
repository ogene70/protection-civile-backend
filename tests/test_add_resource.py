import pytest


def test_example():
    #SET UP TO INITIALISE VARIABLES
    a: int = 9
    b: int = 8 
    #ACTION PART TO LAUNCH THE SCRIPT TO TEST
     
    #ASSERT PART TO VERIFY A RESULT
    with pytest.raises(ValueError) as excinfo:
        result_to_test: float = a+b
    assert "les nombres à calculer doivent être des nombres entiers" in str(excinfo.value)
