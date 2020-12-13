import asyncio
import aiohttp
import json

async def request_data(url):
    # use aiohttp.request (as a context manager) to get data from url
    async with aiohttp.request('GET', url) as resp:
        request_text = await resp.text()
        return request_text
    # then return data as str

async def get_reddit_top(subreddit):
    # use request_data coroutine to get reddit top
    url_pattern = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'
    result = await request_data(url_pattern)
    response = json.loads(result)

    data_children = response.get("data", dict()).get("children", dict())
    data_title = list()
    data_url = list()
    data_score = list()
    for item in data_children:
        data_title.append(item.get("data", dict()).get("title"))
        data_url.append(item.get("data", dict()).get("url"))
        data_score.append(item.get("data", dict()).get("score"))

    data = {subreddit: {
        data_title[i]: {'Score': data_score[i], 'Link': data_url[i]} for i in range(0, len(data_children))}}
    print(data)
    return data

async def main():
    # use asyncio.gather to get tops for reddits "python", "compsci", "microbork"
    # try to use *args instead of hardcoded function calls
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    res = await asyncio.gather(*(get_reddit_top(reddit) for reddit in reddits))

asyncio.run(main())