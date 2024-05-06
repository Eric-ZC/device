import shutil
from pathlib import Path

import pytest
from adbutils import AdbClient

# 抓取日志
# adb shell am start -n com.debug.loggerui/.MainActivity
# adb pull data/debuglogger

# device = ("NMS212NG3349F0018", "D4-504 Pro")
# device = ('NMS212NG3ENGF0064', "Swift 2 Pro")
# device = ('NMS212NG3349F0018',"D4-504 Pro")
# device = ('NDS111PH3342F0074',"D4-504 Pro")
# device = ('NMS115NG1406F0035',"Swift 1 Pro")
# device = ('NMS115NG1406F0040',"Swift 1 Pro")
# device = ('ND4504PH2341F0008',"D4-504 Pro")
# device = ('ND4505PH2341F0001',"D4")
# device = ("NMS212NG3349F0088","Swift 2 Pro")
# device = ('NMS115NG1406F0007',"Swift 1 Pro")
# device = ("ND2402XE2343C0019","D2-402")
# device = ("NMS115NG3406F0052", "swift 1 pro")
# device = ("NMS115NG1406F0050","swift 1 pro")
# device = ("NDS111PH3342F0006","swan 1 pro")
# device = ("ND4505PH2348F0003","D4")
# device = ("NMS211NE3405E0002","Swift 2 Pro")
# device = ("NMS212NG3349F0081","swift 2 pro")
# device = ("ND4504CG2348C0006", "D4_504_Pro")
# device = ("NMS115NG1406F0050", "swift1")
device = ("NDS111XG2329C0005", "swift1")


if __name__ == "__main__":
    sn, model = device
    host = "127.0.0.1"
    port = 5037
    adb = AdbClient(host, port).device(sn)

    for pkg in adb.list_packages():
        if "uiautomator" in pkg:
            adb.uninstall(pkg)

    report_path = Path("reports")
    if report_path.exists():
        shutil.rmtree(report_path)
    pytest.main(
        [
            "-k",
            "test_iterator",
            f"--host={host}",
            "--port=4723",
            f"--udid={sn}",
            f"--model={model}",
            f"--html={report_path.joinpath('report.html')}",
            "--loop=1",
            # "-x",
            "-m",
            "android11"
        ]
    )
