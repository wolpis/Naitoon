<div align="center">
  <h1>NaiToon(네이툰)</h1>
</div>

![image](https://user-images.githubusercontent.com/103942316/188868352-c5527df8-818e-41da-a8b5-cd208d104e42.png)
<div align="center">
  <h1>네이버 웹툰 크롤링 라이브러리</h1>
</div>

[<img src="https://img.shields.io/pypi/v/naitoon.svg">](https://pypi.python.org/pypi/naitoon)<br>
이슈, PR 모두 환영입니다!<br>
> **동기 비동기 모두 지원합니다!**<br>
> 현재 지원기능 : 작품리스트(요일별), ID검색 기능<br>
## Installation
```
$ pip install naitoon
```
## Example
### 리스트 불러오기(비동기)
```py
from naitoon import naver
import asyncio

naver = naver.Webtoon()
async def main():
  data = await naver.get_list() #요일웹툰 리스트를 가져옵니다. 파라미터가 비어있을시 오늘차 요일 리스트를 반환합니다.
  print(data)

asyncio.run(main())
```
### 리스트 불러오기(동기)
```py
from naitoon import sync

naver = sync.Webtoon()
data = naver.get_list() #요일웹툰 리스트를 가져옵니다. 파라미터가 비어있을시 오늘차 요일 리스트를 반환합니다.
print(data)
```
## Response sample
```
[
  {
    'title': '화산귀환', 
    'author': 'LICO / 비가', 
    'star': '9.91', 
    'thumbnail': 'https://shared-comic.pstatic.net/thumb/webtoon/769209/thumbnail/thumbnail_IMAG10_13ff2e28-686a-42de-890e-9289550978bc.jpg', 
    'id': '769209', 
    'link': 'https://comic.naver.com/webtoon/list?titleId=769209&weekday=wed'
  }
]
```
### ID로 작품 불러오기(비동기)
```py
from naitoon import naver
import asyncio

naver = naver.Webtoon()
async def main():
  data = await naver.get_info(758037) #작품의 정보를 가져옵니다. 작품을 찾지 못할 경우 TitleIdException 예외를 반환합니다.
  print(data)

asyncio.run(main())
```
### ID로 작품 불러오기(비동기)
```py
from naitoon import sync

naver = sync.Webtoon()
data = naver.get_info(758037) #요일웹툰 리스트를 가져옵니다. 파라미터가 비어있을시 오늘차 요일 리스트를 반환합니다.
print(data)
```
## Response sample
```
{
  'title': '참교육', 
  'author': '채용택 / 한가람', 
  'genre': '스토리, 액션', 
  'age': '15세 이용가', 
  'description': '무너진 교권을 지키기 위해 교권보호국 소속 나화진의 참교육이 시작된다!<부활남> 채용택 작가 X <신석기녀> 한가람 작가의 신작!', 
  'thumbnail': 'https://shared-comic.pstatic.net/thumb/webtoon/758037/thumbnail/thumbnail_IMAG06_794bcc1e-23aa-4c35-a335-b5d21b4bc2ab.jpg'
}
```
