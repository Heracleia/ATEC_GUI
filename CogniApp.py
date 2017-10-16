#!python
#!/usr/bin/env python
from kivy.app import App
from kivy.uix.bubble import Bubble
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics.instructions import CanvasBase

Builder.load_string('''
#template for menu items
[ListButton@ToggleButton]
    background_normal: 'button_normal_cmenu.jpg'
    background_color: ctx.background_color if hasattr(ctx, 'background_color') else [1, .5, 0, 1]
    group: 'context_menue_root'
    on_release: ctx.on_release(self) if hasattr(ctx, 'on_release') else None
    size_hint: ctx.size_hint if hasattr(ctx, 'size_hint') else (1, 1)
    width: ctx.width if hasattr(ctx, 'width') else 1
    text: ctx.text if hasattr(ctx, 'text') else ''
    

<Button>:
    font_size: self.texture_size[1]/4 
    size_hint: 0.25,0.120
    color: (0, 0, 0, 1)
    #background_color: (0.81, 0.20, 0.81, 1)
    #width: self.texture_size[0]
    #height: self.texture_size[1]
    text_size: self.width,self.height
    halign: 'center'
    valign: 'middle'
    background_down: 'button_down.png'
    #background_down: 'atlas://data/images/defaulttheme/bubble_btn'

<MainScreen>
    id: "main"
    pos_hint: {"right":1,"top":1} 
    size_hint: 0.75, 1
    canvas:
        Rectangle:
            source: 'main_canvas.jpg'
            pos: self.pos
            size: self.size

   

<MainMenu>
    canvas:
        Rectangle:
            source: 'button_back.jpg'
            pos: self.pos
            size: self.size
    
    MainScreen:
        id: "sdfdsfsdf"
       
        Button:
            id: start
            text: "START"
            on_release:  root.add_menu(args[0],"start")
            pos_hint: {"right":0.3,"top":1} 
            background_normal: "start.jpg"

        Button:
            id: "pause"
            text: "PAUSE"
            on_release:  root.add_menu(args[0],"pause")
            pos_hint: {"right":0.6,"top":1}   
            background_normal: "pause.jpg"

        Button:
            id: "stop"
            text: "STOP"
            on_release:  root.add_menu(args[0],"stop")
            pos_hint: {"right":0.9,"top":1}  
            background_normal: "button_normal_cmenu.jpg"
        

    Button:
        id: "sdsd"
        text: "Gross Motor Gait and Balance"
        on_release:  root.add_menu(args[0],1)
        pos_hint: {"right":0.25,"top":1}  
        background_normal: 'button_normal.jpg'


    Button:
        on_release:  root.add_menu(args[0],2)
        text: "Synchronous Movements"
        pos_hint: {"right":0.25,"top":0.873}
        background_normal: 'button_normal.jpg'

    Button:
        on_release:  root.add_menu(args[0],3)
        text: "Bilateral Coordination & Response Inhibition"
        pos_hint: {"right":0.25,"top":0.745}
        background_normal: 'button_normal.jpg'

    Button:
        on_release:  root.add_menu(args[0],4)
        text: "Bilateral Coordination & Response Inhibition     (Red/Green Light)"
        pos_hint: {"right":0.25,"top":0.620}
        background_normal: 'button_normal.jpg'

    Button:
        on_release:  root.add_menu(args[0],5)
        text: "Visual Response Inhibition"
        pos_hint: {"right":0.25,"top":0.495}
        background_normal: 'button_normal.jpg'

    Button:
        on_release:  root.add_menu(args[0],6)
        text: "Cross Body Game"
        pos_hint: {"right":0.25,"top":0.370}
        background_normal: 'button_normal.jpg'

    Button:
        on_release:  root.add_menu(args[0],7)
        text: " Finger-Nose Coordination"
        pos_hint: {"right":0.25,"top":0.245}
        background_normal: 'button_normal.jpg'

    Button:
        on_release:  root.add_menu(args[0],8)
        text: "Rapid Sequential Movements"
        pos_hint: {"right":0.25,"top":0.120}
        background_normal: 'button_normal.jpg'



<Cmenu1>
    size_hint: 0.41, 0.6
    pos_hint: {"right":0.65,"top":1}
    padding: 0.005
    background_color: 1, 0, 0, 1
    
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Natural Walk'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Gait on Toes'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Tandem Gain'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Stand eyes closed hands outstretched'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Stand on One Foot'
                        on_release: root.menu_selected


<Cmenu2>
    size_hint: 0.41, 0.3
    pos_hint: {"right":0.65,"top":0.87}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'March Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'March Fast'
                        on_release: root.menu_selected
                       

<Cmenu3>
    size_hint: 0.41, 0.3
    pos_hint: {"right":0.65,"top":0.75}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Bi-manual Bag Pass Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Bi-manual Bag Pass Fast'
                        on_release: root.menu_selected

<Cmenu4>
    size_hint: 0.41, 0.6
    pos_hint: {"right":0.65,"top":0.62}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Red Light/Green Light -- Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light -- Fast'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Fast'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Visual Slow'
                        on_release: root.menu_selected

<Cmenu5>
    size_hint: 0.41, 0.16
    pos_hint: {"right":0.65,"top":0.50}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: ' A sailor went to Sea, Sea, Sea '
                        on_release: root.menu_selected

<Cmenu6>
    size_hint: 0.41, 0.35
    pos_hint: {"right":0.65,"top":0.37}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Cross Body Ears - Knees'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Cross Body Shoulders = Cross Body Hips'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Combined Reverse Actions'
                        on_release: root.menu_selected


<Cmenu7>
    size_hint: 0.41, 0.15
    pos_hint: {"right":0.65,"top":0.25}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Finger-Nose Coordination'
                        on_release: root.menu_selected

<Cmenu8>
    size_hint: 0.41, 0.7
    pos_hint: {"right":0.65,"top":0.68}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Foot Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Foot-Heel-Toe Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Hand Pat'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Hand Pronate/supinate'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Finger Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Appose Finger Succession'
                        on_release: root.menu_selected                 
''')


