import os
import time


class BaseClawer(object):
    def __init__(self, base_dir):
        self._base_dir = base_dir
        self._name = "baseClawer"

    def _get_time_str(self):
        return time.strftime("%Y%m%d", time.localtime())

    def _save(self, cve_id: str, data):
        if not os.path.isdir(self._base_dir):
            os.makedirs(self._base_dir)

        cve_dir = os.path.join(self._base_dir, cve_id)
        if not os.path.isdir(cve_dir):
            os.makedirs(cve_dir)
        file_path = self.gen_data_file(cve_dir)
        with open(file_path, 'w') as f:
            f.write(data)
        pass

    def gen_data_file(self, cve_dir: str) -> str:
        data_file = "{}_{}.txt".format(self._name, self._get_time_str())
        file_path = os.path.join(cve_dir, data_file)
        if not os.path.isfile(file_path):
            return file_path
        index = 1
        while True:
            data_file = "{}_{}_{}.txt".format(self._name, self._get_time_str(), index)
            file_path = os.path.join(cve_dir, data_file)
            if not os.path.isfile(file_path):
                return file_path
            path = os.path.join(cve_dir, data_file)

    def run(self, cve_id):
        """
        下载cve_id的情报并保存
        :return:
        """
        self._save(cve_id, "test")


if __name__ == '__main__':
    obj = BaseClawer("../data")
    obj.run("CVE-2023-2564")
