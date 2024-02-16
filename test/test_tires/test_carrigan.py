import unittest

from tires.carrigan import Carrigan

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires = Carrigan([0.5, 0.5, 0.9, 0.5])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires = Carrigan([0.5, 0.5, 0.5, 0.5])
        self.assertFalse(tires.needs_service())