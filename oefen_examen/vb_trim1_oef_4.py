""" Oefening 4 (   / 4)
DOEL:
Bepaal wanneer de zon opkomt en ondergaat op basis van de locatie van de gebruiker.
Gebruik hiervoor de api van website 'sunrisesunset.io'.

DOCUMENTATIE: !! scroll naar beneden op pagina voor request voorbeelden !!
https://sunrisesunset.io/api/

VRAAG:
Vraag de gebruiker naar zijn positie (latitude en longitude).
Print volgende zin voor deze positie.
    De zon komt op om **tijd_opkomst** en gaat onder om **tijd_ondergaan**. 


Geeft de gebruiker een verkeerde waarde in? 
Print dan de foutmelding van de api (zie voorbeeld).
"""

""" VOORBEELD (lat = 51, lng = 4.5) ==> Belgie
De zon komt op om 8:30:57 AM en gaat onder om 4:38:03 PM. 
"""

""" VOORBEELD (lat = -25, lng = 145) ==> Australie
De zon komt op om 5:23:50 AM en gaat onder om 7:00:51 PM. 
"""

""" VOORBEELD (lat = -100, lng = 0) ==> FOUT LATITUDE
Latitude must be between -90 and 90 degrees
"""

""" VOORBEELD (lat = 0, lng = 500) ==> FOUT LONGITUDE
Longitude must be between -180 and 180 degrees
"""