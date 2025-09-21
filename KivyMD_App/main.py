from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout


class KivyMD_App(MDApp):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        # A Material Design Label
        self.label = MDLabel(
            text="Hello, KivyMD!",
            halign="center",
            theme_text_color="Primary"
        )

        # A Material Design Button
        btn = MDRaisedButton(
            text="Click Me",
            pos_hint={"center_x": 0.5},
            on_release=self.change_text
        )

        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def change_text(self, instance):
        self.label.text = "You clicked the button!"


if __name__ == "__main__":
    KivyMD_App().run()