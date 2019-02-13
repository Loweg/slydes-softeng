#the place for window stuff

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

import slide

class Window(Gtk.Window):

    def __init__(self):
        '''
            call super class constructor.
            once the backend is a little more developed, the title of the slide will have
            to be changed and such.
        '''

        #---------------#
        # window set up #
        #---------------#

        Gtk.Window.__init__(self, title='Slydes -- Unititled 1')

        # position window to center of screen when launched
        self.set_position(Gtk.WindowPosition.CENTER)

        # resize window
        screen = Gdk.Screen.get_default()
        self.set_size_request(1000, 800)

        #----------------#
        # toolbar set up #
        #----------------#

        # a map from names to Gtk.Action objects for the toolbar.
        toolbar_group = Gtk.ActionGroup("toolbar_actions")

        toolbar = self.create_toolbar(toolbar_group)

        #------------------#
        # shortcuts set up #
        #------------------#

        self.accel_group = Gtk.AccelGroup()
        self.add_accel_group(self.accel_group)


        # the box that will hold all of the things in our window
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(toolbar, False, False, 0)
        self.add(box)

        #-----------------------------#
        # slides and slide bar set up #
        #-----------------------------#

        self.slide_deck = slide.SlideDeck(self)
        self.current_slide = self.slide_deck.get_current_slide()
        box.add(self.slide_deck.get_view())


        # connect and show window
        self.connect('destroy', Gtk.main_quit)
        self.show_all()


    def set_current_slide(self, new_slide):

        '''
            takes in THIS window and a slide object
            sets the passed slide as the current slide to display
        '''
        self.current_slide = new_slide

    def create_ui_manager(self):
        '''
            Takes in THIS window
            Returns a UI manager
        '''
        ui_manager = Gtk.UIManager()

        # add the accelerator group to the toplevel window
        # accelerators: shortcuts for activating a menu item
        # will look into later for use
        # accel_group = ui_manager.get_accel_group()
        # self.add_accel_group(accel_group)
        return ui_manager

    def add_accelerator(self, widget, accel, signal="activate"):
        if accel is not None:
            key, mod = Gtk.accelerator_parse(accel)
            widget.add_accelerator(signal, Gtk.AccelGroup(), key, mod, Gtk.AccelFlags.VISIBLE)


    def create_toolbar(self, action_group):
        '''
            takes in THIS window and an action group
            creates all of the buttons for the toolbar that will be displayed at the top of the window.
        '''

        toolbar = Gtk.Toolbar()

        #--------------------#
        # 'Load File' Button #
        #--------------------#
        button_loadfile = Gtk.ToolButton()
        # set button icon
        img_loadfile = Gtk.Image().new_from_file("images/icons/load-file.png")
        button_loadfile.set_icon_widget(img_loadfile)
        # set tooltip text
        button_loadfile.set_tooltip_text('Load saved slydes presentation')
        # event listener
        button_loadfile.connect('clicked', self.on_menu)

        toolbar.insert(button_loadfile, 0)

        #--------------------#
        # 'Save File' Button #
        #--------------------#
        button_savefile = Gtk.ToolButton()
        # set button icon
        img_savefile = Gtk.Image().new_from_file("images/icons/save.png")
        button_savefile.set_icon_widget(img_savefile)
        # set tooltip text
        button_savefile.set_tooltip_text('Save File')
        # event listener
        button_savefile.connect('clicked', self.on_menu)

        toolbar.insert(button_savefile, 1)

        #--------------------#
        # 'Add Slide' Button #
        #--------------------#
        button_addslide = Gtk.ToolButton()
        # set button icon
        img_addslide = Gtk.Image().new_from_file("images/icons/add-slide.png")
        button_addslide.set_icon_widget(img_addslide)
        # set tooltip text
        button_addslide.set_tooltip_text('Add new slide')
        # event listener
        button_addslide.connect('clicked', self.add_slide)

        toolbar.insert(button_addslide, 2)

        #----------------#
        # 'Print' Button #
        #----------------#
        # button_print = Gtk.ToolButton()
        # # set button icon
        # img_print = Gtk.Image().new_from_file("images/icons/print.png")
        # button_print.set_icon_widget(img_print)
        # # set tooltip text
        # button_print.set_tooltip_text('Print slydes')
        # # event listener
        # button_print.connect('clicked', self.on_menu)

        # toolbar.insert(button_print, 2)

        #---------------#
        # 'Play' Button #
        #---------------#
        button_play = Gtk.ToolButton()
        # set button icon
        img_play = Gtk.Image().new_from_file("images/icons/play.png")
        button_play.set_icon_widget(img_play)
        # set tooltip text
        button_play.set_tooltip_text('Play slydes presentation')
        # event listener
        button_play.connect('clicked', self.on_menu)

        toolbar.insert(button_play, 3)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 4)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 5)

        #-------------------#
        # 'Text Box' Button #
        #-------------------#
        button_textbox = Gtk.ToolButton()
        # set button icon
        img_textbox = Gtk.Image().new_from_file("images/icons/text-box.png")
        button_textbox.set_icon_widget(img_textbox)
        # set tooltip text
        button_textbox.set_tooltip_text('Text box')
        # event listener
        button_textbox.connect('clicked', self.on_menu)

        toolbar.insert(button_textbox, 6)

        #-------------------------#
        # 'Insert Picture' Button #
        #-------------------------#
        button_insertpic = Gtk.ToolButton()
        # set button icon
        img_insertpic = Gtk.Image().new_from_file("images/icons/insert-pic.png")
        button_insertpic.set_icon_widget(img_insertpic)
        # set tooltip text
        button_insertpic.set_tooltip_text('Insert picture')
        # event listener
        button_insertpic.connect('clicked', self.image_clicked)

        toolbar.insert(button_insertpic, 7)

        #---------------#
        # 'Draw' Button #
        #---------------#
        # button_draw = Gtk.ToolButton()
        # # set button icon
        # img_draw = Gtk.Image().new_from_file("images/icons/draw.png")
        # button_draw.set_icon_widget(img_draw)
        # # set tooltip text
        # button_draw.set_tooltip_text('Draw')
        # # event listener
        # button_draw.connect('clicked', self.on_menu)

        # toolbar.insert(button_draw, 8)

        #---------------------#
        # 'Code Block' Button #
        #---------------------#
        # button_code = Gtk.ToolButton()
        # # set button icon
        # img_code = Gtk.Image().new_from_file("images/icons/code-block.png")
        # button_code.set_icon_widget(img_code)
        # # set tooltip text
        # button_code.set_tooltip_text('Insert code block')
        # # event listener
        # button_code.connect('clicked', self.on_menu)

        # toolbar.insert(button_code, 9)

        #----------------#
        # 'Latex' Button #
        #----------------#
        # button_latex = Gtk.ToolButton()
        # # set button icon
        # img_latex = Gtk.Image().new_from_file("images/icons/latex.png")
        # button_latex.set_icon_widget(img_latex)
        # # set tooltip text
        # button_latex.set_tooltip_text('Insert Latex')
        # # event listener
        # button_latex.connect('clicked', self.on_menu)

        # toolbar.insert(button_latex, 10)

        #--------------------#
        # 'Hyperlink' Button #
        #--------------------#
        button_hyperlink = Gtk.ToolButton()
        # set button icon
        img_hyperlink = Gtk.Image().new_from_file("images/icons/hyperlink.png")
        button_hyperlink.set_icon_widget(img_hyperlink)
        # set tooltip text
        button_hyperlink.set_tooltip_text('Insert hyperlink')
        # event listener
        button_hyperlink.connect('clicked', self.insert_link)

        toolbar.insert(button_hyperlink, 8)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 9)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 10)

        #--------------------#
        # 'Undo' Button      #
        #--------------------#
        # button_undo = Gtk.ToolButton()
        # # set button icon
        # img_undo = Gtk.Image().new_from_file("images/icons/undo.png")
        # button_undo.set_icon_widget(img_undo)
        # # set tooltip text
        # button_undo.set_tooltip_text('Undo')
        # # event listener
        # button_undo.connect('clicked', self.on_menu)

        # toolbar.insert(button_undo, 14)

        #-----------------------#
        # 'View Changes' Button #
        #-----------------------#
        button_viewchange = Gtk.ToolButton()
        # set button icon
        img_viewchange = Gtk.Image().new_from_file("images/icons/view-change.png")
        button_viewchange.set_icon_widget(img_viewchange)
        # set tooltip text
        button_viewchange.set_tooltip_text('View changes made')
        # event listener
        button_viewchange.connect('clicked', self.on_menu)

        toolbar.insert(button_viewchange, 11)

        #---------------#
        # 'Redo' Button #
        #---------------#
        # button_redo = Gtk.ToolButton()
        # # set button icon
        # img_redo = Gtk.Image().new_from_file("images/icons/redo.png")
        # button_redo.set_icon_widget(img_redo)
        # # set tooltip text
        # button_redo.set_tooltip_text('Redo')
        # # event listener
        # button_redo.connect('clicked', self.on_menu)

        # toolbar.insert(button_redo, 16)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 12)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 13)

        #----------------------#
        # 'Change Font' Button #
        #----------------------#
        button_changefont = Gtk.ToolButton()
        # set button icon
        img_changefont = Gtk.Image().new_from_file("images/icons/font.png")
        button_changefont.set_icon_widget(img_changefont)
        # set tooltip text
        button_changefont.set_tooltip_text('Change font')
        # event listener
        button_changefont.connect('clicked', self.on_menu)

        toolbar.insert(button_changefont, 14)

        #-----------------------------#
        # 'Increase Font Size' Button #
        #-----------------------------#
        button_increase_fontsize = Gtk.ToolButton()
        # set button icon
        img_increase_fontsize = Gtk.Image().new_from_file("images/icons/increase-font-size.png")
        button_increase_fontsize.set_icon_widget(img_increase_fontsize)
        # set tooltip text
        button_increase_fontsize.set_tooltip_text('Increase font size')
        # event listener
        button_increase_fontsize.connect('clicked', self.increase_font)

        toolbar.insert(button_increase_fontsize, 15)

        #-----------------------------#
        # 'Decrease Font Size' Button #
        #-----------------------------#
        button_decrease_fontsize = Gtk.ToolButton()
        # set button icon
        img_decrease_fontsize = Gtk.Image().new_from_file("images/icons/decrease-font-size.png")
        button_decrease_fontsize.set_icon_widget(img_decrease_fontsize)
        # set tooltip text
        button_decrease_fontsize.set_tooltip_text('Decrease font size')
        # event listener
        button_decrease_fontsize.connect('clicked', self.decrease_font)

        toolbar.insert(button_decrease_fontsize, 16)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 17)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 18)

        #---------------#
        # 'Bold' Button #
        #---------------#
        button_bold = Gtk.ToolButton()
        # set button icon
        img_bold = Gtk.Image().new_from_file("images/icons/bold.png")
        button_bold.set_icon_widget(img_bold)
        # set tooltip text
        button_bold.set_tooltip_text('Bold')
        # event listener
        button_bold.connect('clicked', self.bold_clicked)

        toolbar.insert(button_bold, 19)

        #-----------------#
        # 'Italic' Button #
        #-----------------#
        button_italic = Gtk.ToolButton()
        # set button icon
        img_italic = Gtk.Image().new_from_file("images/icons/italic.png")
        button_italic.set_icon_widget(img_italic)
        # set tooltip text
        button_italic.set_tooltip_text('Italic')
        # event listener
        button_italic.connect('clicked', self.italic_clicked)

        toolbar.insert(button_italic, 20)

        #--------------------#
        # 'Underline' Button #
        #--------------------#
        button_underline = Gtk.ToolButton()
        # set button icon
        img_underline = Gtk.Image().new_from_file("images/icons/underline.png")
        button_underline.set_icon_widget(img_underline)
        # set tooltip text
        button_underline.set_tooltip_text('Underline')
        # event listener
        button_underline.connect('clicked', self.underline_clicked)

        toolbar.insert(button_underline, 21)

        #------------------------------#
        # 'Reset Type Emphasis' Button #
        #------------------------------#
        button_reset = Gtk.ToolButton()
        # set button icon
        img_reset = Gtk.Image().new_from_file("images/icons/reset.png")
        button_reset.set_icon_widget(img_reset)
        # set tooltip text
        button_reset.set_tooltip_text('Reset all text emphasis')
        # event listener
        button_reset.connect('clicked', self.clear_clicked)

        toolbar.insert(button_reset, 22)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 23)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 24)

        #---------------------#
        # 'Align Left' Button #
        #---------------------#
        radio_alignleft = Gtk.RadioToolButton()
        # set button icon
        img_alignleft = Gtk.Image().new_from_file("images/icons/align-left.png")
        radio_alignleft.set_icon_widget(img_alignleft)
        # set tooltip text
        radio_alignleft.set_tooltip_text('Align left')
        # event listener
        radio_alignleft.connect('toggled', self.left_align)

        toolbar.insert(radio_alignleft, 25)

        #-----------------------#
        # 'Align Center' Button #
        #-----------------------#
        radio_aligncenter = Gtk.RadioToolButton().new_from_widget(radio_alignleft)
        # set button icon
        img_aligncenter = Gtk.Image().new_from_file("images/icons/align-center.png")
        radio_aligncenter.set_icon_widget(img_aligncenter)
        # set tooltip text
        radio_aligncenter.set_tooltip_text('Align Center')
        # event listener
        radio_aligncenter.connect('toggled', self.center_align)

        toolbar.insert(radio_aligncenter, 26)

        #----------------------#
        # 'Align Right' Button #
        #----------------------#
        radio_alignright = Gtk.RadioToolButton().new_from_widget(radio_alignleft)
        # set button icon
        img_alignright = Gtk.Image().new_from_file("images/icons/align-right.png")
        radio_alignright.set_icon_widget(img_alignright)
        # set tooltip text
        radio_alignright.set_tooltip_text('Align right')
        # event listener
        radio_alignright.connect('toggled', self.right_align)

        toolbar.insert(radio_alignright, 27)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 28)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 29)

        #------------------------#
        # 'Bulleted List' Button #
        #------------------------#
        # button_bulletlist = Gtk.ToolButton()
        # # set button icon
        # img_bulletlist = Gtk.Image().new_from_file("images/icons/bullet-list.png")
        # button_bulletlist.set_icon_widget(img_bulletlist)
        # # set tooltip text
        # button_bulletlist.set_tooltip_text('Bulleted list')
        # # event listener
        # button_bulletlist.connect('clicked', self.on_menu)

        # toolbar.insert(button_bulletlist, 31)

        #------------------------#
        # 'Numbered List' Button #
        #------------------------#
        # button_numlist = Gtk.ToolButton()
        # # set button icon
        # img_numlist = Gtk.Image().new_from_file("images/icons/number-list.png")
        # button_numlist.set_icon_widget(img_numlist)
        # # set tooltip text
        # button_numlist.set_tooltip_text('Numbered list')
        # # event listener
        # button_numlist.connect('clicked', self.on_menu)

        # toolbar.insert(button_numlist, 32)

        #-----------------------#
        # 'Page Numbers' Button #
        #-----------------------#
        button_pagenum = Gtk.ToolButton()
        # set button icon
        img_pagenum = Gtk.Image().new_from_file("images/icons/page-num.png")
        button_pagenum.set_icon_widget(img_pagenum)
        # set tooltip text
        button_pagenum.set_tooltip_text('Insert page numbers')
        # event listener
        button_pagenum.connect('clicked', self.on_menu)

        toolbar.insert(button_pagenum, 30)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 31)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 32)

        #-----------------#
        # 'Themes' Button #
        #-----------------#
        button_themes = Gtk.ToolButton()
        # set button icon
        img_themes = Gtk.Image().new_from_file("images/icons/change-theme.png")
        button_themes.set_icon_widget(img_themes)
        # set tooltip text
        button_themes.set_tooltip_text('Change slydes theme')
        # event listener
        button_themes.connect('clicked', self.on_menu)

        toolbar.insert(button_themes, 33)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 34)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 35)

        #---------------#
        # 'Help' Button #
        #---------------#
        button_help = Gtk.ToolButton()
        # set button icon
        img_help = Gtk.Image().new_from_file("images/icons/help.png")
        button_help.set_icon_widget(img_help)
        # set tooltip text
        button_help.set_tooltip_text('Help')
        # event listener
        button_help.connect('clicked', self.on_menu)

        toolbar.insert(button_help, 36)

        return toolbar



    def main(self):
        '''
            starts main loop for GTK.
        '''
        Gtk.main()

    def on_menu(self, button):
        '''
            stub method while we wait to implement more button functions.
        '''
        print("Toolbar button clicked.")

    #--------------------------------#
    # 'Insert Picture' Button METHOD #
    #--------------------------------#
    def image_clicked(self, button):
        self.current_slide.insert_image_clicked(button)

    #----------------------#
    # 'Bold' Button METHOD #
    #----------------------#
    def bold_clicked(self, button):
        self.current_slide.tag_button_clicked(button, "bold")

    #------------------------#
    # 'Italic' Button METHOD #
    #------------------------#
    def italic_clicked(self, button):
        self.current_slide.tag_button_clicked(button, "italic")

    #---------------------------#
    # 'Underline' Button METHOD #
    #---------------------------#
    def underline_clicked(self, button):
        self.current_slide.tag_button_clicked(button, "underline")

    #-------------------------------------#
    # 'Reset Type Emphasis' Button METHOD #
    #-------------------------------------#
    def clear_clicked(self, button):
        self.current_slide.clear_tags(button)

    #-----------------------------#
    # 'Align Right' Button METHOD #
    #-----------------------------#
    def right_align(self, button):
        self.current_slide.align(Gtk.Justification.RIGHT)

    #----------------------------#
    # 'Align Left' Button METHOD #
    #----------------------------#
    def left_align(self, button):
        self.current_slide.align(Gtk.Justification.LEFT)

    #------------------------------#
    # 'Align Center' Button METHOD #
    #------------------------------#
    def center_align(self, button):
        self.current_slide.align(Gtk.Justification.CENTER)

    #---------------------------#
    # 'Add Slide' Button METHOD #
    #---------------------------#
    def add_slide(self, button):
        self.slide_deck.make_new_slide()
        self.show_all()

    #---------------------------#
    # 'Hyperlink' Button METHOD #
    #---------------------------#
    def insert_link(self, button):
        self.current_slide.insert_link(self)

    #------------------------------------#
    # 'Increase Font Size' Button METHOD #
    #------------------------------------#
    def increase_font(self, button):
        self.current_slide.increment_font()

    #------------------------------------#
    # 'Decrease Font Size' Button METHOD #
    #------------------------------------#
    def decrease_font(self, button):
        self.current_slide.decrement_font()

window = Window()
window.main()


