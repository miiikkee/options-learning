from src.models.bs_model import black_scholes_price

def test_bs_price_type():
    price = black_scholes_price(...)
    assert isinstance(price, float)