class Cmenu1(Bubble):
    def __init__(self, **kwargs):
        super(Cmenu1, self).__init__(**kwargs)
        self.show_arrow = False
    
    def menu_selected(self, *l):

        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            for child in self.parent.children:
                    #child.clear_widgets()
                    child.background_normal = "button_normal.jpg"

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'


class Cmenu2(Bubble):
    def __init__(self, **kwargs):
        super(Cmenu2, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class Cmenu3(Bubble):
    
    def __init__(self, **kwargs):
        super(Cmenu3, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            for child in self.parent.children:
                    #child.clear_widgets()
                    child.background_normal = "button_normal.jpg"

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class Cmenu4(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu4, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            for child in self.parent.children:
                    #child.clear_widgets()
                    child.background_normal = "button_normal.jpg"

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class Cmenu5(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu5, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class Cmenu6(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu6, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            for child in self.parent.children:
                    #child.clear_widgets()
                    child.background_normal = "button_normal.jpg"

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class Cmenu7(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu7, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class Cmenu8(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu8, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)
            
            for child in self.parent.children:
                    #child.clear_widgets()
                    child.background_normal = "button_normal.jpg"

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected :)'



class MainScreen(FloatLayout) :

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.context_menu = Cmenu1()


class MainMenu(FloatLayout) :

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.context_menu = Cmenu1()


    def on_touch_down(self, *l):
        #allow kids to get touch
        if super(MainMenu, self).on_touch_down(*l):
            return True
        self.remove_widget(self.context_menu)
        for child in self.children:
                #child.clear_widgets()
                child.background_normal = "button_normal.jpg"


    def add_menu(self, obj, submenu_id,*l):
        for child in self.children:
                #child.clear_widgets()
                child.background_normal = "button_normal.jpg"

        if  hasattr(self, 'context_menu'):
                self.remove_widget(self.context_menu)
        if submenu_id == 1:
            self.context_menu = Cmenu1()
        elif submenu_id == 2:
            self.context_menu = Cmenu2()
        elif submenu_id == 3:
            self.context_menu = Cmenu3()
        elif submenu_id == 4:
            self.context_menu = Cmenu4()
        elif submenu_id == 5:
            self.context_menu = Cmenu5()
        elif submenu_id == 6:
            self.context_menu = Cmenu6()
        elif submenu_id == 7:
            self.context_menu = Cmenu7()
        elif submenu_id == 8:
            self.context_menu = Cmenu8()

        if submenu_id not in ["start","stop","pause"]:
            obj.background_normal = "button_normal_is_on.jpg"
            self.add_widget(self.context_menu)
            self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]
       


class MyApp(App):
    def build(self):
        return MainMenu()


if __name__ == '__main__':
    MyApp().run()