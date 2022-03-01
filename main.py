from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.config import ConfigParser
import ast

global user_name
# самый первый экран
class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bl_main = BoxLayout(orientation='vertical', padding=20, spacing=40)
        anc_main = AnchorLayout(anchor_x='center', anchor_y='center', padding=80)

        lbl_main = Label(text='[color=66CC00]Тест[/color] [color=FFFF66]на[/color] [color=FF0000]я[/color][color=FF8000]о[/color][color=FFFF00]й[/color][color=80FF00]щ[/color][color=00FFFF]и[/color][color=0080FF]к[/color][color=7F00FF]а[/color]\n',
            font_size='50sp', markup=True)
        btn_welcome = Button(text='Начать', font_size='50sp', size_hint=(None, None), size=[350, 150],
                         background_color='FF99CC',
                         background_normal='',
                         on_press=self.start_test)

        bl_main.add_widget(lbl_main)
        anc_main.add_widget(btn_welcome)
        bl_main.add_widget(anc_main)
        self.add_widget(bl_main)

    def start_test(self, *args):
        self.manager.transition.direction='left'
        self.manager.current='name_screen'


class SubmitScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        fl_test = FloatLayout()
        lbl_test_name = Label(text='Введите ваше имя:', font_size='40sp', size_hint=(None, None), size=[200, 100], pos=(300,420))
        self.user_name = TextInput(hint_text='кликай сюда', font_size='40sp', size_hint=(None, None), size=[600, 60], pos=(85, 360),
                                   cursor_color=[102/255,0,102/255],
                                   cursor_width='2sp',
                                   halign='center',
                                   background_color=[1, 229/255, 204/255], background_disabled_normal='', background_active='', cursor_blink=True)
        btn_test = Button(text='Далее', font_size='50sp', size_hint=(None, None), size=[350, 100], pos=(225,210),
                         background_color='FF99CC',
                         background_normal='',
                         on_press=self.start_test)

        user_name = ast.literal_eval(
            App.get_running_app().config.get('General', 'user_name'))
        self.user_name.bind(text=self.on_text)

        fl_test.add_widget(lbl_test_name)
        fl_test.add_widget(self.user_name)
        fl_test.add_widget(btn_test)

        self.add_widget(fl_test)

    def on_text(self, *args):
        data=self.user_name.text
        if data=='Алена' or data=='алена\n':
            self.manager.transition.direction='right'
            self.manager.current='alena'

    def start_test(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'test_screen'

    def get_name(self):
        return self.user_name.text

class TestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bl = GridLayout(rows=3)
        lbl = Label(text='Ты читаешь [color=FF0000]я[/color][color=FF8000]о[/color][color=FFFF00]й[/color][color=0000FF]?[/color]', font_size='50sp', markup=True)
        gr = BoxLayout(orientation='horizontal',spacing=30, padding=100)

        btn1 = Button(text='[color=0000FF]Да[/color]', size_hint=(None, None), width=250, height=100,
                     font_size='30sp', halign='center',
                     background_color=[153/255,204/255,1],
                     background_normal='',
                    # on_press=self.yes_screen,
                     markup=True)
       # btn1.bind(on_press=self.yes_screen)
        gr.add_widget(btn1)
        gr.add_widget(Button(text='[color=0000FF]Нет[/color]',size_hint=(None, None), width=250, height=100,
                     font_size='30sp', halign='center',
                     background_color=[153/255,204/255,1],
                     background_normal='',
                     #on_press=self.no_screen(),
                     markup=True))
        fl = FloatLayout()
        btn = fl.add_widget(Button(text='[color=0000FF]Что такое[/color] [color=FF0000]я[/color][color=FF8000]о[/color][color=FFFF00]й[/color][color=0000FF]?[/color]',
                     font_size='30sp', size_hint=(None, None), width=400, height=100, pos=(190,80),
                     background_color=[153/255,204/255,1],
                     background_normal='',
                     on_press=self.what_screen,
                     markup=True))

        bl.add_widget(lbl)
        bl.add_widget(gr)
        bl.add_widget(fl)

        self.add_widget(bl)

    def yes_screen(self, *args):
        self.manager.transition.direction='left'
        self.manager.current='yes_screen'

    def no_screen(self, *args):
        pass
        #self.manager.transition.direction='left'
        #self.manager.current='no_screen'

    def what_screen(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'what_screen'

class Alena(Screen):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()

        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'user_data'))
        print(self.app.user_data)

class WhatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout=GridLayout(rows=2)
        first_layout=AnchorLayout(padding=100, anchor_x='center', anchor_y='center')
        text=Label(text='[color=FF0000]Я[/color][color=FF8000]о[/color][color=FFFF00]й[/color] - жанр манги и аниме,\n'
                        ' изображающий гомосексуальные отношения\n '
                        'между мужчинами. Целевой аудиторией\n '
                        'яоя и авторами яойной манги являются девушки\n'
                        ' и женщины, как правило, [color=66B2FF]гетеросексуальные[/color].',
                   font_size='30sp', halign='center', markup=True,
                   size_hint=(None, None), width=100, height=10)
        return_btn = Button(text='[color=FF00FF]Вернуться назад[/color]', font_size='35sp',
                            size_hint=(None, None), width=300, height=100,
                            background_color='FFCCFF', markup=True,
                            background_normal='',
                            on_press=self.go_back)

        second_layout=AnchorLayout(anchor_x='center', anchor_y='center')
        second_layout.add_widget(return_btn)


        first_layout.add_widget(text)
        main_layout.add_widget(first_layout)
        main_layout.add_widget(second_layout)
        self.add_widget(main_layout)

    def go_back(self, args):
        self.manager.transition.direction='right'
        self.manager.current='test_screen'


class MyApp(App):
    def press(self, instance):
        if self.user_name.text == 'Алена' or self.user_name.text=='алена':
            instance.text = '[color=FF66FF]это был риторический вопрос[/color]'
            instance.font_size = '20sp'
            instance.background_color=[1,224/255,229/255]
            instance.background_normal=''
            instance.markup=True

        elif self.user_name.text=='егор' or self.user_name.text=='Егор':
            instance.text = '[color=FF66FF]не ври[/color]'
            instance.background_color = [1, 224 / 255, 229 / 255]
            instance.font_size = '20sp'
            instance.markup = True

        elif self.user_name.text=='лиза' or self.user_name.text=='Лиза':
            instance.text = '[color=FF66FF]это останется строго между нами![/color]'
            instance.background_color = [1, 224 / 255, 229 / 255]
            instance.font_size = '20sp'
            instance.markup = True

        else:
            instance.text='Алена и тебя завербовала\n в свою группу яойщиков?\n (это риторический вопрос)'
            instance.font_size = '20sp'
            instance.background_color = [204/255, 204 / 255, 1]

    def press_no(self, instance):
        if self.user_name.text == 'Алена' or self.user_name.text=='алена':
            instance.text='[color=FF66FF]WHAT\'S THIS?!\n (покажите ваш мангалиб, дамочка)[/color]'
            instance.halign = 'center'
            instance.background_color = [1, 224 / 255, 229 / 255]
            instance.font_size='20sp'
            instance.markup = True

        elif self.user_name.text=='егор' or self.user_name.text=='Егор':
            instance.text = '[color=FF66FF]верю на слово[/color]'
            instance.background_color = [1, 224 / 255, 229 / 255]
            instance.font_size = '20sp'
            instance.markup = True

        elif self.user_name.text=='лиза' or self.user_name.text=='Лиза':
            instance.text = '[color=FF66FF]ладно....\n(а зря!)[/color]'
            instance.background_color = [1, 224 / 255, 229 / 255]
            instance.font_size = '20sp'
            instance.markup = True
        else:
            instance.text='молодец!\n скорее закрывай этот тест, \nчтобы Алена не увидела'
            instance.font_size='20sp'
            instance.halign = 'center'

    def press_what(self, instance):
        if self.user_name.text =='алена' or self.user_name.text == 'Алена':
            instance.text = '[color=FF66FF]подруга, а ты шо тут забыла?[/color]'
            instance.font_size = '20sp'
            instance.background_color = [1, 224 / 255, 229 / 255]

        elif self.user_name.text=='егор' or self.user_name.text=='Егор':
            instance.text = '[color=FF66FF]егорушка, если тебя заставили пройти этот тест,\n моргни трижды[/color]'
            instance.font_size = '20sp'
            instance.halign='center'
            instance.background_color = [1, 224 / 255, 229 / 255]

        elif self.user_name.text=='лиза' or self.user_name.text=='Лиза':
            instance.text = '[color=FF66FF]подруга...\nдобро пожаловать![/color]'
            instance.font_size = '20sp'
            instance.halign='center'
            instance.background_color = [1, 224 / 255, 229 / 255]

        else:
            instance.text = '[color=FF66FF]это началось еще во времена Христа...[/color]'
            instance.font_size = '20sp'
            instance.halign = 'center'
            instance.background_color = [1, 224 / 255, 229 / 255]

    def build(self):
        sm=ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(SubmitScreen(name='name_screen'))
        sm.add_widget(TestScreen(name='test_screen'))
        sm.add_widget(Alena(name='alena'))
        sm.add_widget(WhatScreen(name='what_screen'))


        return sm

    def build1(self):
        gr = GridLayout()
        bl_main = BoxLayout(orientation='vertical', padding=30, spacing=20)
        bl_first = BoxLayout(orientation='horizontal', spacing=20)

        lbl = Label(text='[color=66CC00]Тест[/color] [color=FFFF66]на[/color] [color=FF0000]я[/color][color=FF8000]о[/color][color=FFFF00]й[/color][color=80FF00]щ[/color][color=00FFFF]и[/color][color=0080FF]к[/color][color=7F00FF]а[/color]\n',
        font_size='50sp', markup=True)
        lbl2=Label(text='Введите ваше имя:', font_size='40sp')
        lbl3 = Label(text='Ты читаешь яой?', font_size='20sp')
        self.user_name = TextInput(hint_text='кликай сюда',
                                   font_size='40sp',
                                   cursor_color=[102/255,0,102/255],
                                   cursor_width='2sp',
                                   halign='center',
                                   background_color=[1, 229/255, 204/255], background_disabled_normal='', background_active='', cursor_blink=True)


        bt1 = Button(text='[color=0000FF]Да[/color]',
                     font_size='30sp',
                     background_color=[153/255,204/255,1],
                     background_normal='',
                     on_press=self.press,
                     markup=True)
        bt2 = Button(text='[color=0000FF]Нет[/color]',
                     font_size='30sp',
                     background_color=[153/255,204/255,1],
                     background_normal='',
                     on_press=self.press_no,
                     markup=True)
        btn3 = Button(text='[color=0000FF]Что такое[/color] [color=FF0000]я[/color][color=FF8000]о[/color][color=FFFF00]й[/color][color=0000FF]?[/color]',
                     font_size='30sp',
                     background_color=[153/255,204/255,1],
                     background_normal='',
                     on_press=self.press_what,
                     markup=True)

        bl_main.add_widget(lbl)
        bl_main.add_widget(lbl2)
        bl_main.add_widget(self.user_name)
        bl_main.add_widget(lbl3)
        bl_main.add_widget(bl_first)
        bl_main.add_widget(btn3)

        bl_first.add_widget(bt1)
        bl_first.add_widget(bt2)
        return bl_main



