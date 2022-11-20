class PlayerStats:

    def __init__(self, reader):
        self._players = reader
    
    def top_scorers_by_nationality(self, nat):
        players = filter(lambda x: x.nationality == nat, self._players)
        players = sorted(players, reverse=True, key=lambda player: player.points)
        return players