class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [ [ 0 for i in range(4) ] for j in range(self.pages) ]


    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count / 4)

    def add_photo(self, label):
        for r in  range(len(self.photos)):
            for i in range(len(self.photos)):
                if not self.photos:
                    self.photos[i].append(label)
                    return f"{label} photo added successfully on page {r +1} slot {i + 1}"
                    break
            break
        return "No more free slots"        



    def display(self):
        pass

p = PhotoAlbum(3)

print(p.add_photo('huj'))
