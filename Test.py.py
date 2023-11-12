from Examen2 import MiClase
import unittest


class TestCocinero(unittest.TestCase):

    def test_ObtieneValencia1(self):
        mc = MiClase(5, 120, 12, ["Canción 1",
                     "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.ObtieneValencia(1234567), 4)

    def test_DivisibleTempo1(self):
        mc = MiClase(5, 120, 12, ["Canción 1",
                     "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.DivisibleTempo(10), [1, 2, 5, 10])

    def test_ObtieneMasBailable1(self):
        mc = MiClase(5, 120, 12, ["Canción 1",
                     "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)

    def test_VerificaListaCanciones1(self):
        mc = MiClase(5, 120, 12, ["Canción 1",
                     "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.VerificaListaCanciones(
            ["Canción 1", "Canción 2", "Canción 3"]), True)


if __name__ == "__main__":
    unittest.main()
