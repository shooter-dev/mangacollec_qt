import random

class PagesUtils:
    @staticmethod
    def generer_background_color(d=128, f=255):
        r = random.randint(d, f)
        g = random.randint(d, f)
        b = random.randint(d, f)

        return f"background-color: #{r:02X}{g:02X}{b:02X};"

    @staticmethod
    def generer_random_color_hex():
        r = random.randint(128, 255)
        g = random.randint(128, 255)
        b = random.randint(128, 255)

        return f"#{r:02X}{g:02X}{b:02X};"