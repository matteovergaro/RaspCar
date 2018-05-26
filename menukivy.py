import kivy
import time
import math
import datetime 
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from math import cos, sin, pi
from kivy.graphics import Color, Line
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar, ActionLabel
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty


Window.size = (800,480)
Window.clearcolor = (0.094, 0.11, 0.127, 1)


class HomeScreen(Screen):

	time = StringProperty()

	def __init__(self, **kwargs):
		super(HomeScreen, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1)

	def update(self, *args):
		self.time = time.asctime()[:16]

class MainScreen(Screen):
	pass

	# 	def update_clock(self, *args):
	# 		self.canvas.clear()
	# 		with self.canvas:
	# 			time = datetime.datetime.now()
	# 			Color(0.2, 0.5, 0.2)
	# 			Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
	# 			Color(0.3, 0.6, 0.3)
	# 			Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
	# 			Color(0.4, 0.7, 0.4)
	# 			th = time.hour*60 + time.minute
	# 			Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")

class Ticks(Widget):

	def __init__(self, **kwargs):
		super(Ticks, self).__init__(**kwargs)

	def update_ticks(self, *args):
		pass


class NavScreen(Screen):

	time = StringProperty()

	def __init__(self, **kwargs):
		super(NavScreen, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1)

	def update(self, *args):
		self.time = time.asctime()[:16]


class MusicScreen(Screen):

	time = StringProperty()

	def __init__(self, **kwargs):
		super(MusicScreen, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1)

	def update(self, *args):
		self.time = time.asctime()[:16]


class CameraScreen(Screen):

	time = StringProperty()

	def __init__(self, **kwargs):
		super(CameraScreen, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1)

	def update(self, *args):
		self.time = time.asctime()[:16]


class ObdScreen(Screen):

	time = StringProperty()

	def __init__(self, **kwargs):
		super(ObdScreen, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1)

	def update(self, *args):
		self.time = time.asctime()[:16]


class RadioScreen(Screen):

	time = StringProperty()

	def __init__(self, **kwargs):
		super(RadioScreen, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1)

	def update(self, *args):
		self.time = time.asctime()[:16]


class SettingsScreen(Screen):

	time = StringProperty()

	def __init__(self, **kwargs):
		super(SettingsScreen, self).__init__(**kwargs)
		Clock.schedule_interval(self.update, 1)

	def update(self, *args):
		self.time = time.asctime()[:16]


class ScreenManagement(ScreenManager):
	pass


kivy = Builder.load_file("menukivy.kv")

class Menu(App):

	def build(self):
		return kivy

if __name__ == '__main__':
    Menu().run()