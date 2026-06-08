import time

from lms.weather_cache.weather_api import get_weather


start = time.time()

result1 = get_weather("Jakarta")

time1 = time.time() - start

print(result1)

print(f"First call: {time1:.2f}s")


start = time.time()

result2 = get_weather("Jakarta")

time2 = time.time() - start

print(result2)

print(f"Second call (cached): {time2:.2f}s")