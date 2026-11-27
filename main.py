from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AnnaAI(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.output = Label(
            text="Namaste! Main Anna AK AI hoon.",
            font_size=20
        )

        self.message = TextInput(
            hint_text="Apna message likhein",
            size_hint_y=None,
            height=50
        )

        send = Button(
            text="Send",
            size_hint_y=None,
            height=50
        )
        send.bind(on_press=self.reply)

        layout.add_widget(self.output)
        layout.add_widget(self.message)
        layout.add_widget(send)

        return layout

    def reply(self, instance):
        text = self.message.text
        self.output.text = "Aapne kaha: " + text
        self.message.text = ""

AnnaAI().run() 
