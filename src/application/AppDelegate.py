from src.platforms.engine.core.AppEngine import AppEngine
from src.platforms.IranKhodroAPIs.core.UseCaseProvider import UseCaseProvider


class AppDelegate:

    @classmethod
    def launch(cls):
        ikcoNetwork = UseCaseProvider()
        engine = AppEngine(ikcoNetwork)
        engine.start()
        print("hello world!!!!")

