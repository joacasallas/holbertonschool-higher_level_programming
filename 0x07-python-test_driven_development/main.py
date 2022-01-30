import unittest

class Mis_tests(unittest.TestCase):
    DatoUno = 0
    DatoDos = 0
    correr = True

    def setUp(self):
        self.DatoUno = 2
        self.DatoDos = 2
        if self.DatoUno * self.DatoDos == 2000:
            correr = False

    def test_suma(self):
        self.assertEqual(self.DatoUno+self.DatoDos,4)
        self.assertTrue(self.correr)
    
    def test_resta(self):
        self.assertTrue(self.DatoUno-self.DatoDos==0)
        self.assertTrue(self.correr)

    def tearDown(self):
        print("Borrando datos ...")
        print("llevando la base de datos a posicion inicial")
        print("guardando resultado del caso")

    def test_verificar_iguales(self):
        a = 5
        b = 4+1

        self.assertEqual(a,b)

    def test_verificar_iguales(self):
        a = 10
        b = 5*2

        self.assertNotEqual(a,b, "a tiene que ser igual a b")
    

if __name__ =='__main__':
    unittest.main()
