
# clickLinks (Python)

Easily create clickable links with different title in python.

## (You can open them with ctrl + click, see last image)

![Preview](https://raw.githubusercontent.com/NexusKiwiii/clickLinksPython/main/previews/preview.png)

## Installation

You can use it as a lib:\
`from clickLink import clickLink`

Or you copy paste parts of it:
```python
def clickLink(url, text):
  return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"
```

## Usage

You can use multiple ways:

```python
googleLinkObject = clickLink("https://google.com", "Google link")  # Here we have the class object


googleLinkUrl = clickLink("https://google.com", "Google link").url()  # Here we already have the string
```
So we use url() to get the string of a object.

```python
print(f'Google link here: {clickLink("https://google.com", "Google").url()}') # Create inside of print function
print(f"Another google link here (object): {googleLinkObject.url()}")         # Create object before and extract url in print function
print(f"Another google link here (string): {googleLinkUrl}")                  # We use the string which we extracted before in the googleLinkUrl variable
```


![When hovering](https://raw.githubusercontent.com/NexusKiwiii/clickLinksPython/main/previews/onHover.png)
