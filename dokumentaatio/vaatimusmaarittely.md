# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla juoksua harrastava käyttäjä voi pitää kirjaa treeneistään. Sovellukseen voi rekisteroityä useita käyttäjiä, joista kukin pitää kirjaa yksilöllisistä treeneistään.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään uuden tunnuksen.
    - Tunnuksen tulee olla uniikki ja 1-20 merkkiä pitkä.
    - Salasanan tulee olla vähintään 8 merkkiä pitkä.
    - Järjestelmä ilmoittaa käyttäjälle jos tunnus on jo käytössä tai jos tunnuksen tai salasana pituus on väärä.
- Käyttäjä voi kirjautua järjestelmään.
    - Järjestelmä ilmoittaa käyttäjälle jos käyttäjätunnusta ei löydy tai käyttäjätunnus ja salasana eivät täsmää.

### Kirjautumisen jälkeen

- Käyttäjä voi lisätä merkinnän treenistään.
    - Merkintä sisältää ainakin seuraavat tiedot: päivämäärä, treenin kesto, juostun matkan pituus.
- Käyttäjä voi tarkastella omia treenimerkintöjään.
- Käyttäjä voi poistaa treenimerkinnän.
- Käyttäjä voi kirjautua ulos järjestelmästä.

## Jatkokehitysideoita

Perusversion toteuttamisen jälkeen järjestelmää on tarkoitus täydentää seuraavilla toiminnallisuuksilla:
- Käyttäjä voi muokata treenimerkintöjään niiden lisäämisen jälkeen.
- Käyttäjä voi tarkastella tilastoja treeneistään.
    - Esim. montako kertaa viikossa, kuukaudessa tai vuodessa on treenannut ja kuinka monta kilometriä on juossut.
- Käyttäjä voi asettaa itselleen tavoitteita ja seurata niiden toteutumista.
    - Esim. juokse 3 kertaa viikossa, juokse 10 km.
- Käyttäjä voi poistaa oman tunnuksensa ja siihen liittyvät treenimerkinnät.
