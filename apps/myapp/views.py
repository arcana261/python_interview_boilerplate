from sanic.views import HTTPMethodView
from sanic.exceptions import NotFound, URLBuildError
from sanic import response
from .db import current_db

class BooksView(HTTPMethodView):
    async def get(self, request):
        docs = await current_db().books.find().to_list(length=100)
        for doc in docs:
            doc['id'] = str(doc['_id'])
            del doc['_id']
        return response.json(docs)

    async def post(self, request):
        doc = request.json
        object_id = await current_db().test_col.save(doc)
        return response.json({'object_id': str(object_id)})
