__db = None

def init_db(sanic, loop):
    global __db
    from motor.motor_asyncio import AsyncIOMotorClient
    mongo_uri = "mongodb://127.0.0.1:27017/myapp"
    __db = AsyncIOMotorClient(mongo_uri)['myapp']

def current_db():
    return __db
