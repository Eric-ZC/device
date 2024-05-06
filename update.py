import io
import subprocess
import tempfile
from zipfile import ZipFile

import requests
from rich.console import Console


def update():
    """
    更新资源
    """
    host = "192.168.190.169:5000"
    env = (
        subprocess.run(["poetry", "env", "info", "-p"], stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .strip()
    )

    console = Console()

    console.print(":smiley: 开始更新资源")
    with tempfile.TemporaryDirectory() as tp:
        filename = 'soium.tar.gz'
        filepath = f'{tp}/{filename}'
        r = requests.get(f"http://{host}/aut/update")
        with open(filepath, "wb") as file:
            file.write(r.content)
        process = subprocess.Popen(
            [f"{env}/Scripts/pip", "install", filepath, "--force-reinstall"],
            stdout=subprocess.PIPE,
        )
        process.communicate()
    r = requests.get(f"http://{host}/aut/get_resources")
    ZipFile(io.BytesIO(r.content)).extractall("resources")
    console.print(":smiley: 资源更新完成")


if __name__ == "__main__":
    update()
