# @author NAM HUNG TRAN 

import pygame 

pygame.init()
pygame.display.set_caption("IOS Calculator")

width = 400
height = 600
thickness = 2
screen = pygame.display.set_mode((width,height))

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,179,71)
LIGHT_GRAY = (232, 232, 232)
GRAY = (100, 100, 100)

running = True
string = ""
allowed = False

size = int(width/10)
font = pygame.font.Font('CONSOLA.TTF', size) 

num_1 = font.render('1',True,WHITE)
rect_1 = num_1.get_rect(center = (0.125*width, 0.75*height))

num_2 = font.render('2',True,WHITE)
rect_2 = num_2.get_rect(center = (0.375*width, 0.75*height))

num_3 = font.render('3',True,WHITE)
rect_3 = num_3.get_rect(center = (0.625*width, 0.75*height))

num_4 = font.render('4',True,WHITE)
rect_4 = num_4.get_rect(center = (0.125*width, 7/12*height))

num_5 = font.render('5',True,WHITE)
rect_5 = num_5.get_rect(center = (0.375*width, 7/12*height))

num_6 = font.render('6',True,WHITE)
rect_6 = num_6.get_rect(center = (0.625*width, 7/12*height))

num_7 = font.render('7',True,WHITE)
rect_7 = num_7.get_rect(center = (0.125*width, 5/12*height))

num_8 = font.render('8',True,WHITE)
rect_8 = num_8.get_rect(center = (0.375*width, 5/12*height))

num_9 = font.render('9',True,WHITE)
rect_9 = num_9.get_rect(center = (0.625*width, 5/12*height))

num_0 = font.render('0',True,WHITE)
rect_0 = num_0.get_rect(center = (0.125*width, 11/12*height))

dot = font.render('.', True, WHITE)
rect_dot = dot.get_rect(center = (0.625*width, 11/12*height))

quit = font.render('AC',True, BLACK)
rect_quit = quit.get_rect(center = (0.125*width, 0.25*height))

sign = font.render('+/-',True, BLACK)
rect_sign = sign.get_rect(center = (0.375*width, 0.25*height))

percent = font.render('%',True, BLACK)
rect_percent = percent.get_rect(center = (0.625*width, 0.25*height))

divide = font.render('÷',True, WHITE)
rect_divide = divide.get_rect(center = (0.875*width, 0.25*height))

times = font.render('x', True, WHITE)
rect_times = times.get_rect(center = (0.875*width, 5/12*height))

minus = font.render('-', True, WHITE)
rect_minus = minus.get_rect(center = (0.875*width, 7/12*height))

plus = font.render('+', True, WHITE)
rect_plus = plus.get_rect(center = (0.875*width, 0.75*height))

equal = font.render('=', True, WHITE)
rect_equal = equal.get_rect(center = (0.875*width, 11/12*height))

