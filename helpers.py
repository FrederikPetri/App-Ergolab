username_helper = """
MDTextField: 
    hint_text: "Indtast brugernavn"
    helper_text: "eller klik på glemt brugernavn"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.6, 'center_y': 0.6}
    size_hint_x: None 
    width: 300
"""

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            title: 'Ergolab'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["settings", lambda x: app.navigation_draw()]]
            elevation: 8 
        MDLabel:
            text: 'Hello World'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar: 
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                icon: 'language-python'
                on_action_button: app.navigation_draw()
"""

navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar: 
                        title: 'Ergolab'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 8
                        
                    Widget:
                
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'Frederik.png'
                MDLabel:
                    text: '     Optagelse'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: '     Rapport'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Optagelse'
                            IconLeftWidget:
                                icon: 'android'
                        OneLineIconListItem:
                            text: 'Rapport'
                            IconLeftWidget:
                                icon: 'android'
"""

another_helper = """
ScreenManager:
    MenuScreen:
    RecordingScreen:
    
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Optagelse'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'optagelse'
        
        
<RecordingScreen>:
    name: 'optagelse'
    MDLabel:
        text: 'Optagelse'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Tilbage'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'menu'
              
"""



# elevation: shadow ;