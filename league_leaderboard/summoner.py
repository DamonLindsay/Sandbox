class Summoner:
    def __init__(self, name, data):
        self.name = name
        self.id = data.get('id')
        self.account_id = data.get('accountId')
        self.puuid = data.get('puuid')
        self.profile_icon_id = data.get('profileIconId')
        self.revision_date = data.get('revisionDate')
        self.summoner_level = data.get('summonerLevel')