MyApp().run()
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from datetime import datetime
import os
import ast
import time


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='Дневник питания', on_press=lambda x:
                              set_screen('list_food')))
        box.add_widget(Button(text='Добавить блюдо в дневник питания',
                              on_press=lambda x: set_screen('add_food')))
        self.add_widget(box)


class SortedListFood(Screen):
    def __init__(self, **kw):
        super(SortedListFood, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана

        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Назад в главное меню',
                             on_press=lambda x: set_screen('menu'),
                             size_hint_y=None, height=dp(40))
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)

        dic_foods = ast.literal_eval(
            App.get_running_app().config.get('General', 'user_data'))

        for f, d in sorted(dic_foods.items(), key=lambda x: x[1]):
            fd = f.decode('u8') + ' ' + (datetime.fromtimestamp(d).strftime('%Y-%m-%d'))
            btn = Button(text=fd, size_hint_y=None, height=dp(40))
            self.layout.add_widget(btn)

    def on_leave(self):  # Будет вызвана в момент закрытия экрана

        self.layout.clear_widgets()  # очищаем список


class AddFood(Screen):

    def buttonClicked(self, btn1):
        if not self.txt1.text:
            return
        # Return the currently running application instance.
        self.app = App.get_running_app()

        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'user_data'))
        self.app.user_data[self.txt1.text.encode('u8')] = int(time.time())

        self.app.config.set('General', 'user_data', self.app.user_data)
        self.app.config.write()

        text = "Последнее добавленное блюдо:  " + self.txt1.text
        self.result.text = text
        self.txt1.text = ''

    def __init__(self, **kw):
        super(AddFood, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        back_button = Button(text='< Назад в главное меню', on_press=lambda x:
                             set_screen('menu'), size_hint_y=None, height=dp(40))
        box.add_widget(back_button)
        self.txt1 = TextInput(text='', multiline=False, height=dp(40),
                              size_hint_y=None, hint_text="Название блюда")
        box.add_widget(self.txt1)
        btn1 = Button(text="Добавить блюдо", size_hint_y=None, height=dp(40))
        btn1.bind(on_press=self.buttonClicked)
        box.add_widget(btn1)
        self.result = Label(text='')
        box.add_widget(self.result)
        self.add_widget(box)


def set_screen(name_screen):
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SortedListFood(name='list_food'))
sm.add_widget(AddFood(name='add_food'))


class FoodOptionsApp(App):
    def __init__(self, **kvargs):
        super(FoodOptionsApp, self).__init__(**kvargs)
        self.config = ConfigParser()

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'user_data', '{}')

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'user_data'))

    def get_application_config(self):
        return super(FoodOptionsApp, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))

    def build(self):
        return sm


if __name__ == '__main__':
    FoodOptionsApp().run()
    
"""