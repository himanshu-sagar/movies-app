from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config import CACHE_REDIS_HOST, CACHE_REDIS_PORT

db = SQLAlchemy()
cache = Cache(config={
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_HOST": CACHE_REDIS_HOST,
    "CACHE_REDIS_PORT": CACHE_REDIS_PORT
})
