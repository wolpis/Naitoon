import requests
from typing import Dict, Union
from bs4 import BeautifulSoup
import re
from naitoon.error import HTTPException, TitleIdException

class SyncNaitoonRequest:
  base_url = "https://comic.naver.com/webtoon/"
  headers = { 
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
    Safari/537.36'
  }
  
  def request(
    self,
    method : str,
    endpoint : str,
    params: Dict[str, Union[str, int]]
  ) -> str:
    url = self.base_url + endpoint
    response = requests.request(method, url, headers=self.headers, params=params)
    rescode = response.status_code
    if rescode == 200:
      return response.text
    else:
      raise HTTPException(f"Error Code {rescode}")

class Webtoon(SyncNaitoonRequest):
  """`SyncNaitoonRequest`를 감싸는 클라이언트 클래스입니다."""
  def get_list(self, weekday : str = 'today') -> Dict['str', 'str']:
    """요일 웹툰을 불러옵니다."""
    week = {
      "week" : weekday.lower()[:3] 
    }
    data = self.request("GET", "weekdayList", week)
    bs = BeautifulSoup(data, features="html5lib")
    list = []
    img_list = bs.find("ul", class_ = "img_list")
    img_list = img_list.find_all("li")
    for i in img_list:
      result = {}
      result['title'] = i.find("img")['title']
      author = i.find("dd", class_ = "desc").text.replace("\n", "").replace("\t", "")
      result['author'] = author
      result['star'] = i.find("strong").text
      result['thumbnail'] = i.find("img")['src']
      link = [link for link in i.find("dd", class_ = "more").children]
      result['id'] = re.sub(r'[^0-9]', '', str(link))
      result['link'] = "https://comic.naver.com" + link[0]['href']
      list.append(result)
    return list

  def get_info(self, id : int):
    """작품의 정보를 가져옵니다."""
    title_id = {
      "titleId" : id
    }
    data = self.request("GET", "list", title_id)
    bs = BeautifulSoup(data, features="html5lib")
    result = {}
    detail = bs.find('div', class_ = "detail")
    if detail == None:
      raise TitleIdException("작품을 찾을 수 없습니다.")
    result['title'] = detail.find("span", class_ = "title").text
    result['author'] = detail.find("span", class_ = "wrt_nm").text.replace("\n", "").replace("\t", "")
    result['genre'] = detail.find("span", class_ = "genre").text
    result['age'] = detail.find("span", class_ = "age").text
    result['description'] = detail.find("p").text
    thumb = bs.find("div", class_ = "thumb")
    result['thumbnail'] = thumb.find("img")['src']
    return result
