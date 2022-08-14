from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category:Category):
        pass

    def add_topic(self, topic:Topic):
        pass

    def add_document(self, document:Document):
        pass



    def edit_category(self, category_id: int, new_name:str):
        pass


    def edit_document(self, document_id: int, new_file_name: str):
        pass

