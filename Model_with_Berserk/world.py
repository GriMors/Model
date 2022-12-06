class World:

    def __init__(self, model):
        self.bodies = []
        self.model = model

    def add_body(self, b):
        self.bodies.append(b)

    def remove(self, b):
        self.bodies.remove(b)

    def act(self, dt):
        self.collisions()
        for b in self.bodies:
            if b.deleted:
                self.remove(b)
            b.move(dt)
            b.parent.view_body.pos = b.pos

    def collisions(self):
        for i in range(len(self.bodies)):
            b1 = self.bodies[i]
            for j in range(i+1, len(self.bodies)):
                b2 = self.bodies[j]
                if b1.intersect(b2) and not (b1 in b2.inter):
                    b1.add_inter(b2)
                    b2.add_inter(b1)
                    self.model.collision(b1.parent, b2.parent)