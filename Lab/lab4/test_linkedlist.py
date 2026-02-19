import unittest 
from linkedlist import Node
from linkedlist import LinkedList

class TestNode(unittest.TestCase):
    def test_init(self):
        node1 = Node("Test", None)
        self.assertEqual(node1.items,"Test")
        self.assertEqual(node1.link, None)
    
    def test_repr(self):
        node1 = Node("test")
        self.assertEqual(repr(node1), "Node(test)")

class TestLinkedList(unittest.TestCase):
    def test_init_empty(self):
        LL1 = LinkedList()
        self.assertEqual(LL1.len, 0)
        self.assertEqual(LL1.get_head(), None)
        self.assertEqual(LL1.get_tail(), None)

    def test_init_nonempty(self):
        LL1 = LinkedList(range(10))
        self.assertEqual(LL1.len, 10)
        self.assertIsNotNone(LL1.get_head())
        self.assertEqual(LL1.get_head().items, 0)
        self.assertEqual(LL1.get_tail().items, 9)

    
    def test_add_first(self):
        ll = LinkedList()
        ll.add_first("Apple")
        self.assertEqual(ll.len, 1)
        self.assertEqual(ll.get_head().items, "Apple")
        self.assertEqual(ll.get_tail().items, "Apple")

    
    def test_add_last(self):
        ll = LinkedList()
        ll.add_last("First")
        ll.add_last("Second")
        ll.add_first("Apple") 

        self.assertEqual(ll.len, 3) 
        self.assertEqual(ll.get_head().items, "Apple")
        self.assertEqual(ll.get_tail().items, "Second")

    def test_remove_first(self):
        ll = LinkedList(range(10))
        removed = ll.remove_first()
        self.assertEqual(removed.items, 0)
        self.assertEqual(ll.len, 9)
        self.assertEqual(ll.get_head().items,1)

    def test_remove_last(self):
        ll = LinkedList(["A", "B", "C"])
        removed = ll.remove_last()
        self.assertEqual(removed.items, "C")
        self.assertEqual(ll.len, 2)
        self.assertEqual(ll.get_tail().items, "B")
        self.assertIsNone(ll.get_tail().link)

        ll.remove_last() # Removes B
        ll.remove_last() # Removes A
        self.assertEqual(ll.len, 0)
        self.assertIsNone(ll.get_head())
        self.assertIsNone(ll.get_tail())

        with self.assertRaises(IndexError):
            ll.remove_last()




unittest.main()
