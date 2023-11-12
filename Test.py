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

    def test_ObtieneValencia2(self):
        mc = MiClase(24736, 116, 15, [
                     "Canción 4", "Canción 5", "Canción 6"], [0.3, 0.6, 0.5])
        self.assertEqual(mc.ObtieneValencia(24736), 2)

    def test_DivisibleTempo2(self):
        mc = MiClase(24736, 116, 15, [
                     "Canción 4", "Canción 5", "Canción 6"], [0.3, 0.6, 0.5])
        self.assertEqual(mc.DivisibleTempo(116), [1, 2, 4, 29, 58, 116])

    def test_ObtieneMasBailable2(self):
        mc = MiClase(24736, 116, 15, [
                     "Canción 4", "Canción 5", "Canción 6"], [0.3, 0.6, 0.5])
        self.assertEqual(mc.ObtieneMasBailable([0.3, 0.6, 0.5]), 0.6)

    def test_VerificaListaCanciones2(self):
        mc = MiClase(24736, 116, 15, [
                     "Canción 4", "Canción 5", "Canción 6"], [0.3, 0.6, 0.5])
        self.assertEqual(mc.VerificaListaCanciones(
            ["Canción 4", "Canción 5", "Canción 6"]), True)

    def test_Encuentra(self):
        mc = MiClase(24736, 116, 15, [
                     "Canción 4", "Canción 5", "Canción 6"], [0.3, 0.6, 0.5])
        self.assertEqual(mc.Encuentra(
            [1, 43, 56, 78, 23, 6], 78), True)


if __name__ == "__main__":
    unittest.main()
