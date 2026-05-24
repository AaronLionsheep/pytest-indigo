import indigo  # pyright: ignore[reportMissingModuleSource]


class Plugin:
    def __init__(self):
        self.name = "plugin"
        indigo.data.set("running", False)

    def start(self):
        if indigo.data.get("running"):
            raise Exception("Plugin is already running!")

        indigo.data.set("running", True)

    def stop(self):
        if not indigo.data.get("running"):
            raise Exception("Plugin is not running!")

        indigo.data.set("running", False)
