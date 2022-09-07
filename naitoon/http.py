import aiohttp
from typing import Dict, Union
from naitoon.error import HTTPException

class NaitoonRequest:
  base_url = "https://comic.naver.com/webtoon/"
  headers = { 
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
    Safari/537.36'
  }
  
  async def request(
    self,
    method : str,
    endpoint : str,
    params: Dict[str, Union[str, int]]
  ) -> str:
    url = self.base_url + endpoint
    async with aiohttp.ClientSession(headers=self.headers) as session:
      async with session.request(method, url=url, params=params) as response:
        rescode = response.status
        if rescode == 200:
          return await response.text()
        else:
          raise HTTPException(f"Error Code {rescode}")
