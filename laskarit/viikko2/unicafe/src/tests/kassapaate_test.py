import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kassapaate = Kassapaate()
    
    def test_kassapaate_alustuu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisten_kateisosto_toimii(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtorahat, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_kateisosto_toimii(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtorahat, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullisten_kateisoste_rahat_ei_riita(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtorahat, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_kateisosto_rahat_ei_riita(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtorahat, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisten_korttiosto_toimii(self):
        kortti = Maksukortti(600)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(kortti.saldo, 360)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_korttiosto_toimii(self):
        kortti = Maksukortti(600)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisten_korttiosto_ei_rahaa(self):
        kortti = Maksukortti(200)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_korttiosto_ei_rahaa(self):
        kortti = Maksukortti(200)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_saldon_lataaminen_kortille(self):
        kortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_saldon_lataaminen_kortille_negatiivinen_summa(self):
        kortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)