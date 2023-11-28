from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


# add buttons to click to input numbers and operators and calculate the result
class CalculatorApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical', padding=25)
        self.txt_input = TextInput(font_size=25, size_hint=(1, .75), multiline=False)
        buttons = [["7", "8", "9", "/"],
                   ["4", "5", "6", "*"],
                   ["1", "2", "3", "-"],
                   [".", "0", "C", "+"]]
        for row in buttons:
            hbl = BoxLayout(padding=25)
            for label in row:
                button = Button(text=label, font_size=25, size_hint=(1, .75))
                button.bind(on_press=self.on_button_press)
                hbl.add_widget(button)
            bl.add_widget(hbl)

        self.formula = ""

        bl.add_widget(self.txt_input)
        bl.add_widget(Button(text="Calculate", font_size=25, size_hint=(1, .25), on_press=self.calculate))
        return bl


    def on_button_press(self, instance):
        if instance.text == "C":
            self.txt_input.text = ""
        else:
            self.txt_input.text += instance.text


    def calculate(self, instance):
        try:
            self.formula = self.txt_input.text
            self.txt_input.text = str(eval(self.formula))
        except Exception:
            self.txt_input.text = "Error"


if __name__ == "__main__":
    CalculatorApp().run()
