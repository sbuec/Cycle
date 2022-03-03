
class Cast:
    def __init__():
        pass



class CastRFK:

    def __init__(self):
        self._actors = {}
       

    # Add actor to specific group
    def add_actor(self, group, actor):
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)


    # Gets actors from specific group
    def get_actors(self, group):
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    

    # Gets all actors in the cast
    def get_all_actors(self):
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results


    # Gets first actor in specific group
    def get_first_actor(self, group):
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result


    #Remove actor from specific group
    def remove_actor(self, group, actor):
        if group in self._actors:
            self._actors[group].remove(actor)