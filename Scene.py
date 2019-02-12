import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, cairo, Pango, GdkPixbuf



class Slide:

    def __init__(self):
        #Initializes the basic slide. Handled as a GTK text view
        self.box = Gtk.Grid()
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_hexpand(False)
        self.scrolledwindow.set_vexpand(False)
        self.box.add(self.scrolledwindow)
        self.textview = Gtk.TextView()
        self.height = 540
        self.width = 910
        self.scrolledwindow.set_size_request(self.width, self.height)
        self.textview.set_size_request(self.width, self.height) #16:9 aspect ratio. Can be changed as needed
        self.textbuffer = self.textview.get_buffer()
        self.images = [] #image list
        self.imagemarks = []

        #Sets our default text and font
        self.currentfont = "sans"
        self.currentfontsize = "11"
        self.set_font(self.currentfont, self.currentfontsize, False)
        
        #set top and bottom margins. Note: Right/Left aren't compatible with text wrapping
        self.textview.set_top_margin(25)
        self.textview.set_bottom_margin(25)
        #Handle right/left margins as non-editible textboxes
        self.rmsize = 25 #size of the left margin
        self.lmsize = 25 #size of the right margin
        self.rightmargin = Gtk.TextView()
        self.rightmargin.set_editable(False)
        self.rightmargin.set_size_request(25, self.height)
        self.box.attach_next_to(self.rightmargin, self.scrolledwindow, 1,1,1)

        self.leftmargin = Gtk.TextView()
        self.leftmargin.set_editable(False)
        self.leftmargin.set_size_request(25, self.height)
        self.box.attach_next_to(self.leftmargin, self.scrolledwindow, 0, 1, 1)



        self.textbuffer.set_text("You can type here. Select and delete this text to remove.")
        #Allows wraparound. Character wraparound was chosen over word wraparound to prevent
        self.textview.set_wrap_mode(Gtk.WrapMode.CHAR)
        #Long words from increasing slide size
        self.scrolledwindow.add(self.textview) 
        #self.box.show()



    def resize_slide(self, width, height, pangoFont):
        #Resizes the slide and the textbox as a result.
        self.textview.set_size_request(width-(self.lmsize+self.rmsize), height)
        self.leftmargin.set_size_request(self.lmsize, height)
        self.rightmargin.set_size_request(self.rmsize, height)
        #Pango requires a string w/font and size. Example: "Sans 20"
        self.textview.modify_font(Pango.FontDescription(pangoFont)) #add scrollbar as well

        #Stubbed, needs to find a way to resize images once they are added.



    def margin_size(margin, marginsize):
        if margin == "left":
            self.leftmargin.set_size_request(marginsize, self.height)
            self.lmsize = marginsize
        elif margin == "right":
            self.rightmargin.set_size_request(marginsize, self.height)
            self.rmsize == marginsize
        elif margin == "top":
            self.textview.set_top_margin(marginsize)
        elif margin == "top":
            self.textview.set_bottom_margin(marginsize)



    def get_slide(self):
        #returns the slide object to be used as needed
        return self.box



    def get_font(self):
        #returns the string describing the current font
        return self.currentfont



    def set_font(self, font, size, warn):
        #take string font and integer size to resize the fonts
        if(int(size) < 11 and warn == True):
            print("Warning! This font may be too small to read!")
            #stubbed, do something to show warning to end user
        newfont = font+" "+str(size)
        self.currentfont = font
        self.currentfontsize = size
        self.textview.modify_font(Pango.FontDescription(newfont))



    def set_font_at(self, font, size):
        #Change only the font in the currently selected area
        two==2
        #stubbed



    def get_height(self):
        return self.height



    def get_width(self):
        return self.width



    def set_dimensions(self, newwidth, newheight):
        #set the width and height of the slide
        self.width = newwidth-(self.lmsize+self.rmsize)
        self.height = newheight
        self.set_font(self.currentfont, 2, False)
        self.leftmargin.set_size_request(self.lmsize, self.height)
        self.rightmargin.set_size_request(self.rmsize, self.height)
        self.scrolledwindow.set_size_request(self.width, self.height)
        self.textview.set_size_request(self.width, self.height)
        

    def insert_image_clicked(self,button):
        dialog = Gtk.FileChooserDialog ("Open Image", button.get_toplevel(), Gtk.FIleChooserAction.OPEN)
        dialog.add_button(Gtk.STOCK_CANCEL, 0)
        dialog.add_button(Gtk.STOCK_OK, 1)
        dialog.set_default_response(1)

        filefilter = Gtk.FileFilter()
        filefilter.add_pixbuf_formats()
        dialog.set_filter(filefilter)

        if dialog.run() == 1:
            pic = GdkPixbuf.Pixbuf.new_from_file(dialog.get_filename())
            self.insert_image(pic)

        dialog.destroy()


    def insert_image(self, image):
        #Insert an image into the slide
        #Stubbed, still deciding on doability and how to do it.
        #I'm thinking insert an image file as a child widget. We should have a button to handle this in UI
        #The filetype for these will be as a pixbuf, since it can be easily inserted and resized
        mark = self.textbuffer.get_insert();
        iterator = self.textbuffer.get_iter_at_mark(mark)
        self.textbuffer.insert_pixbuf(iterator ,image)
        self.images.append(image)
        self.imagemarks.append(mark)
        #untested



    def scale_images(self, newwidth, newheight):
        #scale all images to the new dimensions
        index = 0
        for image in self.images:
            image = image.scale_simple(newwidth, newheight, 2)
            mark = self.imagemarks[0]
            iterator = self.textbuffer.get_iter_at_mark(mark)
            self.textbuffer.backspace(iterator, True, True)
            self.textbuffer.insert_pixbuf(iterator ,image)


    def tag_button_clicked(self, button, tag):
        #This function allows us to do something when a button is pressed
        #The button's tag will tell us what to do, these will be coded into the buttons
        bounds = self.textbuffer.get_selection_bounds #selected text
        if len(bounds) != 0:
            start, end = bounds
            self.textbuffer.apply_tag(tag, start, end)


    def thumbnail(self):
        #Resize slide and everything on it to the thumbnail size
        self.set_dimensions(100, 100)
        #stubbed


    def fullscreen(self):
        #Resize slide and all its elements to fit the fullscreen
        one=1
        #stubbed





