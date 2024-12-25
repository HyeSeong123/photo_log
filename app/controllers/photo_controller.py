from app.models.photo import Photo

class PhotoController:
    @staticmethod
    def add_photo(photo_name, width, height, creation_date, modification_date, text, keywords):
        photo = Photo(photo_name, width, height, creation_date, modification_date, text, keywords)
        photo.save()