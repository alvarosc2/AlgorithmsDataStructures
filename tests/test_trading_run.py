import pytest
from ..section_20_trading_model.trading_run import volado

def test_volado_returns_valid_result():
    result = volado()
    assert result in ['Sol', 'Aguila']

def test_volado_randomness():
    results = [volado() for _ in range(100)]
    assert 'Sol' in results and 'Aguila' in results