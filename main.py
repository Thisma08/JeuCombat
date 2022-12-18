import pygame as pg
import sys

from f_constantes import *

pg.init()
horloge = pg.time.Clock()

ecran = pg.display.set_mode((L_ECRAN, H_ECRAN))
pg.display.set_caption('Titre fenêtre')

rect_image1 = pg.Rect(0, 0, 100, 50)
rect_image1.center = (170, 75)

rect_image2 = pg.Rect(0, 0, 100, 50)
rect_image2.center = (390, 75)

rect_image3 = pg.Rect(0, 0, 100, 50)
rect_image3.center = (610, 75)

rect_image4 = pg.Rect(0, 0, 100, 50)
rect_image4.center = (830, 75)

rect_image5 = pg.Rect(0, 0, 100, 50)
rect_image5.center = (170, 250)

rect_image6 = pg.Rect(0, 0, 100, 50)
rect_image6.center = (390, 250)

rect_image7 = pg.Rect(0, 0, 100, 50)
rect_image7.center = (610, 250)

rect_image8 = pg.Rect(0, 0, 100, 50)
rect_image8.center = (830, 250)

p = 1
rect_selection = pg.Rect(0, 0, 120, 70)
rect_selection.center = (170, 75)

rect_joueur = pg.Rect(0, 0, 100, 100)
rect_joueur.center = (L_ECRAN//2, H_ECRAN//2 + 50)

vx_joueur = 5
vy_joueur = 0

saut = False

li = 1
col = 1

font_name = pg.font.match_font(FONT_NAME)

ecranChoixPerso = True
ecranJeu = False

choisi = False


while True:
    if ecranChoixPerso:
        ecran.fill(NOIR)

        pg.draw.rect(ecran, OR, rect_selection)

        pg.draw.rect(ecran, COULEURS_PERSO[0], rect_image1)
        pg.draw.rect(ecran, COULEURS_PERSO[1], rect_image2)
        pg.draw.rect(ecran, COULEURS_PERSO[2], rect_image3)
        pg.draw.rect(ecran, COULEURS_PERSO[3], rect_image4)
        pg.draw.rect(ecran, COULEURS_PERSO[4], rect_image5)
        pg.draw.rect(ecran, COULEURS_PERSO[5], rect_image6)
        pg.draw.rect(ecran, COULEURS_PERSO[6], rect_image7)
        pg.draw.rect(ecran, COULEURS_PERSO[7], rect_image8)

        if choisi:
            font = pg.font.Font(font_name, 35)
            text_surface = font.render("Vous avez choisi : " + PERSONNAGES[perso_choisi - 1], True, BLANC)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (L_ECRAN // 2, 350)
            ecran.blit(text_surface, text_rect)

        for evenement in pg.event.get():
            if evenement.type == pg.KEYDOWN:
                if evenement.key == pg.K_RIGHT:
                    if col < 4:
                        col += 1
                        p += 1
                        rect_selection.centerx += 220
                    else:
                        col = 1
                        p -= 3
                        rect_selection.centerx = 170

                if evenement.key == pg.K_LEFT:
                    if col > 1:
                        col -= 1
                        p -= 1
                        rect_selection.centerx -= 220
                    else:
                        col = 4
                        p += 3
                        rect_selection.centerx = 830

                if evenement.key == pg.K_DOWN:
                    if li < 2:
                        li += 1
                        p += 4
                        rect_selection.centery += 175
                    else:
                        li = 1
                        p -= 4
                        rect_selection.centery -= 175

                if evenement.key == pg.K_UP:
                    if li > 1:
                        li -= 1
                        p -= 4
                        rect_selection.centery -= 175
                    else:
                        li = 2
                        p += 4
                        rect_selection.centery += 175

                if evenement.key == pg.K_RETURN:
                    choisi = True
                    perso_choisi = p
                    ecranChoixPerso = False
                    ecranJeu = True

            if evenement.type == pg.QUIT:
                pg.quit()
                sys.exit()

    if ecranJeu:
        ecran.fill(NOIR)

        for evenement in pg.event.get():
            if evenement.type == pg.QUIT:
                pg.quit()
                sys.exit()

        input = pg.key.get_pressed()
        if input[pg.K_LEFT]:
            rect_joueur.left -= vx_joueur
        if input[pg.K_RIGHT]:
            rect_joueur.right += vx_joueur
        if input[pg.K_UP]:
            if saut == False:
                vy_joueur = -20
                saut = True

        vy_joueur += 1

        if rect_joueur.bottom > H_ECRAN//2 + 100:
            rect_joueur.bottom = H_ECRAN//2 + 100
            vy_joueur = 0
            saut = False

        rect_joueur.centery += vy_joueur

        pg.draw.rect(ecran, COULEURS_PERSO[perso_choisi-1], rect_joueur)

    pg.display.flip()
    horloge.tick(60)
