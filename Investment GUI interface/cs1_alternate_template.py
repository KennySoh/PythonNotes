from kivy.app import App 
from kivy.uix.label import Label  

class AlternateApp(App):
	
	def build(self):
         self.count=0
         self.label=Label(on_touch_down=self.alternate)
         return self.label

	def alternate(self,instance, touch):
         self.count+=1
         if self.count%2==0:
             self.label.text="Programming is fun"
         else:
             self.label.text="It is fun to program"

myapp=AlternateApp()
myapp.run()