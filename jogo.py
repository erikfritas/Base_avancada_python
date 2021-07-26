import os
import keyboard as kb

cmd = "cls" if os.name == "nt" else "clear"


class Player:
    def __init__(self, head, body, foot, speed=1):
        self.head = head
        self.body = body
        self.foot = foot

        self.x = 10
        self.y = 10

        self.speed = speed

    def createRenderObj(self, x, y, obj):
        return "\n"*y + " "*x + obj
        
    def update(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def render(self):
        renderHead = self.createRenderObj(self.x+int(len(self.body)/2), self.y, self.head)
        renderBody = self.createRenderObj(self.x, 1, self.body)
        renderFoot = self.createRenderObj(self.x, 1, self.foot)

        renderPlayer = renderHead + renderBody + renderFoot
        
        return renderPlayer

    def onPress(self, btn):
        if kb.is_pressed(btn):
            return True
        else:
            return False

    def left(self):
        if self.x >= 0+self.speed:
            self.x -= self.speed

    def right(self):
        if self.x < 50-self.speed:
            self.x += self.speed

    def up(self):
        if self.y >= 0+self.speed:
            self.y -= self.speed

    def down(self):
        if self.y <= 30-self.speed:
            self.y += self.speed


class Game:
    def __init__(self):
        self.update()
        self.render()

    def update(self):
        # update
        if len(players) < qtPlayer:
            players.append(Player("O", "/|\\", "/ \\")) # para vc colocar \ vc tem que colocar duas vezes desse jeito \\

        if players[0].onPress('a'):
            players[0].left()
        elif players[0].onPress('d'):
            players[0].right()

        if players[0].onPress('w'):
            players[0].up()
        elif players[0].onPress('s'):
            players[0].down()

    def render(self):
        # render
        os.system(cmd)
        for p in players:
            print(p.render())


if __name__ == "__main__":
    players = []
    qtPlayer = 1
    
    while True:
        if kb.is_pressed('q'):
            break
        Game()
