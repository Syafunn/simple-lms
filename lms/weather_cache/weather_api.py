import time
import json
import redis

redis_client = redis.Redis(
    host="redis",
    port=6379,
    db=2,
    decode_responses=True
)


def get_weather(city):

    cache_key = f"weather:{city}"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        print("Data dari Redis Cache")
        return json.loads(cached_data)

    print("Data dari API")

    time.sleep(2)

    weather_data = {
        "city": city,
        "temperature": 30,
        "condition": "Sunny"
    }

    redis_client.setex(
        cache_key,
        300,
        json.dumps(weather_data)
    )

    return weather_data