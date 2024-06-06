from flask import Blueprint, request, jsonify
from ..services.writer_service import WriterService

def create_writer_blueprint(writer_service: WriterService):
    writer_blueprint = Blueprint('writer', __name__)

    @writer_blueprint.route('/writers', methods=['GET'])
    def get_all_writers():
        writers = writer_service.get_all_writers()
        return jsonify([writer.serialize() for writer in writers])
    
    @writer_blueprint.route('/writer/<int:writer_id>', methods=['GET'])
    def get_writer_by_id(writer_id):
        writer = writer_service.get_writer_by_id(writer_id)
        if writer:
            return jsonify(writer.serialize())
        return jsonify({ 'message': 'Writer not found' }), 404
    
    @writer_blueprint.route('/writer', methods=['POST'])
    def create_writer():
       data = request.get_json()
       writer_service.create_writer(data)
       return jsonify({ 'message': 'Writer created successfully' }), 201 

    @writer_blueprint.route('/writer/<int:writer_id>', methods=['DELETE'])
    def delete_writer(writer_id):
        writer_service.delete_writer(writer_id)
        return jsonify({ 'message': 'Writer deleted successfully' }), 200
    
    return writer_blueprint

    
