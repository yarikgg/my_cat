#тути v1.0
import pygame

import random

pygame.font.init()

import time

W = 1980
H = 1080

display = pygame.display.set_mode((W, H))
pygame.display.set_caption('туть_GAME')

tuti = pygame.image.load("туть.png")
bombe = pygame.image.load("bombe.png")
whiskas = pygame.image.load("whiskas.png")
mywk = pygame.image.load("mywk.png")
menu = pygame.image.load("menu.png")
exp = pygame.image.load("exp.png")
tree = pygame.image.load("crestmass-tree.png")
#БУДИИИИИИИИИИИИИИИИИИИИИИЛЬНИК

i = 3
black = (0, 0, 0)

score = 0

m = 1

pygame.mouse.set_visible(False)

t_x = 0
t_y = 665
w_y = 50
m_y = -200
b_y = 50

wx = random.randint(70, 1850)
mx = random.randint(70, 1850)
bx = random.randint(70, 1850)
bx2 = random.randint(70, 1850)
bx3 = random.randint(70, 1850)
 
white = (255,255,255)
display.fill(white)

cheat = 1

display.blit(tuti,(t_x, t_y))

RED = (255,0,0)
YELLOW = (255, 255, 0)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				print(str(score)+"-ваш рекорд")
				exit()
			elif event.key == pygame.K_RIGHT:
				t_x += 90 
			elif event.key == pygame.K_LEFT:
				t_x -= 90
			elif event.key == pygame.K_f:
				cheat += 1
				if cheat >= 3:
					cheat = 1
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pygame.mouse.set_visible(True)
	display.fill(white)
	display.blit(whiskas,(wx, w_y))
	display.blit(mywk,(mx, m_y))
	display.blit(bombe, (bx, b_y))

	tx = t_x + 740
	w_y += 2
	m_y += 4
	b_y += 2

	if wx >= t_x and w_y == 800:
		if wx <= tx and w_y == 800: 
			w_y = 50
			wx = random.randint(70, 1850)
			score += 1				
 
	if bx >= t_x and b_y == 800:
		if bx <= tx and b_y == 800: 
			i -= 1
			for x in range(50):
				display.blit(exp,(bx,650))
			bx = random.randint(70, 1850)
			b_y = 50
			pygame.display.update()
			
	if mx >= t_x and m_y == 800:
		if mx <= tx and m_y == 800: 
			score += 10
			m_y = 2001

	if w_y == 1080 and cheat == 1:
		print("ваш рекорд =", score)
		f = open('score.txt', 'w')
		f.write(' ваш рекорд = '+str(score))
		f.close
		display.fill(white)
		display.blit(menu,(0,0))
		pygame.display.update()
		time.sleep(3)
		break
		if event.type == pygame.MOUSEBUTTONDOWN:
			i = 3
	
	if w_y >= 1080:
		w_y = 50
		
	if b_y == 1080:
		b_y = 50
		bx = random.randint(70, 1850)
	if i == 0 and cheat == 1:
		display.fill(white)
		display.blit(menu,(0,0))
		pygame.display.update()
		time.sleep(3)
		print("ваш рекорд =",score)
		f = open('score.txt', 'a')
		f.write(' ваш рекорд =',str(score))
		f.close
		break

	if m_y == 1080:
		mx = random.randint(70, 1850)
		m_y = 50

	display.blit(tuti,(t_x, t_y))
	pygame.display.update()
