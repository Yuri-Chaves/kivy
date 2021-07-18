# Métodos de inicializar aplicações:

# 1º Método (não recomendável por faltar mais inicializações)
# from kivy.base import runTouchApp
# from kivy.uix.button import Button
# runTouchApp(Button(text = "Hello Word From Kivy"))

# 2º Método
# from kivy.app import App
# from kivy.uix.button import Button

# class MainApp(App):
#     def build(self):
#         return Button(text = "Hello Word From Kivy")
# MainApp().run()