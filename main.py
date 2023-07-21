from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#ffe8ad"
    text_color: "#756029"   
    icon_color: "#756029"
    ripple_color: "#c5bdd2"
    selected_color: "#f0d281"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True 


<ContentNavigationDrawer>
           
    MDNavigationDrawerMenu: 
        MDNavigationDrawerHeader:
            title: "Програма автоматизации"
            title_color: "#d1b771"
            title_font_style: "H5"
            source: "https://kivymd.readthedocs.io/en/1.1.1/_static/logo-kivymd.png"
            spacing: 10
            padding: 20, 15
            
        MDNavigationDrawerLabel:
            text: "Меню"
            
        DrawerClickableItem:
            icon: "wifi"
            text: "Wifi auto-off"
            on_press:
                root.screen_manager.current = "wifi settings"
            
        DrawerClickableItem:
            icon: "bluetooth"
            text: "Bluetooth auto-off"
            on_press:
                root.screen_manager.current = "bluetooth settings"
            
        DrawerClickableItem:
            icon: "nfc"
            text: "NFC auto-off"
            on_press:
                root.screen_manager.current = "nfc settings"
            
        MDNavigationDrawerDivider:
            
        DrawerLabelItem:
            icon: "information-outline"
            text: "Ця створенна для автоматизації повсякденних задач."

MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        md_bg_color: "#f2c855"
        title: "Програма автоматизации"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "wifi settings"
                
                AnchorLayout:
                
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: 50
                        adaptive_height: True
                        
                        
                        MDLabel:
                            text: "Wifi Settings"
                            text_color: "#edd18a"
                            halign: "center"
                            font_size: 30
                            text_color: "#f7cf68"
                        
                        MDLabel:
                            text: "Время до отключения wifi"
                            halign: "center"
                            font_size: 20
                            text_color: "#f7cf68"
                                                        
                        MDDropDownItem:
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            text: '30 second'
                            current_item: "30 second"
                            on_release: print("Press item")
                            
                MDRaisedButton:                        
                    text: "Применить"
                    md_gb_color: "#f7c443"
                    anchor: "right"
                    pos_hint: {"x": 0.8, "y": 0.05}

            MDScreen:
                name: "bluetooth settings"

                AnchorLayout:
                
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: 50
                        adaptive_height: True
                        
                        
                        MDLabel:
                            text: "Bluetooth Settings"
                            text_color: "#edd18a"
                            halign: "center"
                            font_size: 30
                            text_color: "#f7cf68"
                        
                        MDLabel:
                            text: "Время до отключения bluetooth"
                            halign: "center"
                            font_size: 20
                            text_color: "#f7cf68"
                                                        
                        MDDropDownItem:
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            text: '30 second'
                            current_item: "30 second"
                            on_release: print("Press item")
                            
                MDRaisedButton:                        
                    text: "Применить"
                    md_gb_color: "#f7c443"
                    anchor: "right"
                    pos_hint: {"x": 0.8, "y": 0.05}
                    
            MDScreen:
                name: "nfc settings"
                
                AnchorLayout:
                
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: 50
                        adaptive_height: True
                        
                        
                        MDLabel:
                            text: "NFC Settings"
                            text_color: "#edd18a"
                            halign: "center"
                            font_size: 30
                            text_color: "#f7cf68"
                        
                        MDLabel:
                            text: "Время до отключения nfc"
                            halign: "center"
                            font_size: 20
                            text_color: "#f7cf68"
                                                        
                        MDDropDownItem:
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            text: '30 second'
                            current_item: "30 second"
                            on_release: print("Press item")
                            
                MDRaisedButton:                        
                    text: "Применить"
                    md_gb_color: "#f7c443"
                    anchor: "right"
                    pos_hint: {"x": 0.8, "y": 0.05}

        MDNavigationDrawer:
            id: nav_drawer
            scrim_color: 0, 0, 0, .2
            radius: (0, 16, 16, 0)
            
            ContentNavigationDrawer:
                screen_manager: screen_manager
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    #nav_drawer = ObjectProperty()


class Automate(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return self.screen


Automate().run()
