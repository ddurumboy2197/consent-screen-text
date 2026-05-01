class ConsentScreen:
    def __init__(self, language):
        self.language = language

    def get_text(self):
        if self.language == "uz":
            return "Mening ma'lumotlarimni qabul qilish"
        elif self.language == "ru":
            return "Принятие данных"
        elif self.language == "en":
            return "Data Consent"
        else:
            return "Unknown language"

class App:
    def __init__(self):
        self.consent_screen = ConsentScreen("uz")

    def get_consent_screen_text(self):
        return self.consent_screen.get_text()

app = App()
print(app.get_consent_screen_text())

# Uzbek
print(app.get_consent_screen_text(language="uz"))

# Russian
print(app.get_consent_screen_text(language="ru"))

# English
print(app.get_consent_screen_text(language="en"))
```

```python
class ConsentScreen:
    def __init__(self, language):
        self.language = language

    def get_text(self):
        if self.language == "uz":
            return "Mening ma'lumotlarimni qabul qilish"
        elif self.language == "ru":
            return "Принятие данных"
        elif self.language == "en":
            return "Data Consent"
        else:
            return "Unknown language"

class App:
    def __init__(self):
        self.consent_screen = ConsentScreen("uz")

    def get_consent_screen_text(self, language="uz"):
        return self.consent_screen.get_text(language)

app = App()
print(app.get_consent_screen_text())

# Uzbek
print(app.get_consent_screen_text("uz"))

# Russian
print(app.get_consent_screen_text("ru"))

# English
print(app.get_consent_screen_text("en"))
