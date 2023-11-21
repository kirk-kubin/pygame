import pygame as pg

def load_player_images():
    player_image = pg.image.load("project/images/gun/gun.png")
    player_image = pg.transform.scale(player_image, (player_image.get_width()+154.55, player_image.get_height()+100))
    player_image1 = pg.image.load("project/images/gun/gun1.png")
    player_image1 = pg.transform.scale(player_image1, (player_image1.get_width()+154.55, player_image1.get_height()+100))
    player_image2 = pg.image.load("project/images/gun/gun2.png")
    player_image2 = pg.transform.scale(player_image2, (player_image2.get_width()+154.55, player_image2.get_height()+100))
    player_image3 = pg.image.load("project/images/gun/gun3.png")
    player_image3 = pg.transform.scale(player_image3, (player_image3.get_width()+154.55, player_image3.get_height()+100))
    return player_image,player_image1,player_image2,player_image3

def load_flash_images():
    flash_image = pg.image.load("project/images/flash/flash.png")
    flash_image = pg.transform.scale(flash_image, (flash_image.get_width()+80, flash_image.get_height()+40))
    flash_image1 = pg.image.load("project/images/flash/flash1.png")
    flash_image1 = pg.transform.scale(flash_image1, (flash_image1.get_width()+80, flash_image1.get_height()+40))
    flash_image2 = pg.image.load("project/images/flash/flash2.png")
    flash_image2 = pg.transform.scale(flash_image2, (flash_image2.get_width()+80, flash_image2.get_height()+40))
    flash_image3 = pg.image.load("project/images/flash/flash3.png")
    flash_image3 = pg.transform.scale(flash_image3, (flash_image3.get_width()+80, flash_image3.get_height()+40))
    flash_image4 = pg.image.load("project/images/flash/flash4.png")
    flash_image4 = pg.transform.scale(flash_image4, (flash_image4.get_width()+80, flash_image4.get_height()+40))
    flash_image5 = pg.image.load("project/images/flash/flash5.png")
    flash_image5 = pg.transform.scale(flash_image5, (flash_image5.get_width()+80, flash_image5.get_height()+40))
    return flash_image,flash_image1,flash_image2,flash_image3,flash_image4,flash_image5