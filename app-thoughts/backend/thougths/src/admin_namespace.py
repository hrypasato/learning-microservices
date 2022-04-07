import http.client
from flask_restx import Namespace, Resource
from .models import ThoughtModel
from .db import db

admin_namespace = Namespace('admin', description='Admin operations')


@admin_namespace.route('/thoughts/<int:thought_id>/')
class ThoughtsDelete(Resource):

    @admin_namespace.doc('delete_thought',
                         responses={http.client.NO_CONTENT: 'No content'})
    def delete(self, thought_id):
        '''
        Delete a thought
        '''
        thought = ThoughtModel.query.get(thought_id)
        if not thought:
            # The thought is not present
            return '', http.client.NO_CONTENT

        db.session.delete(thought)
        db.session.commit()

        return '', http.client.NO_CONTENT
