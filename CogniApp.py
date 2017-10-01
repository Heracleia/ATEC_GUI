#!python
#!/usr/bin/env python
from kivy.app import App
from kivy.uix.bubble import Bubble
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string('''
#template for menu items
[ListButton@ToggleButton]
    background_down: 'atlas://data/images/defaulttheme/bubble_btn'
    background_normal: 'atlas://data/images/defaulttheme/bubble_btn_pressed'
    group: 'context_menue_root'
    on_release: ctx.on_release(self) if hasattr(ctx, 'on_release') else None
    size_hint: ctx.size_hint if hasattr(ctx, 'size_hint') else (1, 1)
    width: ctx.width if hasattr(ctx, 'width') else 1
    text: ctx.text if hasattr(ctx, 'text') else ''
    Image:
        source: ctx.btn_img if ctx.text == 'hows' \
            else 'atlas://data/images/defaulttheme/bubble_btn'
        size: (20, 20)
        y: self.parent.y + (self.parent.height/2) - (self.height/2)
        x: self.parent.x + (self.parent.width - self.width)


<Button>:
    font_size: self.texture_size[1]/4 
    size_hint: 0.25,0.120
    color: (1, 1, 1, 1)
    background_color: (0.81, 0.20, 0.81, 1)
    #width: self.texture_size[0]
    #height: self.texture_size[1]
    text_size: self.width,self.height
    halign: 'center'
    valign: 'middle'

<MainMenu>
    Button:
        text: "Gross Motor Gait and Balance"
        on_release:  root.add_menu(args[0],1)
        pos_hint: {"right":0.25,"top":0.995}  

    Button:
        on_release:  root.add_menu(args[0],2)
        text: "Synchronous Movements"
        pos_hint: {"right":0.25,"top":0.870}

    Button:
        on_release:  root.add_menu(args[0],3)
        text: "Bilateral Coordination & Response Inhibition"
        pos_hint: {"right":0.25,"top":0.745}

    Button:
        on_release:  root.add_menu(args[0],4)
        text: "Bilateral Coordination & Response Inhibition     (Red/Green Light)"
        pos_hint: {"right":0.25,"top":0.620}

    Button:
        on_release:  root.add_menu(args[0],5)
        text: "Visual Response Inhibition"
        pos_hint: {"right":0.25,"top":0.495}

    Button:
        on_release:  root.add_menu(args[0],6)
        text: "Cross Body Game"
        pos_hint: {"right":0.25,"top":0.370}
    Button:
        on_release:  root.add_menu(args[0],7)
        text: " Finger-Nose Coordination"
        pos_hint: {"right":0.25,"top":0.245}
    Button:
        on_release:  root.add_menu(args[0],8)
        text: "Rapid Sequential Movements"
        pos_hint: {"right":0.25,"top":0.120}


<MainPage>
    MainMenu
    
<SetA>
    Button:
        text: 'press to launch menu'
        size_hint: .2, .2
        on_release:  root.add_menu(args[0])
        pos_hint: {"right":0.25,"top":0.620}
  
    Button:
        text: 'press to launch menu'
        size_hint: .2, .2
        on_release:  root.add_menu(args[0])
        pos_hint: {"right":0.4,"top":0.2}

<SetB>
    Button:
        text: 'BBBBBBB'
        size_hint: .2, .2
        on_release:  root.add_menu(args[0])
        pos_hint: {"right":0.6,"top":0.620}
  
   


<Cmenu1>
    size_hint: None, None
    size: 120, 250
    pos: (5, 50)
    padding: 5
    background_color: .2, .9, 1, .7
    #wanna have some fun? set this to 'data/images/image-loading.gif'
    background_image: 'atlas://data/images/defaulttheme/button_pressed'
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: None, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Hello'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'World'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'hows'
                        #'>'image
                        btn_img: 'atlas://data/images/defaulttheme/tree_closed'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'it'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'going'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'peace'
                        on_release: root.menu_selected
                # end root menu
                #sub-menu
                BoxLayout:
                    ListButton:
                        # go back(root menu) button
                        text: '<'
                        size_hint: (.15, 1)
                        on_release: root.menu_selected
                    BoxLayout:
                        orientation: 'vertical'
                        ListButton:
                            text: 'The'
                            on_release: root.menu_selected
                        ListButton:
                            text: 'revolving'
                            on_release: root.menu_selected
                        ListButton:
                            text: 'door'
                            on_release: root.menu_selected
                        ListButton:
                            text: 'hits'
                            on_release: root.menu_selected
                        ListButton:
                            text: 'every'
                            on_release: root.menu_selected
                        ListButton:
                            text: 'one'
                            on_release: root.menu_selected
                #end sub-menu




<Cmenu2>
    size_hint: None, None
    size: 120, 250
    pos: (5, 50)
    padding: 5
    background_color: .2, .9, 1, .7
    #wanna have some fun? set this to 'data/images/image-loading.gif'
    background_image: 'atlas://data/images/defaulttheme/button_pressed'
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: None, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Hello'
                        on_release: root.menu_selected
                 
''')


