import unittest

from tires.octoprime import Octoprime

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires = Octoprime([0.5, 1.0, 1.0, 0.5])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires = Octoprime([0.5, 0.5, 0.5, 0.5])
        self.assertFalse(tires.needs_service())