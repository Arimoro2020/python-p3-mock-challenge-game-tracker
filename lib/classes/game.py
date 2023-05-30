class Game:
    all = []
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        Game.all.append(self)

    def average_score(self, player):
        from classes.result import Result
        sum = 0
        score_list = [result.score for result in Result.all if (result.game == self and  result.player ==player)]
        all_results = [result for result in Result.all if (result.game == self and  result.player ==player)]
        for score in score_list:
            sum += score
        try:
            average = sum / len(all_results)
            return average
        except ValueError:
            raise ValueError ("denominator can not be zero")

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if type(value) == str and len(value) >0 and not hasattr(self, "title"):
            self._title = value
        else:
            raise Exception("value must be a string of 1 or more characters and cannot be changed if exists")

        
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return [result for result in Result.all if result.game ==self] 
    
    def players(self, new_player=None):
        from classes.result import Result
        from classes.player import Player
        if isinstance(new_player, Player):
             self._players.append(new_player)
        return [result.player for result in Result.all if result.game ==self] 

   