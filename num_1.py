from kivymd.app import MDApp
from kivy.base import Builder
from kivy.clock import Clock
from random import random,randrange
from kivy.graphics import Color,Ellipse
from kivymd.uix.menu import MDDropdownMenu
from kivy.animation import Animation
from time import sleep
a = '''
MDScreen:
	MDScreen:
		md_bg_color:0.0,0.37441226840019226,0.3359342464586584,0.743147611618042

########## bg screen############
	MDScreen:
		id:bg
		pos_hint:{'x':-1}
		md_bg_color:0.0,0.37441226840019226,0.3359342464586584,0.743147611618042
		MDFloatLayout:
			md_bg_color:0.0,0.37441226840019226,0.3359342464586584,0.243147611618042
			radius:[23,]
			size_hint:.73,.6
			pos_hint:{'center_x':.40,'center_y':.5}

#############buttons########		
			MDRaisedButton:
				size_hint:.9,.1
				pos_hint:{'center_x':.5,'center_y':.75}
				text:'click me 1'
				on_release:sm.current = 's1'
				on_release:app.abc(sm),app.ab(s1)
				
			MDRaisedButton:
				size_hint:.9,.1
				pos_hint:{'center_x':.5,'center_y':.6}
				text:'click me 2'
				on_release:sm.current = 's2'
				on_release:app.abc(sm),app.ab(s2)
			MDRaisedButton:
				size_hint:.9,.1
				pos_hint:{'center_x':.5,'center_y':.45}
				text:'click me 3'
				on_release:sm.current = 's3'
				on_release:app.abc(sm),app.ab(s3)
			MDRaisedButton:
				size_hint:.9,.1
				pos_hint:{'center_x':.5,'center_y':.3}
				text:'click me 4'
				on_release:sm.current = 's4'
				on_release:app.abc(sm),app.ab(s4)

##########front screens##########
	ScreenManager:
		id:sm
		xx:.5
		yy:1
		yy1:.5
		
##########screen one############
		MDScreen:
			name:'s1'
			id:s1
			pos_hint:{'center_y':sm.yy1,'center_x':sm.xx}
			size_hint_y:sm.yy	
			md_bg_color:0.004499173745876405,0.30743211217042876,0.47640473813545414,1.0
##############################
			MDBoxLayout:
				padding:15
				md_bg_color:1,1,1,1
				pos_hint:{'top':.97,'center_x':sm.xx}
				size_hint:.9,.1
				radius:[36,]
				MDIconButton:
					user_font_size:50
					icon:'menu'
					pos_hint:{'center_y':.5}
					theme_text_color:'Custom'
					text_color:1,0,0,1
					on_release:app.abc(sm)
					on_release:s1.radius=[36,]
##############################
			MDBoxLayout:
				padding:10
				md_bg_color:0,0,0,.09
				size_hint:None,None
				size:690,400
				pos_hint:{'top':.85,'center_x':sm.xx}
				ScrollView:
					bar_width:0
					MDGridLayout:
						rows:1
						spacing:15
						size_hint:None,None
						size:900,380
						MDBoxLayout:
							md_bg_color:0,0,0,.6
							size:380,200
							SmartTileWithLabel:
								source:'/sdcard/cc.png'
								text:'[color=6699ff][b][i]available cources[/i]:[/b][/color]\\n([color=00ff00]40[/color])'
								radius:[36,]
								on_release:print('ok')
						MDBoxLayout:
							radius:[36,]
							md_bg_color:1,.3,.3,.7
							size:380,200
							SmartTileWithLabel:
								source:'/sdcard/cc1.png'
								text:'[color=6699ff][b][i]available cources[/i]:[/b][/color]\\n([color=00ff00]40[/color])'
						MDBoxLayout:
							radius:[36,]
							md_bg_color:1,.3,.3,.7
							size:380,200
							SmartTileWithLabel:
								source:'/sdcard/cc2.png'
								text:'[color=6699ff][b][i]available cources[/i]:[/b][/color]\\n([color=00ff00]40[/color])'
############################
			MDBoxLayout:
				padding:20
				md_bg_color:.2,.5,.6,.8
				size_hint:.9,.5
				pos_hint:{'center_y':.28,'center_x':sm.xx}
				ScrollView:
					MDLabel:
						text:'[color=ff00ff][b]welcome:[/b][/color]\\nsjakakhshdhdffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff\\njdjdkjsjdjdjdjjsnebeb\\nebnebenenenej\\njejwjwjwjenejsjje\\nkwkwkkwkwk\\nwj\\nsjakakhshdhdffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff\\njdjdkjsjdjdjdjjsnebeb\\nebnebenenenej\\njejwjwjwjenejsjje\\nkwkwkkwkwk\\nwj\\nsjakakhshdhdffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff\\njdjdkjsjdjdjdjjsnebeb\\nebnebenenenej\\njejwjwjwjenejsjje\\nkwkwkkwkwk\\nwjw'	
						markup:True					
							
					
			
				
##########screen two#########		
		MDScreen:
			name:'s2'
			id:s2
			md_bg_color:0.004499173745876405,0.30743211217042876,0.47640473813545414,1.0	
			pos_hint:{'center_y':sm.yy1,'center_x':sm.xx}
			size_hint_y:sm.yy
			MDBoxLayout:
				padding:15
				md_bg_color:1,1,1,1
				pos_hint:{'top':.97,'center_x':sm.xx}
				size_hint:.9,.1
				radius:[36,]
				MDIconButton:
					user_font_size:50
					icon:'menu'
					pos_hint:{'center_y':.5}
					theme_text_color:'Custom'
					text_color:app.theme_cls.accent_color
					on_release:app.abc(sm)
					on_release:s2.radius=[36,]
			MDLabel:
				text:'welcome 2'
				halign:'center'
##########screen three###########
		MDScreen:
			name:'s3'
			id:s3
			md_bg_color:0.004499173745876405,0.30743211217042876,0.47640473813545414,1.0	
			pos_hint:{'center_y':sm.yy1,'center_x':sm.xx}
			size_hint_y:sm.yy
			MDBoxLayout:
				padding:15
				md_bg_color:1,1,1,1
				pos_hint:{'top':.97,'center_x':sm.xx}
				size_hint:.9,.1
				radius:[36,]
				MDIconButton:
					user_font_size:50
					icon:'menu'
					pos_hint:{'center_y':.5}
					theme_text_color:'Custom'
					text_color:app.theme_cls.accent_color
					on_release:app.abc(sm)
					on_release:s3.radius=[36,]
			MDLabel:
				text:'welcome 3'
				halign:'center'
				
##########screen four###########
		MDScreen:
			name:'s4'
			id:s4
			md_bg_color:0.004499173745876405,0.30743211217042876,0.47640473813545414,1.0
			pos_hint:{'center_y':sm.yy1,'center_x':sm.xx}
			size_hint_y:sm.yy
			MDBoxLayout:
				padding:15
				md_bg_color:1,1,1,1
				pos_hint:{'top':.97,'center_x':sm.xx}
				size_hint:.9,.1
				radius:[36,]
				MDIconButton:
					user_font_size:50
					icon:'menu'
					pos_hint:{'center_y':.5}
					theme_text_color:'Custom'
					text_color:app.theme_cls.accent_color
					on_release:app.abc(sm)
					on_release:s4.radius=[36,]
			MDLabel:
				text:'welcome 4'
				halign:'center'
				
'''

