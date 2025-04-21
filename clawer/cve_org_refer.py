import json

from clawer.base import BaseClawer
import requests
import os


def get_cve_path_by_cve_id(cve_id: str) -> str:
    """
    根据cve_id获取cve的路径
    :param cve_id:
    :return:
    """
    _, year, last_num = cve_id.split("-")
    dir_name = "{}xxx".format(last_num[:-3])
    return os.path.join(year, dir_name, "{}.json".format(cve_id.upper()))

class CveOrgRefer(BaseClawer):
    def __init__(self, base_dir):
        super().__init__(base_dir)
        self._name = "cve_org_refer"

    def run(self, cve_id: str):
        config_base = "/data/cvelistV5-main/cves"
        config_file = os.path.join(config_base, get_cve_path_by_cve_id(cve_id))
        with open(config_file, 'r', encoding='utf8') as f:
            data = json.load(f)

        for d in data["containers"]['cna']['descriptions']:
            print(d)



if __name__ == '__main__':
    CveOrgRefer("../data").run("CVE-2025-43929")