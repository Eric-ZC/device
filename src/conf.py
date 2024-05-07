from pathlib import Path, PurePosixPath


class Configs:
    max_count = 5

    month_title = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
    }

    class wifi:
        free = "CTS-2.4", ""
        admin = "Neostra-admin", "ad@666999"
        gm = "Neostra-GM", "neo@888888"

    class packages:

        launcher = "com.android.launcher3", ".uioverrides.QuickstepLauncher"
        settings = "com.android.settings", ".Settings"
        wifi_settings = "com.android.settings", ".Settings$WifiSettings2Activity"

        diagnosis_oir ="com.neostra.hardwarehousekeeper","com.neostra.hardwarehousekeeper.ui.activity.HomeActivity"
        diagnosis = "com.neostra.test.basic", "com.neostra.test.basic.MainActivity"
        file_manager = "com.android.documentsui", ".files.FilesActivity"
        chrome = "com.android.chrome", "com.google.android.apps.chrome.Main"
        camera = "com.mediatek.camera", "com.mediatek.camera.CameraLauncher"
        store = "com.imin.appstore", "com.zzf.store.LaunchActivity"
        calculator = "com.android.calculator2", ".Calculator"
        gallery = "com.android.gallery3d", ".app.GalleryActivity"
        music = "com.android.music", ".MusicBrowserActivity"
        google_store = "com.android.vending", "com.android.vending.AssetBrowserActivity"

    class path:
        """
        文件夹
        """

        storage = PurePosixPath("/storage/emulated/0")
        resources = Path("resources")
        music = storage.joinpath("Music")
        documents = storage.joinpath("Documents")
        download = storage.joinpath("Download")
        movies = storage.joinpath("Movies")
        pictures = storage.joinpath("Pictures")
        camera = storage.joinpath("DCIM").joinpath("Camera")


settings = Configs()
