from elementae import Usuarium
import pytest

def Testuser():

    
    trial = Usuarium()
    start_value=len(trial.dpt)
    trial.addpt('HR')
    if len(trial.dpt) != 0:
        if len(trial.dpt) == start_value +1:
            return True


def test1():
    assert Testuser()==True


        