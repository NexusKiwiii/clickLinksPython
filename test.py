from clickLink import clickLink
from time import sleep
from os import system


googleLinkObject = clickLink(
    "https://google.com", "Google link"
)  # Here only the class object

googleLinkUrl = clickLink(
    "https://google.com", "Google link"
).url()  # Here we already have the string

print(f'Google link here: {clickLink("https://google.com", "Google").url()}')
print(f"Another google link here (object): {googleLinkObject.url()}")
print(f"Another google link here (string): {googleLinkUrl}")
sleep(1000)
system("pause")
