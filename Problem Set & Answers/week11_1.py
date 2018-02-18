from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.label=Label (text="Hello Cohort 7",on_touch_event=self.alternate)
        return self.label
        
    def alternate(self, instance, touch):
        self.label.text="Hi ... Hi ..."
        
        
MyApp().run()