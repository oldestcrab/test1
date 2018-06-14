# -*- coding:utf-8 -*-

import requests

url = 'http://news.sciencenet.cn/news/news/fieldlist.aspx?id=3'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'referer':'http://news.sciencenet.cn/news/fieldlist.aspx?id=3'
}
formdata = {
    '__VIEWSTATE':'%2FwEPDwUJNDE3NTc0Njg0D2QWAgIED2QWBGYPPCsACwEADxYKHgxEYXRhS2V5RmllbGQFAmlkHghEYXRhS2V5cxYeAtCQGQLIkBkCzpAZAtKQGQLMkBkCy5AZAr6QGQKykBkCqZAZAqaQGQKkkBkCnJAZApOQGQKPkBkC9o8ZAoCQGQL5jxkC%2BI8ZAvSPGQKdjxkCsI8ZAsOPGQK6jxkCk48ZAo6PGQKKjxkCgo8ZAvaOGQLljhkC4I4ZHgtfIUl0ZW1Db3VudAIeHglQYWdlQ291bnQCAR4VXyFEYXRhU291cmNlSXRlbUNvdW50Ah5kFgJmD2QWPAIBD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTcyOC5zaHRtJOenkeaKgOmpseWKqOiUrOiPnOWTgeenjeaNouS7o%2BWNh%2Be6pwnog6HnkoflrZAQMjAxOC81LzkgOTozMjoyN2QCAg9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE3MjAuc2h0bSwxNeS6v%2BWKqeaOqOWPtuWOv%2BWunueOsOmlsuiNieeVnOeJp%2BS4gOS9k%2BWMlgnlj7Lkv4rluq0QMjAxOC81LzkgOTozMjoyN2QCAw9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE3MjYuc2h0bS3liJvmhI%2FkuLrkuaHmnZHml4XmuLjmj5LkuIrigJzpmpDlvaLnv4XohoDigJ0KIOiDoeeSh%2BWtkBAyMDE4LzUvOSA5OjMwOjA3ZAIED2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTczMC5zaHRtIeeUqOe6s%2Bexs%2BaKgOacr%2BaUuemAoOS8oOe7n%2BWGnOS4mgnnp6blv5fkvJ8QMjAxOC81LzkgOToyOTowN2QCBQ9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE3MjQuc2h0bSfnn6Xor4bpnZLlubTlj4jliLDigJzkuIrlsbHkuIvkuaHigJ3ml7YJ5YiY5rC45aW9EDIwMTgvNS85IDk6MjY6NTNkAgYPZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNzIzLnNodG01MzbkuKrlpKfln47luILlhbHlkIzlj5HluIPjgIrotKjph4%2FlhbTlhpzlgKHorq7kuabjgIsJ56em5b%2BX5LyfEDIwMTgvNS85IDk6MjY6NTNkAgcPZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNzEwLnNodG0q5Z%2B65Zug57uE57yW5YaZ6aG555uu556E5YeG6LaF5a6J5YWo57uG6IOeBuWul%2BWNjhAyMDE4LzUvOSA5OjIwOjMyZAIID2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTY5OC5zaHRtNuS4reenkemZouWNjuWNl%2BakjeeJqeWbreaPkOWHuuakjeeJqemAguW6lOaAp%2BaWsOWBh%2BivtBHmnLHmsYnmlowgIOWRqOmjnhAyMDE4LzUvOSA5OjA2OjE5ZAIJD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTY4OS5zaHRtJ%2BenkeWtpuWutuegtOino%2BS4gOenjeakjeeJqeWvhOeUn%2BacuuWItgbmmYvmpaAQMjAxOC81LzkgODo0MTo1NmQCCg9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE2ODYuc2h0bS3noJTnqbblj5HnjrBETkHkv67lpI3og73lipvkuI7nlJ%2Fnianpkp%2FmnInlhbMG5ZGo6IifEDIwMTgvNS85IDg6MzU6MjJkAgsPZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNjg0LnNodG0z5oiR5Zu95LiJ54af5Yi25pep54af5rK56I%2Bc5paw5ZOB56eN6YCJ6IKy6I6356qB56C0EOmygeS8nyDlvKDlrabmmIYRMjAxOC81LzggMjI6NDE6MzNkAgwPZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNjc2LnNodG0w5paw56CU56m25Y%2Bv5o%2BQ5L6b5qOJ6Iqx5a6a5ZCR6IKy56eN5Z%2B65Zug6LWE5rqQCei1teW5v%2BerixEyMDE4LzUvOCAxOTowMjo0NmQCDQ9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE2Njcuc2h0bTPmlrDmioDmnK%2Fov73ouKrljZXkuKrnu4bog57lpoLkvZXkuqfnlJ%2FlrozmlbTouqvkvZMG5a6X5Y2OETIwMTgvNS84IDE2OjA0OjU3ZAIOD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTY2My5zaHRtMOS%2FneaKpOWFuOWei%2BaegeWwj%2Benjee%2BpOmHjueUn%2BakjeeJqeatpeS8kOWKoOW%2Fqwbpk4Hpk64RMjAxOC81LzggMTU6Mzk6MTdkAg8PZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNjM4LnNodG0q5Yac56eR6Zmi5o6o5Ye66JSs6I%2Bc57u%2F6Imy55Sf5Lqn5paw5qih5byPCeiSi%2BW7uuenkREyMDE4LzUvOCAxMzowNzowNGQCEA9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE2NDguc2h0bS3noJTnqbblj5HnjrBETkHkv67lpI3og73lipvkuI7nlJ%2Fnianpkp%2FmnInlhbMG5ZGo6IifETIwMTgvNS84IDExOjQwOjI0ZAIRD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTY0MS5zaHRtNOmVv%2Bacn%2Biiq%2Bivr%2BinoyDpnZ7nvJbnoIFSTkHlrZjlnKjigJzorqTnn6Xpu5HmtJ7igJ0J5byg5L2z5pifETIwMTgvNS84IDEwOjEwOjUxZAISD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTY0MC5zaHRtJ%2Ba%2FkuWNseakjeeJqeS8r%2BS5kOagkeW5vOiLl%2BWfueiCsuaIkOWKnwnotbXmsYnmlowRMjAxOC81LzggMTA6MDg6MTRkAhMPZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNjM2LnNodG0n6J2Z6J2g6YG%2F5YWN5Zue5aOw5bmy5omw6Z2g5pS55Y%2BY6aKR546HCeW8oOaipueEthEyMDE4LzUvOCAxMDowNToxN2QCFA9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE1NDkuc2h0bRLpuJ%2Fov4HlvpnkuLroioLog70G5pmL5qWgEDIwMTgvNS84IDg6NTg6MDFkAhUPZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNTY4LnNodG0%2F5rKz5YyX5L2%2F55So5qSN5L%2Bd5peg5Lq65py65a%2B55bCP6bqm6L%2Bb6KGM5aSn6KeE5qih5Za36I2v5L2c5LiaCeacseaXreS4nBAyMDE4LzUvOCA4OjUwOjQwZAIWD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTU4Ny5zaHRtJ%2BmZiOm5j%2B%2B8muWFqOaDheaKleWFpeaVmeaUuei0o%2BaXoOaXgei0txHku5jmloflqbcgIOa4qeaJjRAyMDE4LzUvOCA4OjQxOjE5ZAIXD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTU3OC5zaHRtOeS6uuexu%2BiDmuiDjuW5sue7huiDnumHjeWhkeeUn%2BeJqeWtpuamguW%2FteW5tui%2Fm%2BWFpeS4tOW6igblrpfljY4QMjAxOC81LzggODo0MToxOWQCGA9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE1Mzkuc2h0bTPmlrDnoJTnqbbmj63lvIDnu4boj4zog73igJzlkIPigJ3pnZLpnInntKDnmoTnp5jlr4YAETIwMTgvNS83IDIwOjIyOjIyZAIZD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTUzNC5zaHRtQuW3peeoi%2BmZoumZouWjq%2BadjueOie%2B8muS8mOiJr%2BWTgeenjeeahOiCsuaIkOWPr%2BiDveaYr%2BihjOS4mumdqeWRvQARMjAxOC81LzcgMTg6MjY6MTdkAhoPZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNTMwLnNodG0z5oSP5aSn5Yip56eR5a2m5a625Y%2BR546w55mM57uG6IOe5omp5pWj6amx5Yqo5Z%2B65ZugBuWNmua6kBEyMDE4LzUvNyAxNzoyMToyNmQCGw9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE1MjIuc2h0bT%2Fku4rlubTnrKzlhavmibnkurrnsbvpgZfkvKDotYTmupDooYzmlL%2Forrjlj6%2Fpobnnm67kv6Hmga%2FmsYfmgLsAETIwMTgvNS83IDE1OjU4OjQ1ZAIcD2QWAmYPZBYCZg8VBBwvaHRtbG5ld3MvMjAxOC81LzQxMTUxMC5zaHRtM%2BWbveWutueJpueJm%2BS6p%2BS4muenkeaKgOWIm%2BaWsOiBlOebn%2BWcqOWFsOW3nuaIkOeriwnliJjmmZPlgKkRMjAxOC81LzcgMTM6NDg6MTBkAh0PZBYCZg9kFgJmDxUEHC9odG1sbmV3cy8yMDE4LzUvNDExNDkzLnNodG0h55So6KGM5Li656eR5a2m5omT6YCg6L%2BQ5Yqo5Lmg5oOvCeWGr%2Be7tOe7tBEyMDE4LzUvNyAxMTowNDo1MmQCHg9kFgJmD2QWAmYPFQQcL2h0bWxuZXdzLzIwMTgvNS80MTE0ODguc2h0bTzkuK3lm73mioDmnK%2FigJzotbDopb%2Flj6PigJ3pmLLmsrvloZTlkInlhYvmlq%2FlnablhpzmnpflrrPomasJ5a2Z5Lqt5paHETIwMTgvNS83IDEwOjUxOjU1ZAIBDw8WBh4LUmVjb3JkY291bnQC%2BI4BHg5DdXN0b21JbmZvVGV4dAVj6K6w5b2V5oC75pWw77yaPGI%2BMTgyOTY8L2I%2BIOaAu%2BmhteaVsO%2B8mjxiPjYxMDwvYj4g5b2T5YmN5Li656ysPGZvbnQgY29sb3I9InJlZCI%2BPGI%2BOTwvYj48L2ZvbnQ%2B6aG1HhBDdXJyZW50UGFnZUluZGV4AglkZGRIFk8GOkdSw1VbUi94ZbC3XArjnw%3D%3D',
    '__EVENTTARGET':'AspNetPager1',
    '__EVENTARGUMENT':'5',
    'AspNetPager1_input':'9'
}

response = requests.post(url, data = formdata, headers = headers)

print(response.text)
with open('./result.html', 'a', encoding = 'utf-8') as f:
    f.write(response.text)