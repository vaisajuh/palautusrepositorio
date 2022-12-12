from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or

class QueryBuilder:

    def __init__(self, matcher = None):
        self.query_object = matcher or All()
    
    def plays_in(self, team):
        return QueryBuilder(And(self.query_object, PlaysIn(team)))
    
    def has_at_least(self, value, str):
        return QueryBuilder(And(self.query_object, HasAtLeast(value, str)))
    
    def has_fewer_than(self, value, str):
        return QueryBuilder(And(self.query_object, HasFewerThan(value, str)))
    
    def one_of(self, *matchers):
        return QueryBuilder(And(self.query_object, Or(*matchers)))

    def build(self):
        return self.query_object