class my(MDApp):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
	def build(self,):
		self.a = Builder.load_string(a)
		self.theme_cls.primary_palette = 'Blue'
		self.theme_cls.accent_palette = 'Purple'
		return self.a
############################	
	def abc(self,widget,*args):
		if self.a.ids.sm.xx == .5 :
			anim = Animation(duration=.2,xx=.9,yy=.9,yy1=.475)
			anim.start(widget)
			self.a.ids.bg.pos_hint={'x':0}
		else:
			anim = Animation(duration=.2,xx=.5,yy1=.5,yy=1)
			anim.start(widget)
			self.abb(self.a.ids.bg)
			self.a.ids.s1.radius = [0,0,0,0]
			self.a.ids.s2.radius = [0,0,0,0]
			self.a.ids.s3.radius = [0,0,0,0]
			self.a.ids.s4.radius = [0,0,0,0]
##############################
	def ab(self,widget,*args):
		anim = Animation(duration=.2,size_hint=(1,1),pos_hint={'center_x':.5,'center_y':.5},radius=[0,0,0,0])
		anim.start(widget)
##############################
	def abb(self,widget,*args):
		if self.a.ids.bg.pos_hint=={'x':0}:
			anim = Animation(duration=.1,pos_hint={'x':-1})
			anim.start(widget)
		elif self.a.ids.bg.pos_hint=={'x':-1}:
			anim = Animation(duration=.1,pos_hint={'x':0})
			anim.start(widget)
				

my().run()