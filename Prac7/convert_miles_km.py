from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

Miles_to_km = 1.60934


class MilesConverter(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * Miles_to_km)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverter().run()
