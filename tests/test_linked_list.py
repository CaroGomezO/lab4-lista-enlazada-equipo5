# tests/test_linked_list.py
# Pruebas base escritas por el docente.
# CADA EQUIPO agregará sus propias pruebas en este archivo
# desde su rama — esto generará merge conflicts intencionales.

import pytest
from src.linked_list import LinkedList, Node


# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                             #
# ------------------------------------------------------------------ #

def test_lista_vacia_str():
    ll = LinkedList()
    assert str(ll) == "Lista vacía"


def test_lista_vacia_len():
    ll = LinkedList()
    assert len(ll) == 0


def test_node_repr():
    n = Node(42)
    assert repr(n) == "Node(42)"
    

# ------------------------------------------------------------------ #
# Pruebas del Equipo B — delete                                       #
# ------------------------------------------------------------------ #

def test_delete_nodo_existente():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    assert ll.delete(2) == True
    assert len(ll) == 2

def test_delete_cabeza():
    ll = LinkedList()
    ll.head = Node(10)
    ll.head.next = Node(20)
    assert ll.delete(10) == True
    assert ll.head.data == 20

def test_delete_ultimo_nodo():
    ll = LinkedList()
    ll.head = Node(5)
    ll.head.next = Node(9)
    assert ll.delete(9) == True
    assert ll.head.next is None

def test_delete_valor_no_existe():
    ll = LinkedList()
    ll.head = Node(1)
    assert ll.delete(99) == False

def test_delete_lista_vacia():
    ll = LinkedList()
    assert ll.delete(1) == False