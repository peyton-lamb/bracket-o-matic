class Pool:
    def __init__ (self, teams):
        self.__teams = teams
        self.__games = {}
        self.__contestants = {}

    def addContestant(self, name, picks):
        self.__contestants[name] = {'picks':picks, 'score':0}

    def addResult(self, bracket_pos, winner):
        teams[bracket_pos] = winner

    