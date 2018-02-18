from kivy.app import App
from kivy.uix.label import Label 

class SlideDetectApp(App):
    def build(self):
        self.label=Label(text = "I LIKE TO MOVE IT MOVE IT! ", on_touch_move = self.detect)#change here
        return self.label

    def detect(self, instance, touch):
        if touch.dx<-40:
            self.label.text = "Slide Left"
            pass
        if touch.dx>40:
            self.label.text = "Slide Right"  
            pass
        if touch.dy<-40:
            self.label.text = "Slide Down"
            pass    
        if touch.dy>40:
            self.label.text = "Slide Up"
            pass
        return True

if __name__=='__main__':
	SlideDetectApp().run()