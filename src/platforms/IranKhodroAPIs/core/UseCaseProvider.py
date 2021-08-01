from src.domain.abstracts.AbstractNetworkUseCase import AbstractNeworkUseCase
import requests


class UseCaseProvider(AbstractNeworkUseCase):

    def getSearchUseCase(self):
        response = requests.get("https://esale.ikco.ir/api/services/OnlineSales/priceList/spGetLotteryWinnerByOrderID?id=6969696969696")
        print(response)
