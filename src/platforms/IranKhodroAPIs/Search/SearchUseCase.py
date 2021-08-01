import requests

class SearchUseCase:

    def send(self):
        response = requests.get("https://esale.ikco.ir/#!/lotteryWinnerList")
        print(response.json())
