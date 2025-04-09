class L(list):
    def p(self, *args):
        if not args:
            return
        if not self:
            self.extend([[arg] for arg in args[0]])
            return
        c = [[i] for i in self]
        for lst in args:
            n = []
            for cn in c:
                for item in lst:
                    n.append(cn + [item])
            c = n
        self.clear()
        self.extend(c)
    def c(self):
        for i in range(len(self)):
            while any(isinstance(item, list) for item in self[i]):
                self[i] = sum(([item] if not isinstance(item, list) else item for item in self[i]), [])