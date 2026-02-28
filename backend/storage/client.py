import redis.asyncio as redis
import os

# Use Railway's Redis URL if available, otherwise default to local
redis_url = os.getenv("REDIS_URL", "redis://redis:6379")

redis_client = redis.from_url(
    redis_url,
    decode_responses=True
)