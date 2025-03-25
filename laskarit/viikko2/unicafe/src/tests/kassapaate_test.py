import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    # Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000 euroa, lounaita myyty 0)
    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_luodun_kassapaatteen_myytyjen_edullisten_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luodun_kassapaatteen_myytyjen_maukkaiden_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
    def test_jos_edullisen_lounaan_kateismaksu_on_riittava_kassassa_oleva_rahamaara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_jos_maukkaan_lounaan_kateismaksu_on_riittava_kassassa_oleva_rahamaara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_jos_edullisen_lounaan_kateismaksu_on_riittava_vaihtorahan_suuruus_on_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(340), 100)

    def test_jos_maukkaan_lounaan_kateismaksu_on_riittava_vaihtorahan_suuruus_on_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_jos_edullisen_lounaan_kateismaksu_on_riittava_myytyjen_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_maukkaan_lounaan_kateismaksu_on_riittava_myytyjen_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_edullisen_lounaan_kateismaksu_ei_ole_riittava_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_jos_maukkaan_lounaan_kateismaksu_ei_ole_riittava_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_jos_edullisen_lounaan_kateismaksu_ei_ole_riittava_kaikki_rahat_palautetaan_vaihtorahana(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_jos_maukkaan_lounaan_kateismaksu_ei_ole_riittava_kaikki_rahat_palautetaan_vaihtorahana(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_jos_edullisen_lounaan_kateismaksu_ei_ole_riittava_myytyjen_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_maukkaan_lounaan_kateismaksu_ei_ole_riittava_myytyjen_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    # Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    def test_jos_edullisen_lounaan_korttimaksu_on_riittava_summa_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_jos_maukkaan_lounaan_korttimaksu_on_riittava_summa_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)

    def test_jos_edullisen_lounaan_korttimaksu_on_riittava_palautetaan_true(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_jos_maukkaan_lounaan_korttimaksu_on_riittava_palautetaan_true(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_jos_edullisen_lounaan_korttimaksu_on_riittava_myytyjen_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_maukkaan_lounaan_korttimaksu_on_riittava_myytyjen_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_edullisen_lounaan_korttimaksu_ei_ole_riittava_kortin_rahamaara_ei_muutu(self):
        maksukortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 230)

    def test_jos_maukkaan_lounaan_korttimaksu_ei_ole_riittava_kortin_rahamaara_ei_muutu(self):
        maksukortti = Maksukortti(390)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 390)

    def test_jos_edullisen_lounaan_korttimaksu_ei_ole_riittava_myytyjen_lounaiden_maara_ei_muutu(self):
        maksukortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_maukkaan_lounaan_korttimaksu_ei_ole_riittava_myytyjen_lounaiden_maara_ei_muutu(self):
        maksukortti = Maksukortti(390)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_jos_edullisen_lounaan_korttimaksu_ei_ole_riittava_palautetaan_false(self):
        maksukortti = Maksukortti(230)

        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(maksukortti))

    def test_jos_maukkaan_lounaan_korttimaksu_ei_ole_riittava_palautetaan_false(self):
        maksukortti = Maksukortti(390)

        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))

    def test_jos_edullinen_lounas_ostetaan_kortilla_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_jos_maukas_lounas_ostetaan_kortilla_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    # Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_kortille_rahaa_ladattaessa_kassassa_oleva_rahamaara_muuttuu_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.0)

    def test_jos_kortille_ladattava_rahamaara_on_negatiivinen_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_jos_kortille_ladattava_rahamaara_on_negatiivinen_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
