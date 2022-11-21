classDiagram
    class Ruutu
    class Pelilauta
    class Pelinappula
    class Pelaaja
    class Noppa
    class Toiminto
    class Kortti
    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma_ja_yhteismaa
    Ruutu <|-- Asemat_ja_laitokset
    Ruutu <|-- Normaalit_kadut
    Pelilauta "1" --> "40" Ruutu
    Pelaaja "1" --> "1" Pelinappula
    Pelinappula "1" --> "1" Ruutu
    Pelilauta "1" --> "2" Noppa
    Ruutu "1" --> "1" Ruutu
    Pelilauta "1" --> "2..8" Pelaaja
    Ruutu "1" --> "1" Toiminto
    Sattuma_ja_yhteismaa "1" --> "*" Kortti
    Kortti "1" --> "1" Toiminto
    Normaalit_kadut "1" --> "0..1" Pelaaja
    Normaalit_kadut : +int talot
    Normaalit_kadut : +bool hotelli
    Pelaaja : +int rahaa
