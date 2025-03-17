class L(list):
    def p(self, *args):
        if not args:
            return
        if not self:
            self.extend(args)
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
        while len(self) > 1:
            item = self.pop(1)
            if isinstance(item, list):
                self[0].extend(item)
            else:
                self[0].append(item)
        i = 0
        while i < len(self[0]):
            while isinstance(self[0][i], list):
                self[0][i:i+1] = self[0][i]
            i += 1
        while isinstance(self[0], list):
            self[:] = self[0]