class SlideDeck:
    def __init__(self):
        self.deck = []
        self.buttons = []
        firstslide = Slide()
        self.deck.append(firstslide)
        self.currentslide = firstslide
        self.grid = Gtk.Grid()
        self.list = Gtk.ListBox()
        self.side = Gtk.ScrolledWindow()
        self.side.set_size_request(100,540)
        self.side.add(self.list)
        self.grid.add(self.side)
        self.grid.add(firstslide.get_slide())
        firstbutton = Gtk.Button(label = "1")
        firstbutton.connect("clicked", self.on_button_clicked)
        self.list.add(firstbutton)
        self.buttons.append(firstbutton)



    def get_current_slide(self):
        #Returns the current slide
        return self.currentslide

    def on_button_clicked(self, button):
        slide_num = int(button.get_label())
        self.set_current_slide(slide_num)

    def set_current_slide(self, slide_number):
        self.grid.remove(self.currentslide.get_slide())
        self.list.show()
        self.currentslide = self.retrieve_slide(slide_number)
        self.grid.add(self.currentslide.get_slide())
        self.currentslide.get_slide().show()
        self.grid.show_all()


    def make_new_slide(self):
        #Make a new slide then return it
        newslide = Slide()
        #newslide.set_font("sans", "25") #used to test that making a new slide works
        self.deck.append(newslide)
        newindex = len(self.deck)
        newbutton = Gtk.Button(label = newindex)
        newbutton.connect("clicked", self.on_button_clicked)
        self.list.add(newbutton)
        self.buttons.append(newbutton)
        return newslide


    def retrieve_slide(self, slide_number):
        #retrieve the slide in the position specified
        #Note: The slides will start page count with 1, but the list iterator starts with 0.
        #To rectify this, we will subtract 1 from the input number
        goal = slide_number-1
        index = 0
        #Iterate through the deck and return the right slide
        if goal < len(self.deck):
            for slide in self.deck:
                if index == goal:
                    return slide
                index = index+1
        return currentslide

    def get_view(self):
        return self.grid






def slideTest():
    win = Gtk.Window()
    win.set_default_size(1000,1000)
    win.connect("destroy", Gtk.main_quit)
    
    slidedeck = SlideDeck()
    slide = slidedeck.get_current_slide()
    win.add(slidedeck.get_view())
    slidedeck.make_new_slide()
    slide = slidedeck.retrieve_slide(2)
    slidedeck.set_current_slide(2)
    #slide.resize_slide(1820,1080, "sans 42") #Successful
    #slide.set_font("sans", 20) #Successful
    pic = GdkPixbuf.Pixbuf.new_from_file("apple-touch-icon-144x144-precomposed.png") #use GdkPixbuf to load images.
    slide.insert_image(pic)
    slide.scale_images(50,50) #works
    
    win.show_all()
    
    Gtk.main()
    



slideTest()