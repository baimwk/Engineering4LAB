import unittest
from context import src
from src.lab4 import lab4


class TestLab4(unittest.TestCase):
    def testADJ(self):
        self.assertEqual(lab4('Красивый, счастливый, зеленый!'), (3, 0, 0))

    def testADVERB(self):
        self.assertEqual(lab4('Весело он насухо'), (0, 2, 0))

    def testVERB(self):
        self.assertEqual(lab4('Лает он, кусает. Прыгает и играет'), (0, 0, 4))

    def testJim(self):
        self.assertEqual(lab4('Дай, Джим, на счастье лапу мне, Такую лапу не видал я сроду. '), (1, 1, 2))
