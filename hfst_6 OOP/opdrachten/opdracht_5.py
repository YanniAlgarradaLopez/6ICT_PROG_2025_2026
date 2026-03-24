""" THERMOMETER UITLEG
Je krijgt hieronder een korte beschrijving van een temperatuursensor.
Maak op basis van deze beschrijving een klasse met correcte eigenschappen en methoden.
Maak ook een object aan van deze klasse waarin je alle onderdelen van de sensor test.

Bij het aanmaken van de sensor geef je een ondergrens en bovengrens voor de temperatuur mee.
De temperatuursensor moet volgende zaken kunnen:
    - Meet een temperatuur (simuleer dit door een willekeurige waarde te genereren tussen 0°C en 50°C).
    - Een waarschuwingsmelding tonen als de temperatuur buiten de grenzen valt.
    - De huidige temperatuur en status van de sensor controleren (oke, koud of warm).
    - Het herkalibereren van de ondergrens en bovengrens.
    
Belangrijk! Bij elke actie moet duidelijk aangegeven worden wat er gebeurt.
"""


""" THERMOMETER VOORBEELD (ondergrens 10°C en bovengrens 30°C)
De gebruiker meet een temperatuur, het is nu 25°C

De gebruiker controleert de huidige temperatuur.
De temperatuur van 25°C is oke.

De gebruiker meet een temperatuur, het is nu 8°C.
WAARSHUWING! Temperatuur ligt buiten de grens

De gebruiker controleert de huidige temperatuur.
De temperatuur van 8°C is te koud.

De gebruiker stelt nieuw grenzen in: 5°C en 40°C

De gebruiker controleert de huidige temperatuur.
De temperatuur van 8°C is oke.

De gebruiker meet een temperatuur, het is nu 44°C
WAARSHUWING! Temperatuur ligt buiten de grens

De gebruiker controleert de huidige temperatuur.
De temperatuur van 44°C is te warm.
"""
