import asyncio
import aiohttp
import time

async def fetch(url, session):
    start_time = time.time()
    async with session.get(url) as response:
        end_time = time.time()
        return await response.text(), end_time - start_time

async def main():
    urls = ['http://load_balancer' for _ in range(10)]  # Adjust the number of requests as needed

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        responses = await asyncio.gather(*tasks)

        for response, round_trip_time in responses:
            print("Response:", response)
            print("Round Trip Time:", round_trip_time)

if __name__ == "__main__":
    asyncio.run(main())
