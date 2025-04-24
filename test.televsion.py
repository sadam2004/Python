import pytest
from television import Televison
def tv():
    return Televison()
def test_init():
    assert str(tv) == "Power == True, Channel = 0, Volume = 0"
def test_power():
    tv.power()
    assert str(tv) == "Power == True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power == False, Channel = 0, Volume = 0"
def test_mute():
    tv.mute()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 2, Volume = 1"
def test_channel():
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_up():
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_down():
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_volume_up():
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 2"
def test_volume_up():
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"


