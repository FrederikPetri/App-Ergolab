from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from jnius import autoclass

class MainApp(App):
    def build(self):
        self.button = Button(text="Hello World")
        self.button.bind(on_press=self.callback)
        return self.button

    def callback(self, instance):

        sdk_version = autoclass('XsensDotSdk.getSdkVersion()')

        popup = Popup(title="success",
                      content=Label(text=sdk_version),
                      size=(100, 100),
                      size_hint=(0.3, 0.3),
                      auto_dismiss=False)
        popup.open()

MainApp().run()