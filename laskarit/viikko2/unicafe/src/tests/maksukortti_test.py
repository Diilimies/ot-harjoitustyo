import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(234)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.34 euroa")
    
    def test_saldo_vahenee_jos_rahaa(self):
        self.maksukortti.ota_rahaa(900)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

    def test_saldo_ei_vahene_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_true_jos_rahaa_otettu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)

    def test_false_jos_rahaa_ei_otettu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)