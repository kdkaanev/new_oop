class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [ for  in range(self.pages) ]


    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count / 4)

    def add_photo(self, label):
        for r in  range(len(self.photos)):
            for i in range(len(self.photos)):
                if  self.photos[r][i] == '':
                    self.photos[r][i] = label
                    return f"{label} photo added successfully on page {r +1} slot {i + 1}"
            break
        return "No more free slots"        



    def display(self):
        pass

'