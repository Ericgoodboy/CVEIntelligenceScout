import time
import tqdm
from clawer import cve_detail, csdn_top5


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    clawer_list = [cve_detail.CveDetail("./data"), csdn_top5.CsdnTop5("./data")]
    cve_id_list = """
CVE-2022-40664
CVE-2021-24404
CVE-2021-24285
CVE-2023-2982
CVE-2021-24506
CVE-2022-34858
CVE-2015-7297
CVE-2024-1061
CVE-2017-17731
CVE-2013-5743
CVE-2024-43044
CVE-2015-8369
CVE-2023-23489
CVE-2023-23490
CVE-2021-24361
CVE-2020-14092
CVE-2024-1698
CVE-2022-26138
CVE-2021-24353
CVE-2021-24626
CVE-2021-24337
CVE-2022-2840
CVE-2021-24442
CVE-2023-1730
CVE-2016-10057
CVE-2022-0693
CVE-2021-29441
CVE-2020-11989
CVE-2022-36537
CVE-2023-3077
CVE-2020-13640
CVE-2016-3659
CVE-2023-23488
CVE-2023-6875
CVE-2021-24142
CVE-2015-8604
CVE-2010-0738
CVE-2023-35828
CVE-2015-4634
CVE-2021-27905
CVE-2024-4434
CVE-2020-1938
CVE-2018-16385
CVE-2023-7028
CVE-2014-1854
CVE-2023-1454
    """
    for cve_id in tqdm.tqdm(cve_id_list.split("\n")):
        if cve_id.strip():
            time.sleep(1)
            for clawer in clawer_list:
                clawer.run(cve_id)
