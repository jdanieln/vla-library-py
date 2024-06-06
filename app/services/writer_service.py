from ..models.writer_model import Writer

class WriterService:
    def __init__(self, writer_repository):
        self.writer_respository = writer_repository

    def get_all_writers(self):
        return self.writer_respository.get_all()
    
    def get_writer_by_id(self, writer_id):
        return self.writer_respository.get_by_id(writer_id)
    
    def create_writer(self, data):
        new_writer = Writer(name=data['name'])
        self.writer_respository.create(new_writer)

    def delete_writer(self, writer_id):
        self.writer_respository.delete(writer_id)