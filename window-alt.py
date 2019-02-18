#the place for window stuff
import os
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

        Gtk.Window.__init__(self, title='Slydes -- Untitled 1')

        # position window to center of screen when launched
        self.set_position(Gtk.WindowPosition.CENTER)

        # resize window
        #screen = Gdk.Screen.get_default()
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

        self.connect('key-press-event', self.on_key)


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

    def create_toolbar(self, action_group):
        '''
            takes in THIS window and an action group
            creates all of the buttons for the toolbar that will be displayed at the top of the window.
        '''

        toolbar = Gtk.Toolbar()

        #--------------------#
        # 'Load File' Button #
        #--------------------#
        self.button_loadfile = Gtk.ToolButton()
        # set button icon
        # img_loadfile = Gtk.Image().new_from_file("images/icons/load-file.png")
        self.button_loadfile.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_OPEN))
        # set tooltip text
        self.button_loadfile.set_tooltip_text('Ctrl+O: Load saved slydes presentation')
        # event listener
        self.button_loadfile.connect('clicked', self.on_menu)

        toolbar.insert(self.button_loadfile, 0)

        #--------------------#
        # 'Save File' Button #
        #--------------------#
        self.button_savefile = Gtk.ToolButton()
        # set button icon
        # img_savefile = Gtk.Image().new_from_file("images/icons/save.png")
        self.button_savefile.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_SAVE))
        # set tooltip text
        self.button_savefile.set_tooltip_text('F12: Save File')
        # event listener
        self.button_savefile.connect('clicked', self.on_menu)

        toolbar.insert(self.button_savefile, 1)

        #--------------------#
        # 'Add Slide' Button #
        #--------------------#
        self.button_addslide = Gtk.ToolButton()
        # set button icon
        # img_addslide = Gtk.Image().new_from_file("images/icons/add-slide.png")
        self.button_addslide.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_ADD))
        # set tooltip text
        self.button_addslide.set_tooltip_text('Ctrl+M: Add new slide')
        # event listener
        self.button_addslide.connect('clicked', self.add_slide)

        toolbar.insert(self.button_addslide, 2)

        #----------------#
        # 'Print' Button #
        #----------------#
        # button_print = Gtk.ToolButton()
        # # set button icon
        # # img_print = Gtk.Image().new_from_file("images/icons/print.png")
        # button_print.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_PRINT))
        # # set tooltip text
        # button_print.set_tooltip_text('Print slydes')
        # # event listener
        # button_print.connect('clicked', self.on_menu)

        # toolbar.insert(button_print, 2)

        #---------------#
        # 'Play' Button #
        #---------------#
        # button_play = Gtk.ToolButton()
        # # set button icon
        # # img_play = Gtk.Image().new_from_file("images/icons/play.png")
        # button_play.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_MEDIA_PLAY))
        # # set tooltip text
        # button_play.set_tooltip_text('Play slydes presentation')
        # # event listener
        # button_play.connect('clicked', self.on_menu)

        # toolbar.insert(button_play, 3)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 3)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 4)

        # #-------------------#
        # # 'Text Box' Button #
        # #-------------------#
        # button_textbox = Gtk.ToolButton()
        # # set button icon
        # img_textbox = Gtk.Image().new_from_file("images/icons/text-box.png")
        # button_textbox.set_icon_widget(img_textbox)
        # # set tooltip text
        # button_textbox.set_tooltip_text('Text box')
        # # event listener
        # button_textbox.connect('clicked', self.on_menu)

        # toolbar.insert(button_textbox, 6)

        #-------------------------#
        # 'Insert Picture' Button #
        #-------------------------#
        self.button_insertpic = Gtk.ToolButton()
        # set button icon
        # img_insertpic = Gtk.Image().new_from_file("images/icons/insert-pic.png")
        self.button_insertpic.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_ORIENTATION_LANDSCAPE))
        # set tooltip text
        self.button_insertpic.set_tooltip_text('Ctrl+P: Insert picture')
        # event listener
        self.button_insertpic.connect('clicked', self.image_clicked)

        toolbar.insert(self.button_insertpic, 5)

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
        self.button_hyperlink = Gtk.ToolButton()
        # set button icon
        # img_hyperlink = Gtk.Image().new_from_file("images/icons/hyperlink.png")
        self.button_hyperlink.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_CONNECT))
        # set tooltip text
        self.button_hyperlink.set_tooltip_text('Ctrl+K: Insert hyperlink')
        # event listener
        self.button_hyperlink.connect('clicked', self.insert_link)

        toolbar.insert(self.button_hyperlink, 6)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 7)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 8)

        #--------------------#
        # 'Undo' Button      #
        #--------------------#
        # button_undo = Gtk.ToolButton()
        # # set button icon
        # # img_undo = Gtk.Image().new_from_file("images/icons/undo.png")
        # button_undo.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_UNDO))
        # # set tooltip text
        # button_undo.set_tooltip_text('Undo')
        # # event listener
        # button_undo.connect('clicked', self.on_menu)

        # toolbar.insert(button_undo, 14)

        #-----------------------#
        # 'View Changes' Button #
        #-----------------------#
        # button_viewchange = Gtk.ToolButton()
        # # set button icon
        # # img_viewchange = Gtk.Image().new_from_file("images/icons/view-change.png")
        # button_viewchange.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_ABOUT))
        # # set tooltip text
        # button_viewchange.set_tooltip_text('View changes made')
        # # event listener
        # button_viewchange.connect('clicked', self.on_menu)

        # toolbar.insert(button_viewchange, 10)

        #---------------#
        # 'Redo' Button #
        #---------------#
        # button_redo = Gtk.ToolButton()
        # # set button icon
        # # img_redo = Gtk.Image().new_from_file("images/icons/redo.png")
        # button_redo.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_REDO))
        # # set tooltip text
        # button_redo.set_tooltip_text('Redo')
        # # event listener
        # button_redo.connect('clicked', self.on_menu)

        # toolbar.insert(button_redo, 16)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 9)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 10)

        #----------------------#
        # 'Change Font' Button #
        #----------------------#
        # button_changefont = Gtk.ToolButton()
        # # set button icon
        # # img_changefont = Gtk.Image().new_from_file("images/icons/font.png")
        # button_changefont.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_SELECT_FONT))
        # # set tooltip text
        # button_changefont.set_tooltip_text('Change font')
        # # event listener
        # button_changefont.connect('clicked', self.on_menu)

        # toolbar.insert(button_changefont, 13)

        #-----------------------------#
        # 'Increase Font Size' Button #
        #-----------------------------#
        self.button_increase_fontsize = Gtk.ToolButton()
        # set button icon
        # img_increase_fontsize = Gtk.Image().new_from_file("images/icons/increase-font-size.png")
        self.button_increase_fontsize.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_GO_UP))
        # set tooltip text
        self.button_increase_fontsize.set_tooltip_text('Ctrl+Shift+>: Increase font size')
        # event listener
        self.button_increase_fontsize.connect('clicked', self.increase_font)

        toolbar.insert(self.button_increase_fontsize, 11)

        #-----------------------------#
        # 'Decrease Font Size' Button #
        #-----------------------------#
        self.button_decrease_fontsize = Gtk.ToolButton()
        # set button icon
        # img_decrease_fontsize = Gtk.Image().new_from_file("images/icons/decrease-font-size.png")
        self.button_decrease_fontsize.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_GO_DOWN))
        # set tooltip text
        self.button_decrease_fontsize.set_tooltip_text('Ctrl+Shift+<: Decrease font size')
        # event listener
        self.button_decrease_fontsize.connect('clicked', self.decrease_font)

        toolbar.insert(self.button_decrease_fontsize, 12)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 13)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 14)

        #---------------#
        # 'Bold' Button #
        #---------------#
        self.button_bold = Gtk.ToolButton()
        # set button icon
        # img_bold = Gtk.Image().new_from_file("images/icons/bold.png")
        self.button_bold.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_BOLD))
        # set tooltip text
        self.button_bold.set_tooltip_text('Ctrl+B: Bold')
        # event listener
        self.button_bold.connect('clicked', self.bold_clicked)

        toolbar.insert(self.button_bold, 15)

        #-----------------#
        # 'Italic' Button #
        #-----------------#
        self.button_italic = Gtk.ToolButton()
        # set button icon
        # img_italic = Gtk.Image().new_from_file("images/icons/italic.png")
        self.button_italic.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_ITALIC))
        # set tooltip text
        self.button_italic.set_tooltip_text('Ctrl+I: Italic')
        # event listener
        self.button_italic.connect('clicked', self.italic_clicked)

        toolbar.insert(self.button_italic, 16)

        #--------------------#
        # 'Underline' Button #
        #--------------------#
        self.button_underline = Gtk.ToolButton()
        # set button icon
        # img_underline = Gtk.Image().new_from_file("images/icons/underline.png")
        self.button_underline.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_UNDERLINE))
        # set tooltip text
        self.button_underline.set_tooltip_text('Ctrl+U: Underline')
        # event listener
        self.button_underline.connect('clicked', self.underline_clicked)

        toolbar.insert(self.button_underline, 17)

        #------------------------------#
        # 'Reset Type Emphasis' Button #
        #------------------------------#
        self.button_reset = Gtk.ToolButton()
        # set button icon
        # img_reset = Gtk.Image().new_from_file("images/icons/reset.png")
        self.button_reset.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_REFRESH))
        # set tooltip text
        self.button_reset.set_tooltip_text('Reset all text emphasis')
        # event listener
        self.button_reset.connect('clicked', self.clear_clicked)

        toolbar.insert(self.button_reset, 18)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 19)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 20)

        #---------------------#
        # 'Align Left' Button #
        #---------------------#
        self.radio_alignleft = Gtk.RadioToolButton()
        # set button icon
        # img_alignleft = Gtk.Image().new_from_file("images/icons/align-left.png")
        self.radio_alignleft.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_JUSTIFY_LEFT))
        # set tooltip text
        self.radio_alignleft.set_tooltip_text('Ctrl+L: Align left')
        # event listener
        self.radio_alignleft.connect('toggled', self.left_align)

        toolbar.insert(self.radio_alignleft, 21)

        #-----------------------#
        # 'Align Center' Button #
        #-----------------------#
        self.radio_aligncenter = Gtk.RadioToolButton().new_from_widget(self.radio_alignleft)
        # set button icon
        # img_aligncenter = Gtk.Image().new_from_file("images/icons/align-center.png")
        self.radio_aligncenter.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_JUSTIFY_CENTER))
        # set tooltip text
        self.radio_aligncenter.set_tooltip_text('Ctrl+E: Align Center')
        # event listener
        self.radio_aligncenter.connect('toggled', self.center_align)

        toolbar.insert(self.radio_aligncenter, 22)


        #----------------------#
        # 'Align Right' Button #
        #----------------------#
        self.radio_alignright = Gtk.RadioToolButton().new_from_widget(self.radio_alignleft)
        # set button icon
        # img_alignright = Gtk.Image().new_from_file("images/icons/align-right.png")
        self.radio_alignright.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_JUSTIFY_RIGHT))
        # set tooltip text
        self.radio_alignright.set_tooltip_text('Align right')
        # event listener
        self.radio_alignright.connect('toggled', self.right_align)

        toolbar.insert(self.radio_alignright, 23)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 24)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 25)

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
        # button_pagenum = Gtk.ToolButton()
        # # set button icon
        # # img_pagenum = Gtk.Image().new_from_file("images/icons/page-num.png")
        # button_pagenum.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_PAGE_SETUP))
        # # set tooltip text
        # button_pagenum.set_tooltip_text('Insert page numbers')
        # # event listener
        # button_pagenum.connect('clicked', self.on_menu)

        # toolbar.insert(button_pagenum, 29)

        # # separator
        # toolbar.insert(Gtk.SeparatorToolItem(), 30)
        # # separator
        # toolbar.insert(Gtk.SeparatorToolItem(), 31)

        #-----------------#
        # 'Themes' Button #
        #-----------------#
        # button_themes = Gtk.ToolButton()
        # # set button icon
        # # img_themes = Gtk.Image().new_from_file("images/icons/change-theme.png")
        # button_themes.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_COLOR_PICKER))
        # # set tooltip text
        # button_themes.set_tooltip_text('Change slydes theme')
        # # event listener
        # button_themes.connect('clicked', self.on_menu)

        # toolbar.insert(button_themes, 32)

        # # separator
        # toolbar.insert(Gtk.SeparatorToolItem(), 33)
        # # separator
        # toolbar.insert(Gtk.SeparatorToolItem(), 34)

        #---------------#
        # 'Help' Button #
        #---------------#
        self.button_help = Gtk.ToolButton()
        # set button icon
        # img_help = Gtk.Image().new_from_file("images/icons/help.png")
        self.button_help.set_icon_widget(Gtk.Image(stock=Gtk.STOCK_HELP))
        # set tooltip text
        self.button_help.set_tooltip_text('F1: Help')
        # event listener
        self.button_help.connect('clicked', self.help_clicked)

        toolbar.insert(self.button_help, 26)

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


    def on_key(self, widget, event):
        '''
        check event.keyval
        '''
        key = Gdk.keyval_name(event.keyval)

        ctrl = (event.state & Gdk.ModifierType.CONTROL_MASK)

        # align left
        if ctrl and key == "l":
            self.radio_alignleft.set_active(True)
        # align center
        elif ctrl and key == "e":
            self.radio_aligncenter.set_active(True)
        # align right
        elif ctrl and key == "r":
            self.radio_alignright.set_active(True)
        # change font
        elif ctrl and key == "f":
            self.on_menu(self.button_changefont)
        # insert hyperlink
        elif ctrl and key == "k":
            self.insert_link(self.button_hyperlink)
        # add slide
        elif ctrl and key == "m":
            self.add_slide(self.button_addslide)
        # help button
        elif key == "F1":
            self.on_menu(self.button_help)
        # bold
        elif ctrl and key == "b":
            self.bold_clicked(self.button_bold)
        # italic
        elif ctrl and key == "i":
            self.italic_clicked(self.button_italic)
        # underline
        elif ctrl and key == "u":
            self.underline_clicked(self.button_underline)
        # play presentation
        elif key == "F5":
            self.on_menu(self.button_play)
        # save 
        elif key == "F12":
            self.on_menu(self.button_savefile)
        # increase font size
        elif ctrl and key == "greater":
            self.increase_font(self.button_increase_fontsize)
        # decrease font size
        elif ctrl and key == "less":
            self.decrease_font(self.button_decrease_fontsize)
        # page numbers
        elif ctrl and key == "n":
            self.on_menu(self.button_pagenum)
        # change theme
        elif ctrl and key == "t":
            self.on_menu(self.button_themes)
        # load
        elif ctrl and key == "o":
            self.on_menu(self.button_loadfile)
        # insert picture
        elif ctrl and key == "p":
            self.image_clicked(self.button_insertpic)

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

    def help_clicked(self, button):
        os.system('xdg-open ./help.html')

window = Window()
window.main()