class Cmenu1(Bubble):

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

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'


class Cmenu2(Bubble):

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

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class SetA(FloatLayout):

    def __init__(self, **kwargs):
        super(SetA, self).__init__(**kwargs)

    def on_touch_down(self, *l):
        #allow kids to get touch
        if super(SetA, self).on_touch_down(*l):
            return True
        # remove menu when touched and menu exists
        if hasattr(self, 'context_menu'):
            self.remove_widget(self.context_menu)

    def add_menu(self, obj, *l):
        if not hasattr(self, 'context_menu'):
            self.context_menu = Cmenu1()
        self.remove_widget(self.context_menu)
        self.add_widget(self.context_menu)
        self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]



class SetB(FloatLayout):

    def __init__(self, **kwargs):
        super(SetB, self).__init__(**kwargs)

    def on_touch_down(self, *l):
        #allow kids to get touch
        if super(SetB, self).on_touch_down(*l):
            return True
        # remove menu when touched and menu exists
        if hasattr(self, 'context_menu'):
            self.remove_widget(self.context_menu)

    def add_menu(self, obj, *l):
        if not hasattr(self, 'context_menu'):
            self.context_menu = Cmenu1()
        self.remove_widget(self.context_menu)
        self.add_widget(self.context_menu)
        self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]




class MainMenu(FloatLayout) :
    def add_menu(self, obj, submenu_id,*l):
        if  hasattr(self, 'context_menu'):
                self.remove_widget(self.context_menu)
        if submenu_id == 5:
            
            self.context_menu = Cmenu1()
            self.remove_widget(self.context_menu)
            self.add_widget(self.context_menu)
            self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]
        elif submenu_id == 6:
            if not hasattr(self, 'context_menu'):
                print "sfdsdfsdfs"
            self.context_menu = Cmenu2()
            self.remove_widget(self.context_menu)
            self.add_widget(self.context_menu)
            self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]

    def menu_selected(self, *l):
        if l[0].text == 'Cross Body Game':
            # move to sub menu
            def add_menu(self, obj, *l):
                if not hasattr(self, 'context_menu'):
                    self.context_menu = SetA()
                self.remove_widget(self.context_menu)
                self.add_widget(self.context_menu)
                self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]

            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == 'Synchronous Movements':
            # move to sub menu
            def add_menu(self, obj, *l):
                if not hasattr(self, 'context_menu'):
                    self.context_menu = SetB()
                self.remove_widget(self.context_menu)
                self.add_widget(self.context_menu)
                self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]

            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            self.parent.remove_widget(self.context_menu)
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class MainPage(FloatLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)

    def on_touch_down(self, *l):
        #allow kids to get touch
        if super(MainPage, self).on_touch_down(*l):
            return True
        # remove menu when touched and menu exists
        if hasattr(self, 'context_menu'):
            self.remove_widget(self.context_menu)

    def add_menu(self, obj, *l):
        if not hasattr(self, 'context_menu'):
            self.context_menu = MainMenu()
        self.remove_widget(self.context_menu)
        self.add_widget(self.context_menu)
        self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]



class MyApp(App):
    def build(self):
        return MainPage()


if __name__ == '__main__':
    MyApp().run()