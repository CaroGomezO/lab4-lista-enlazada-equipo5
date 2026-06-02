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


# ------------------------------------------------------------------ #
# Pruebas Equipo A — append                                           #
# ------------------------------------------------------------------ #

def test_append_un_elemento():
    ll = LinkedList()
    ll.append(10)
    assert ll.head is not None
    assert ll.head.data == 10
    assert len(ll) == 1


def test_append_varios_elementos():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert str(ll) == "1 -> 2 -> 3"
    assert len(ll) == 3


def test_append_orden_preservado():
    ll = LinkedList()
    for v in [5, 10, 15]:
        ll.append(v)
    current = ll.head
    for expected in [5, 10, 15]:
        assert current.data == expected
        current = current.next


def test_append_lista_inicia_vacia():
    ll = LinkedList()
    assert ll.head is None
    assert len(ll) == 0
    assert str(ll) == "Lista vacía"


def test_append_ultimo_nodo_apunta_a_none():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    current = ll.head
    while current.next:
        current = current.next
    assert current.next is None


def test_append_valor_cero():
    ll = LinkedList()
    ll.append(0)
    assert ll.head is not None
    assert ll.head.data == 0
    assert len(ll) == 1


def test_append_un_elemento_next_es_none():
    ll = LinkedList()
    ll.append(42)
    assert ll.head.next is None


def test_append_multiples_elementos():
    ll = LinkedList()
    n = 1000
    for i in range(n):
        ll.append(i)
    assert len(ll) == n
    assert ll.head.data == 0


def test_append_datos_duplicados():
    ll = LinkedList()
    ll.append(5)
    ll.append(5)
    assert len(ll) == 2
    assert str(ll) == "5 -> 5"
