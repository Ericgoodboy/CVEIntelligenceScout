import requests
import tqdm

from clawer.base import BaseClawer
import urllib.parse
import time
import logging

log = logging.getLogger(__name__)


def crawl_csdn_top5(keyword):
    # 构造搜索URL
    encoded_keyword = urllib.parse.quote(keyword)
    url = (f"https://so.csdn.net/api/v3/search?q={encoded_keyword}&t=all&p="
           f"1&s=0&tm=0&lv=-1&ft=0&l=&u=&ct=-1&pnt=-1"
           f"&ry=-1&ss=-1&dct=-1&vco=-1&cc=-1&sc=-1&akt=-1&art=-"
           f"1&ca=-1&prs=&pre=&ecc=-1&ebc=-1&urw=&ia=1&dId=&cl=-1&scl=-"
           f"1&tcl=-1&platform=pc&ab_test_code_overlap=&ab_test_random_code=")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()

        ret = response.json()
        articles = ret['result_vos']
        return articles[:10]  # 确保返回不超过5条结果

    except requests.RequestException as e:
        print(f"请求失败: {str(e)}")
        return []
    except Exception as e:
        print(f"解析失败: {str(e)}")
        return []


class CsdnTop5(BaseClawer):
    def __init__(self, base_dir):
        super().__init__(base_dir)
        self._name = "csdn_top5"

    def run(self, cve_id: str):
        results = crawl_csdn_top5(cve_id)
        for item in tqdm.tqdm(results):
            time.sleep(1)
            try:
                ret = requests.get(item['url'], headers={
                    "content-type": "text/html; charset=UTF-8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/91.0.4472.124 Safari/537.36"
                }, timeout=3)
                if ret.status_code == 200:
                    self._save(cve_id, ret.text)
                else:
                    pass
            except requests.Timeout:
                print('请求超时')
            except Exception as e:
                log.error(f"请求失败: {str(e)}")


# 示例用法
if __name__ == "__main__":
    keyword = "CVE-2022-34858"
    CsdnTop5("../data").run(keyword)
