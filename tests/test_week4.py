from week4 import adieu

def test_names():
    assert 'Ed' == adieu.join_names(['Ed'])
    assert 'Ed and Kathleen' == adieu.join_names(['Ed', 'Kathleen'])
    assert 'Ed, Kathleen, and Kelsey' == adieu.join_names(['Ed', 'Kathleen', 'Kelsey'])
    assert 'Ed, Kathleen, Kelsey, and Pixie' == adieu.join_names(['Ed', 'Kathleen', 'Kelsey', 'Pixie'])
