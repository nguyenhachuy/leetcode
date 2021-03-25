class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #why waste time if there are no paths...
        if not paths:
            return []

        dict_ = defaultdict(list)

        for path in paths:
            #split each path to its files
            splited_paths = path.split()

            for p in splited_paths[1:]:
                #add to dict for each text its path
                dict_[p[p.find('(') + 1 : -1]].append('/'.join([splited_paths[0] , p[:p.find("(")]]))

         #return list of lists of paths with duplicate content
        return [x for x in dict_.values() if len(x) > 1]

