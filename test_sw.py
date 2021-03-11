from app import Usuarium
import pytest

def UserTest():

    outcome=False
    trial = Usuarium()
    start_value=Usuarium.dpt
    
    assert Usuarium.addpt('HR')==len(start_value + 1)

        