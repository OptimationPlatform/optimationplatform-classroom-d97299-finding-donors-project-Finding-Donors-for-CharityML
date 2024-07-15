# tests/test_model.py

import pytest
from model import  predict


def test_predict():
    x="Kat "
    assert predict(x)=="Hello"+x
