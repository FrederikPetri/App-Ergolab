from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, \
    IconLeftWidget, ImageLeftWidget, ThreeLineAvatarListItem
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (300,500) # Remember to remove when building app


class ErgolabApp(MDApp):
    def build(self):
        # Change theme options
        self.theme_cls.primary_palette = "Green"  # Theme colors
        self.theme_cls.primary_hue = "200"  # Opacity of colors
        self.theme_cls.theme_style = "Light"  # Theme style

        screen = Screen()


        # Create label
        label = MDLabel(text='Hello world', halign='center', theme_text_color='Custom',
                        text_color=(61 / 255, 200 / 255, 100 / 255, 1), font_style='H2')

        # Create icon
        icon_label = MDIcon(icon='chart-pie', halign='center')

        # Create flat button
        btn_flat = MDRectangleFlatButton(text='Hello World',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Create icon button
        btn_icon = MDIconButton(icon='chess-queen',
                                pos_hint={'center_x': 0.8, 'center_y': 0.8})

        # Create float button
        btn_icon_float = MDFloatingActionButton(icon='chess-knight',
                                                pos_hint={'center_x': 0.3, 'center_y': 0.3})

        # Create list
        scroll = ScrollView()
        list_view = MDList()

        scroll.add_widget(list_view)
        icon = IconLeftWidget(icon='chart-pie')
        image = ImageLeftWidget(source='motioncatch-logo.png')
        item1 = OneLineListItem(text='One line')
        item2 = TwoLineListItem(text='Two lines', secondary_text='hello')
        item3 = ThreeLineListItem(text='Three lines', secondary_text='hello', tertiary_text='world')
        item4 = ThreeLineIconListItem(text='Three lines', secondary_text='hello', tertiary_text='world')
        item4.add_widget(icon)
        item5 = ThreeLineAvatarListItem(text='Three lines', secondary_text='hello', tertiary_text='world')
        item5.add_widget(image)

        list_view.add_widget(item1)
        list_view.add_widget(item2)
        list_view.add_widget(item3)
        list_view.add_widget(item4)
        list_view.add_widget(item5)

        # Create table
        table = MDDataTable(pos_hint={'center_x': 0.6, 'center_y': 0.6}, size_hint=(0.9, 0.6), rows_num=2, check=True,
                            column_data=[
                                ("No.", dp(18)),
                                ("Food", dp(20)),
                                ("Calories", dp(20))],
                            row_data=[
                                ("1", "Burger", "300"),
                                ("2", "Oats", "150")])
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)

        screen.add_widget(label)
        screen.add_widget(icon_label)
        screen.add_widget(btn_flat)
        screen.add_widget(btn_icon)
        screen.add_widget(btn_icon_float)

        #screen.add_widget(scroll)
        #screen.add_widget(table)

        return screen

    def navigation_draw(self):
        print("Navigation")

    def check_press(self, instace_table, current_row):
        print(instace_table, current_row)

    def row_press(self, instace_table, instance_row):
        print(instace_table, instance_row)

    def show_data(self, obj):
        if self.username.text is "":
            check_string = 'Indtast venligst dit brugernavn'
        else:
            check_string = self.username.text + ' eksisterer ikke'

        btn_close = MDFlatButton(text='Luk', on_release=self.close_dialog)
        btn_more = MDFlatButton(text='Mere')
        self.dialog = MDDialog(title='Tjek af brugernavn', text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[btn_close, btn_more])  # Sizehint: Require 70% of the screen in width
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


# Run the app
ErgolabApp().run()
