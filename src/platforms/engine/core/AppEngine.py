from src.domain.abstracts.AbstractNetworkUseCase import AbstractNeworkUseCase

class AppEngine:

    useCases: AbstractNeworkUseCase
    def __init__(self, networkUseCases: AbstractNeworkUseCase):
        self.useCases = networkUseCases

    def start(self):
        self.loopSearch()

    def loopSearch(self):
        response = self.useCases.getSearchUseCase().send()
        # if len response.cars == 0:

