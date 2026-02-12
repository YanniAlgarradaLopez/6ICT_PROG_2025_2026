""" Voorbeelden (API geeft enkel Engelse zinnen terug):

Advies 1:
    Input || Topic for advice: spiders
    Print || Remember that spiders are more afraid of you, than you are of them.
Advies 2:
    Input || Topic for advice: teeth
    Print || You don't need to floss all of your teeth. Only the ones you want to keep.
Advies 3:
    Input || Topic for advice: programming
    Print || No advice slips found matching that search term.

"""
import requests

query = input("Topic for advice: ")
response_json = requests.get(f"")

