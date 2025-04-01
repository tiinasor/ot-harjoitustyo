# Ohjelmistotekniikka, harjoitustyö

**Juoksusovellus**, jonka avulla käyttäjä voi pitää kirjaa *treeneistään*.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```


## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelmaa ei pysty vielä suorittamaan, koska sillä ei ole käyttöliittymää.

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
