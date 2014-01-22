import re

import lib


class JPEGImage(object):
    def __init__(self, fname=None, blob=None):
        if (not fname and not blob) or (fname and blob):
            raise Exception("Must initialize with either fname or blob.")
        if fname is not None:
            with open(fname, 'rb') as fp:
                self.data = fp.read()
        elif blob is not None:
            self.data = blob

    def rotate(self, angle):
        if angle % 90:
            raise ValueError("angle must be a multiple of 90.")
        self.data = lib.Transformation(self.data).rotate(angle)
        return self

    def flip(self, direction):
        if direction not in ('horizontal', 'vertical'):
            raise ValueError("direction must be either 'vertical' or "
                             "'horizontal'")
        self.data = lib.Transformation(self.data).flip(direction)
        return self

    def transpose(self):
        self.data = lib.Transformation(self.data).transpose()
        return self

    def transverse(self):
        self.data = lib.Transformation(self.data).transverse()
        return self

    def crop(self, x, y, width, height):
        self.data = lib.Transformation(self.data).crop(x, y, width, height)
        return self

    def scale(self, width, height, quality=75):
        self.data = lib.Transformation(self.data).scale(width, height, quality)
        return self

    def save(self, fname):
        if not re.match(r'^.*\.jp[e]*g$', fname.lower()):
            raise ValueError("fname must refer to a JPEG file, i.e. end with "
                             "'.jpg' or '.jpeg'")
        with open(fname, 'w') as fp:
            fp.write(self.data)

    def as_blob(self):
        return self.data