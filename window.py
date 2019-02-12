#the place for window stuff

import gi
import testing as tst
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class Window(Gtk.Window):

    def __init__(self):

        #################
        # window set up #
        #################
        '''
            call super class constructor.
            once the backend is a little more developed, the title of the slide will have
            to be changed and such.
        '''
        Gtk.Window.__init__(self, title='Slydes -- Unititled 1')

        # position window to center of screen when launched
        self.set_position(Gtk.WindowPosition.CENTER)

        # get the screen size of the computer
        screen = Gdk.Screen.get_default()
        # set size of window according to the size of the screen
        self.set_size_request(screen.get_width() - 400, screen.get_height() - 200)

        # a map from names to Gtk.Action objects for the toolbar.
        toolbar_group = Gtk.ActionGroup("toolbar_actions")

        # accel_group = Gtk.AccelGroup()
        # self.add_accel_group(action_group)

        toolbar = self.create_toolbar(toolbar_group)

        ui_manager = self.create_ui_manager()
        ui_manager.insert_action_group(toolbar_group)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        toolbar.unset_style()
        box.pack_start(toolbar, False, False, 0)


        self.add(box)

        # connect and show window
        self.connect('destroy', Gtk.main_quit)
        self.show_all()




    # create_ui_manager takes in THIS window and returns a ui manager. 
    def create_ui_manager(self):
        ui_manager = Gtk.UIManager()

        # add the accelerator group to the toplevel window
        # accelerators: shortcuts for activating a menu item
        # will look into later for use
        # accel_group = ui_manager.get_accel_group()
        # self.add_accel_group(accel_group)
        return ui_manager




    # create_toolbar takes in THIS window and creates/displays the toolbar.
    # the toolbar is from which users can interact with and manage their slides appearance and such.
    def create_toolbar(self, action_group):
        toolbar = Gtk.Toolbar()

        #-------------------#
        # 'Load File' Button #
        #-------------------#
        button_loadfile = Gtk.ToolButton()
        # set button icon
        img_loadfile = Gtk.Image().new_from_file("images/icons/load-file.png")
        button_loadfile.set_icon_widget(img_loadfile)
        # set tooltip text
        button_loadfile.set_tooltip_text('Load saved slydes presentation')
        # keyboard shortcut
        # button_loadfile.add_accelerator('clicked', action_group, ord('N'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
        # event listener
        button_loadfile.connect('clicked', tst.on_menu)

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

        toolbar.insert(button_play, 2)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 3)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 4)

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

        toolbar.insert(button_textbox, 5)

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
        button_insertpic.connect('clicked', self.on_menu)

        toolbar.insert(button_insertpic, 6)

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
        button_hyperlink.connect('clicked', self.on_menu)

        toolbar.insert(button_hyperlink, 7)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 8)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 9)

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

        toolbar.insert(button_viewchange, 10)

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
        toolbar.insert(Gtk.SeparatorToolItem(), 11)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 12)


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

        toolbar.insert(button_changefont, 13)

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
        button_bold.connect('clicked', self.on_menu)

        toolbar.insert(button_bold, 14)

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
        button_italic.connect('clicked', self.on_menu)

        toolbar.insert(button_italic, 15)

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
        button_underline.connect('clicked', self.on_menu)

        toolbar.insert(button_underline, 16)

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
        button_increase_fontsize.connect('clicked', self.on_menu)

        toolbar.insert(button_increase_fontsize, 17)

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
        button_decrease_fontsize.connect('clicked', self.on_menu)

        toolbar.insert(button_decrease_fontsize, 18)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 19)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 20)

        #---------------------#
        # 'Align Left' Button #
        #---------------------#
        button_alignleft = Gtk.ToolButton()
        # set button icon
        img_alignleft = Gtk.Image().new_from_file("images/icons/align-left.png")
        button_alignleft.set_icon_widget(img_alignleft)
        # set tooltip text
        button_alignleft.set_tooltip_text('Align left')
        # event listener
        button_alignleft.connect('clicked', self.on_menu)

        toolbar.insert(button_alignleft, 21)

        #-----------------------#
        # 'Align Center' Button #
        #-----------------------#
        button_aligncenter = Gtk.ToolButton()
        # set button icon
        img_aligncenter = Gtk.Image().new_from_file("images/icons/align-center.png")
        button_aligncenter.set_icon_widget(img_aligncenter)
        # set tooltip text
        button_aligncenter.set_tooltip_text('Align Center')
        # event listener
        button_aligncenter.connect('clicked', self.on_menu)

        toolbar.insert(button_aligncenter, 22)


        #----------------------#
        # 'Align Right' Button #
        #----------------------#
        button_alignright = Gtk.ToolButton()
        # set button icon
        img_alignright = Gtk.Image().new_from_file("images/icons/align-right.png")
        button_alignright.set_icon_widget(img_alignright)
        # set tooltip text
        button_alignright.set_tooltip_text('Align right')
        # event listener
        button_alignright.connect('clicked', self.on_menu)

        toolbar.insert(button_alignright, 23)

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
        button_pagenum = Gtk.ToolButton()
        # set button icon
        img_pagenum = Gtk.Image().new_from_file("images/icons/page-num.png")
        button_pagenum.set_icon_widget(img_pagenum)
        # set tooltip text
        button_pagenum.set_tooltip_text('Insert page numbers')
        # event listener
        button_pagenum.connect('clicked', self.on_menu)

        toolbar.insert(button_pagenum, 26)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 27)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 28)

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

        toolbar.insert(button_themes, 29)

        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 30)
        # separator
        toolbar.insert(Gtk.SeparatorToolItem(), 31)

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

        toolbar.insert(button_help, 32)

        return toolbar



    def main(self):
        Gtk.main()

    def on_menu(self, button):
        print("Toolbar button clicked.")


window = Window()
window.main()


