import pytest
from src.channel import Channel

@pytest.fixture
def moscowpython_channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')

@pytest.fixture
def highload_channel():
    return Channel('UCwHL6WHUarjGfUM_586me8w')

def test_str_representation(moscowpython_channel):
    assert str(moscowpython_channel) == 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'

def test_addition(moscowpython_channel, highload_channel):
    assert moscowpython_channel + highload_channel == 100100

def test_subtraction(moscowpython_channel, highload_channel):
    assert moscowpython_channel - highload_channel == -48300

def test_greater_than(moscowpython_channel, highload_channel):
    assert moscowpython_channel > highload_channel is False

# Добавьте другие тесты по необходимости