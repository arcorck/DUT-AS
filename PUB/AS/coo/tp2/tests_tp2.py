from tp2 import *

def test_box_create():
    b = Box()

def test_box_add():
    b = Box()
    b.add("truc")
    b.add("machin")

def test_box_contains():
    b = Box()
    b.add("truc")
    b.add("machin")
    assert "truc" in b
    assert "bidule" not in b
    assert "machin" in b

def test_box_remove():
    b = Box()
    b.add("truc")
    b.add("machin")
    b.remove("truc")
    assert "machin" in b
    assert "truc" not in b

def test_box_open():
    b = Box()
    # une boite doit être fermée par défaut
    assert not b.is_open()
    b.open()
    assert b.is_open()
    b.close()
    assert not b.is_open()

def test_action_look():
    b = Box()
    b.add("truc")
    b.add("machin")
    assert b.action_look() == "la boite est fermée !"
    b.open()
    assert b.action_look() == "la boite contient: truc, machin"


def test_thing_create():
    chose = Thing(3)

def test_thing_volume():
    chose = Thing(5)
    assert chose.volume() == 5

