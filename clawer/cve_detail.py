"""
cve_detail.py
cve_detail 网站爬虫
"""
from clawer.base import BaseClawer
import requests
import logging
log = logging.getLogger(__name__)

class CveDetail(BaseClawer):
    def __init__(self, base_dir):
        super().__init__(base_dir)
        self._name = "cve_detail"

    def run(self, cve_id: str):
        url = "https://www.cvedetails.com/cve/{}/".format(cve_id.upper())
        headers = {
            "accept": "plication/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "cache-control": "max-age=0",
            "priority": "u=0, i",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            self._save(cve_id, response.text)
        else:
            log_str = "{}:{}".format(cve_id, response.status_code)
            log.error(log_str)


if __name__ == '__main__':
    obj = CveDetail("../data")
    obj.run("CVE-2022-40664")
