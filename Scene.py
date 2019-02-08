import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, cairo, Pango



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
		self.pixbuflist = [] #image list


		#Sets our default text and font
		self.currentfont = "sans"
		self.currentfontsize = "11"
		self.set_font(self.currentfont, self.currentfontsize)
		
		#set top and bottom margins. Note: Right/Left aren't compatible with text wrapping
		self.textview.set_top_margin(25)
		self.textview.set_bottom_margin(25)
		#Handle right/left margins as non-editible textboxes
		self.rmsize = 25
		self.lmsize = 25
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
		self.textview.modify_font(Pango.FontDescription(pangoFont))
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



	def set_font(self, font, size):
		#take string font and integer size to resize the fonts
		if(int(size) < 11):
			print("Warning! This font may be too small to read!")
			#stubbed, do something to show warning to end user
		newfont = font+" "+str(size)
		self.currentfont = font
		self.currentfontsize = size
		self.textview.modify_font(Pango.FontDescription(self.currentfont))



	def get_height(self):
		return self.height



	def get_width(self):
		return self.width



	def set_dimensions(self, newwidth, newheight):
		#set the width and height of the slide
		self.width = newwidth
		self.height = newheight
		self.textview.set_size_request(width, height)



	def insert_image(self, image):
		#Insert an image into the slide
		#Stubbed, still deciding on doability and how to do it.
		#I'm thinking insert an image file as a child widget. We should have a button to handle this in UI
		#The filetype for these will be as a pixbuf, since it can be easily inserted and resized
		mark = self.textbuffer.get_insert();
		iterator = self.textbuffer.get_iter_at_mark(mark)
		self.textbuffer.insert_pixbuf(iterator ,image)
		#untested



	def tag_button_clicked(self, tag):
		#This function allows us to do something when a button is pressed
		#The button's tag will tell us what to do, these will be coded into the buttons
		bounds = self.textbuffer.get_selection_bounds #selected text
		if len(bounds) != 0:
			start, end = bounds
			self.textbuffer.apply_tag(tag, start, end)


	def thumbnail(self):
		#Resize slide and everything on it to the thumbnail size
		one=1
		#stubbed

	def fullscreen(self):
		#Resize slide and all its elements to fit the fullscreen
		one=1
		#stubbed
	


class SlideDeck:
	def __init__(self):
		self.deck = []






def slideTest():
	win = Gtk.Window()
	win.set_default_size(1000,1000)
	win.connect("destroy", Gtk.main_quit)
	
	slide = Slide()
	win.add(slide.get_slide())
	#slide.resize_slide(1820,1080, "sans 42") #Successful
	#slide.font_size("sans", 40) #Successful
	win.show_all()
	
	Gtk.main()
	



slideTest()