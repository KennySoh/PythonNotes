from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 


class Investment(App):
    def build(self):
        layout= GridLayout(cols=2)
        self.investment = Label(text="Investment Amount",font_size=35,halign='left',valign='middle')
        layout.add_widget(self.investment)
        self.investment_input = TextInput(multiline= False, font_size=35, halign='center',valign='middle')
        layout.add_widget(self.investment_input)
        self.years = Label(text='Years',font_size=35,halign='left',valign='middle')
        layout.add_widget(self.years)
        self.years_input = TextInput(multiline= False, font_size=35, halign='center',valign='middle')   
        layout.add_widget(self.years_input)
        self.interest_rate = Label(text='Investment Rate', font_size=35, halign='center',valign='middle')
        layout.add_widget(self.interest_rate)
        self.interest_rate_input = TextInput(multiline= False, font_size=35, halign='center',valign='middle')   
        layout.add_widget(self.interest_rate_input)
        self.future_value = Label(text='Future Value', font_size=35, halign='center',valign='middle')
        layout.add_widget(self.future_value)
        self.txt_future_val = Label(text = '0' ,font_size=35, halign='center',valign='middle' )
        layout.add_widget(self.txt_future_val)
        self.button = Button(text="Calculate", on_press=self.calculate, font_size=24)
        layout.add_widget(self.button)
        return layout
    
    def calculate(self, instance):
        inv_amt = float(self.investment_input.text)
        years = float(self.years_input.text)
        mth_int_rate = float(self.interest_rate_input.text)
        self.txt_future_val.text= str(inv_amt*(1+mth_int_rate)**(12.0*years))




Investment().run()