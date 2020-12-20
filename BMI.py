import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button

Window.clearcolor=(0,0,102/255.0,1)

class Main(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label())
        self.add_widget(Label(text='BMI CALCULATOR',font_size=29))
        self.add_widget(Label(text='MASS IN KILOGRAMS',))
        self.mass=TextInput(multiline=False)
        self.add_widget(self.mass)
        self.add_widget(Label(text='HEIGHT IN METRES',))
        

        self.h=TextInput(multiline=False)
        self.add_widget(self.h)
        
        self.add_widget(Label())
        self.submit=Button(text='FIND MY BMI',font_size=25,background_color=(0,0,50/255.0,1))
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.bmi_calc)

    def bmi_calc(self,instance):
        m=self.mass.text
        h=self.h.text
        m=float(m)
        h=float(h)
        bmi_c=m/h**2

        if bmi_c>=20 and bmi_c<=25:
            ans=f'YOUR BMI IS {bmi_c} AND YOUR NORMAL'
            bmi.home.update_text(ans)
            bmi.sm.current='home'

        elif bmi_c<20:
            ans=f'YOUR BMI IS {bmi_c} AND YOUR UNDERWEIGHT'
            bmi.home.update_text(ans)
            bmi.sm.current='home'

        elif bmi_c>=26 and bmi_c<=30:
            ans=f'YOUR BMI IS {bmi_c} AND YOUR OVERWEIGHT'
            bmi.home.update_text(ans)
            bmi.sm.current='home'

        elif bmi_c>30:
            ans=f'YOUR BMI IS {bmi_c} AND YOUR OBESE'
            bmi.home.update_text(ans)
            bmi.sm.current='home'

       
class Home(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.add_widget(Label())
        self.add_widget(Label())

        self.message=Label(font_size=20)
        self.add_widget(self.message)

        self.back=Button(text='GO BACK',background_color=(0,0,102/255.0,1))
        self.add_widget(self.back)
        self.back.bind(on_press=self.gh)

        self.add_widget(Label())

    def gh(self,instance):
        bmi.sm.current='main'

    def update_text(self, message):
        self.message.text=message
        

class BMIApp(App):
    def build(self):
        self.sm=ScreenManager()

        self.main=Main()
        screen=Screen(name='main')
        screen.add_widget(self.main)
        self.sm.add_widget(screen)

        self.home=Home()
        screen=Screen(name='home')
        screen.add_widget(self.home)
        self.sm.add_widget(screen)

        return self.sm

if __name__=='__main__':
    bmi=BMIApp()
    bmi.run()
