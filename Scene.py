import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, cairo, Pango



class Slide:

	def __init__(self):
		#Initializes the basic slide. Handled as a GTK text view
		self.box = Gtk.Grid()
		self.textview = Gtk.TextView()
		self.textview.set_size_request(960,540) #16:9 aspect ratio. Can be changed as needed
		self.textbuffer = self.textview.get_buffer()
		self.pixbuflist = [] #image list


		#Sets our default text and font
		self.currentfont = ""
		self.set_font("sans", "11")

		self.textbuffer.set_text("You can type here. Select and delete this text to remove.")
		#Allows wraparound. Character wraparound was chosen over word wraparound to prevent
		#Long words from increasing slide size
		self.box.add(self.textview) 


	def resize_slide(self, width, height, pangoFont):
		#Resizes the slide and the textbox as a result.
		self.textview.set_size_request(width, height)
		#Pango requires a string w/font and size. Example: "Sans 20"
		self.textview.modify_font(Pango.FontDescription(pangoFont))
		#Stubbed, needs to find a way to resize images once they are added.



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
		self.currentfont = newfont
		self.textview.modify_font(Pango.FontDescription(self.currentfont))



	def insert_image(self, image):
		#Insert an image into the slide
		#Stubbed, still deciding on doability and how to do it.
		#I'm thinking insert an image file as a child widget. We should have a button to handle this in UI
		#The filetype for these will be as a pixbuf, since it can be easily inserted and resized
		mark = self.textbuffer.get_insert();
		iterator = self.textbuffer.get_iter_at_mark(mark)
		self.textbuffer.insert_pixbuf(iterator ,image)
		#untested

	def on_button_clicked(self, tag):
		#This function allows us to do something when a button is pressed
		#The button's tag will tell us what to do, these will be coded into the buttons
		bounds = self.textbuffer.get_selection_bounds #selected text
		if len(bounds) != 0:
			start, end = bounds
			self.textbuffer.apply_tag(tag, start, end)









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