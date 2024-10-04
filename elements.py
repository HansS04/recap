class HTMLElement:
    def __init__(self, tag_name, attributes=None, inner_content=""):
        self.tag_name = tag_name  # Název HTML tagu (např. "div", "a", "img")
        self.attributes = attributes or {}  # Atributy elementu (např. "href", "src")
        self.inner_content = inner_content  # Vnitřní obsah elementu (např. text v "div")

    def set_attribute(self, key, value):
        self.attributes[key] = value  # Nastavuje atribut elementu (např. href="https://")

    def render(self):
        # Vytváří HTML string s atributy a obsahem
        attrs = " ".join(f'{key}="{value}"' for key, value in self.attributes.items())
        return f"<{self.tag_name} {attrs}>{self.inner_content}</{self.tag_name}>\n"

class Input(HTMLElement):
    def __init__(self, input_type="text", name="", value=""):
        super().__init__("input")  # Inicializuje element typu "input"
        self.set_attribute("type", input_type)  # Nastaví typ inputu (např. "text", "password")
        self.set_attribute("name", name)  # Nastaví jméno atributu inputu (např. "username")
        self.set_attribute("value", value)  # Nastaví výchozí hodnotu inputu

    def render(self):
        # Vytváří HTML pro input element s atributy, uzavírá ho samo-uzavírajícím tagem
        attrs = " ".join(f'{key}="{value}"' for key, value in self.attributes.items())
        return f"<input {attrs} />\n"

class Select(HTMLElement):
    def __init__(self, name="", options=None):
        super().__init__("select")  # Inicializuje element typu "select"
        self.set_attribute("name", name)  # Nastaví jméno selectu
        self.options = options or []  # Pole možností (např. ["USA", "Canada"])

    def render(self):
        # Vytváří HTML pro možnosti v elementu "select"
        options_html = "".join(f'<option value="{opt}">{opt}</option>\n' for opt in self.options)
        attrs = " ".join(f'{key}="{value}"' for key, value in self.attributes.items())
        return f"<select {attrs}>\n{options_html}</select>\n"

class A(HTMLElement):
    def __init__(self, href="#", text=""):
        super().__init__("a", inner_content=text)  # Inicializuje element typu "a" s textem uvnitř
        self.set_attribute("href", href)  # Nastaví "href" atribut pro odkaz

class Img(HTMLElement):
    def __init__(self, src="", alt=""):
        super().__init__("img")  # Inicializuje element typu "img"
        self.set_attribute("src", src)  # Nastaví "src" atribut (odkaz na obrázek)
        self.set_attribute("alt", alt)  # Nastaví "alt" atribut (alternativní text)

    def render(self):
        # Vytváří HTML pro obrázek jako samo-uzavírající tag
        attrs = " ".join(f'{key}="{value}"' for key, value in self.attributes.items())
        return f"<img {attrs} />\n"

class Div(HTMLElement):
    def __init__(self, inner_content=""):
        super().__init__("div", inner_content=inner_content)  # Inicializuje element typu "div" s obsahem uvnitř

class Form(HTMLElement):
    def __init__(self, action="", method="post"):
        super().__init__("form")  # Inicializuje element typu "form"
        self.set_attribute("action", action)  # Nastaví "action" atribut (kam bude formulář odeslán)
        self.set_attribute("method", method)  # Nastaví metodu odeslání formuláře (např. POST)
        self.elements = []  # Pole elementů formuláře

    def add_element(self, element):
        self.elements.append(element)  # Přidá element do formuláře

    def render(self):
        # Vytváří HTML pro všechny elementy uvnitř formuláře
        form_content = "".join(element.render() for element in self.elements)
        attrs = " ".join(f'{key}="{value}"' for key, value in self.attributes.items())
        return f"<form {attrs}>\n{form_content}</form>\n"

# Vytvoříme objekt formuláře s akcí "/submit" a metodou "post"
form = Form(action="/submit", method="post")

# Přidáme input pro uživatelské jméno
form.add_element(Input(input_type="text", name="username", value="Enter username"))
# Přidáme input pro heslo
form.add_element(Input(input_type="password", name="password", value=""))

# Přidáme select s možnostmi států
form.add_element(Select(name="country", options=["USA", "Canada", "Mexico"]))

# Přidáme odkaz (anchor tag)
form.add_element(A(href="https://olc.cz", text="OLC Systems"))

# Přidáme obrázek
form.add_element(Img(src="olc_logo.svg", alt="Example Image"))

# Přidáme div s jednoduchým textem
div = Div(inner_content="This is a simple form.")
form.add_element(div)

# Vytvoříme celý HTML dokument s vloženým formulářem
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Form</title>
</head>
<body>
{form.render()}
</body>
</html>
"""

# Uložíme výstup do souboru "output.html"
with open("output.html", "w") as file:
    file.write(html_content)

print("Output was saved to - output.html.")
