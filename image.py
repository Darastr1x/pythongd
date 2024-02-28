import pygame as pg


class Images:
    def __init__(self, filename, trans_x, trans_y):
        self.filename = filename
        self.trans_x = trans_x
        self.trans_y = trans_y

    def load_image(self):
        self.filename = pg.image.load(self.filename).convert()
        self.filename = pg.transform.scale(self.filename, (self.trans_x, self.trans_y))
        return self.filename

    def get_filename(self):
        return self.filename
