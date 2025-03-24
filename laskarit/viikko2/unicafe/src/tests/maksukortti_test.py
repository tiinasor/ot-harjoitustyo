import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 25.0)

    def test_rahan_ottaminen_vahentaa_saldoa_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)

    def test_rahan_ottaminen_ei_muuta_saldoa_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_metodi_palauttaa_true_jos_rahat_riittivat(self):
        self.assertTrue(self.maksukortti.ota_rahaa(900))

    def test_ota_rahaa_metodi_palauttaa_false_jos_rahat_eivat_riittaneet(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1100))
        