while running:
	cal = False

	screen.fill(BLACK)

	pygame.draw.rect(screen, LIGHT_GRAY, (0,1/6*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, LIGHT_GRAY, (0.25*width,1/6*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, LIGHT_GRAY, (0.5*width,1/6*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, YELLOW, (0.75*width,1/6*height,0.25*width,1/6*height))

	pygame.draw.rect(screen, GRAY, (0,1/3*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, GRAY, (0.25*width,1/3*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, GRAY, (0.5*width,1/3*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, YELLOW, (0.75*width,1/3*height,0.25*width,1/6*height))

	pygame.draw.rect(screen, GRAY, (0,1/2*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, GRAY, (0.25*width,1/2*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, GRAY, (0.5*width,1/2*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, YELLOW, (0.75*width,1/2*height,0.25*width,1/6*height))

	pygame.draw.rect(screen, GRAY, (0,2/3*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, GRAY, (0.25*width,2/3*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, GRAY, (0.5*width,2/3*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, YELLOW, (0.75*width,2/3*height,0.25*width,1/6*height))

	pygame.draw.rect(screen, GRAY, (0,5/6*height,0.5*width,1/6*height))
	pygame.draw.rect(screen, GRAY, (0.5*width,5/6*height,0.25*width,1/6*height))
	pygame.draw.rect(screen, YELLOW, (0.75*width,5/6*height,0.25*width,1/6*height))

	pygame.draw.line(screen, BLACK, (0,1/6*height), (width, 1/6*height), thickness)
	pygame.draw.line(screen, BLACK, (0,1/3*height), (width, 1/3*height), thickness)
	pygame.draw.line(screen, BLACK, (0,1/2*height), (width, 1/2*height), thickness)
	pygame.draw.line(screen, BLACK, (0,2/3*height), (width, 2/3*height), thickness)
	pygame.draw.line(screen, BLACK, (0,5/6*height), (width, 5/6*height), thickness)

	pygame.draw.line(screen, BLACK, (1/4*width,1/6*height), (1/4*width, 5/6*height), thickness)
	pygame.draw.line(screen, BLACK, (1/2*width,1/6*height), (1/2*width, height), thickness)
	pygame.draw.line(screen, BLACK, (3/4*width,1/6*height), (3/4*width, height), thickness)

	screen.blit(num_0, rect_0)
	screen.blit(num_1, rect_1)
	screen.blit(num_2, rect_2)
	screen.blit(num_3, rect_3)
	screen.blit(num_4, rect_4)
	screen.blit(num_5, rect_5)
	screen.blit(num_6, rect_6)
	screen.blit(num_7, rect_7)
	screen.blit(num_8, rect_8)
	screen.blit(num_9, rect_9)
	screen.blit(dot,rect_dot)
	screen.blit(quit,rect_quit)
	screen.blit(sign,rect_sign)
	screen.blit(percent,rect_percent)
	screen.blit(divide,rect_divide)
	screen.blit(times,rect_times)
	screen.blit(minus,rect_minus)
	screen.blit(plus,rect_plus)
	screen.blit(equal,rect_equal)

	mouseX, mouseY = pygame.mouse.get_pos()

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if (0<mouseX<0.25*width) and (2/3*height<mouseY<5/6*height):
						string += "1"
						allowed = True
						print(string)
					if (0.25*width<mouseX<0.5*width) and (2/3*height<mouseY<5/6*height):	
						string += "2"
						allowed = True
						print(string)
					if (0.5*width<mouseX<0.75*width) and (2/3*height<mouseY<5/6*height):
						string += "3"
						allowed = True
						print(string)
					if (0<mouseX<0.25*width) and (1/2*height<mouseY<2/3*height):
						string += "4"
						allowed = True
						print(string)
					if (0.25*width<mouseX<0.5*width) and (1/2*height<mouseY<2/3*height):
						string += "5"
						allowed = True
						print(string)
					if (0.5*width<mouseX<0.75*width) and (1/2*height<mouseY<2/3*height):
						string += "6"
						allowed = True
						print(string)
					if (0<mouseX<0.25*width) and (1/3*height<mouseY<1/2*height):
						string += "7"
						allowed = True
						print(string)
					if (0.25*width<mouseX<0.5*width) and (1/3*height<mouseY<1/2*height):
						string += "8"
						allowed = True
						print(string)
					if (0.5*width<mouseX<0.75*width) and (1/3*height<mouseY<1/2*height):
						string += "9"
						allowed = True
						print(string)
					if (0<mouseX<0.5*width) and (5/6*height<mouseY<height):
						string += "0"
						allowed = True
						print(string)
					if (0.5*width<mouseX<0.75*width) and (5/6*height<mouseY<height):
						string += "."
						allowed = False
						#cal = False
						print(string)
					if (0<mouseX<0.25*width) and (1/6*height<mouseY<1/3*height):
						string = ""
						allowed = False
						cal = False
						print(string)
					if (0.25*width<mouseX<0.5*width) and (1/6*height<mouseY<1/3*height):
						if (len(string)>0):
							if (string[0] != "-"):
								string = "-" + string
								print(string)
							else:
								string = string[1:]
								print(string)
							allowed = False
					if (0.5*width<mouseX<0.75*width) and (1/6*height<mouseY<1/3*height) and allowed:
						string = float(string)
						string = string/100
						string = str(string)
						print(string)
						allowed = True
					if (0.75*width<mouseX<width) and (1/6*height<mouseY<1/3*height) and allowed:
						string += "/"
						allowed = False
						print(string)
					if (0.75*width<mouseX<width) and (1/3*height<mouseY<1/2*height) and allowed:
						string += "*"
						allowed = False
						print(string)
					if (0.75*width<mouseX<width) and (1/2*height<mouseY<2/3*height) and allowed:
						string += "-"
						allowed = False
						print(string)
					if (0.75*width<mouseX<width) and (2/3*height<mouseY<5/6*height) and allowed:
						string += "+"
						allowed = False
						print(string)
					if (0.75*width<mouseX<width) and (5/6*height<mouseY<height) and allowed:
						cal = True


	text_string = font.render(string, True, WHITE)
	rect_text = text_string.get_rect()
	rect_text.midright = (width, height/12)

	if not cal: 
		screen.blit(text_string, rect_text)
	else:
		string = str(eval(string))
		screen.blit(text_string, rect_text)

	pygame.display.flip()

pygame.quit()



