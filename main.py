# Uno de los problemas es que si importas Kivy de una, pesa un monton solo los paquetes, asi que hay que importar individualmente lo que necesites. (14/02/24)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


# La siguiente linea de codigo importa el .kv que contiene todos los detalles esteticos (frontend) de la app, mientras que el main.py contiene el backend.(14/02/24)
kv = Builder.load_file('mm_props.kv')

# Las siguientes clases son las diferentes pantallas de la app (14/02/24)

class Menu(Screen):
    pass

class Settings(Screen):
    pass

class Recipes(Screen):
    pass

class Inventory(Screen):
    pass

# La siguiente clase crea el entorno completo de la app. (14/02/24)
class MealMasterApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Settings(name='settings'))
        sm.add_widget(Recipes(name='recipes'))
        sm.add_widget(Inventory(name='inventory'))
        return sm

# La siguiente funcion ejecuta la app. (14/02/24)
if __name__ == '__main__':
    MealMasterApp().run()