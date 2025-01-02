from cmu_graphics import *
import math
from helper_functions import *

class Ball:
    gravity = 0.7
    def __init__(self, app):
        self.cx, self.cy, self.r = app.width/4, app.height/4, 15
        self.dx, self.dy = 0, -10

    def airResistance(self):
        constant = 0.01
        theta = math.atan(self.dy/self.dx) if self.dx != 0 else math.pi/2
        v0 = (self.dx**2+self.dy**2)**0.5 
        drag_force = constant*(v0)**2
        self.dx += -drag_force * math.cos(theta) / 100
        self.dy += -drag_force * math.sin(theta) / 100
    
    def projectile(self):
        self.dy += Ball.gravity
        self.cx += self.dx
        self.cy += self.dy
        
    def checkCollide(self, player): #thanks Anna, the greatest TA of the summer
        a, b = player.cy - player.tipY, player.cx - player.tipX
        c = a * player.cx - b * player.cy
        
        potentialPoint = abs(a * self.cx - b * self.cy - c) / (a**2 + b**2)**0.5
        if potentialPoint <= self.r:
            if distance(player.tipX, player.tipY, self.cx, self.cy) <= self.r or distance(player.cx, player.cy, self.cx, self.cy) <= self.r: return True
            elif player.cx == player.tipX: ## self-added: vertical (since this makes math.sin(theta) = 0 and true no matter how far away the ball is
                return self.r+self.cy >= player.tipY and self.cx-self.r<=player.cx<=self.cx+self.r
            
            else:
                return acute(player.cx, player.cy, player.tipX, player.tipY, self.cx, self.cy, self.r) and acute(player.tipX, player.tipY, player.cx, player.cy, self.cx, self.cy, self.r)
        return False
        
    def bounceSpeed(self, player): # reflection vector vdo: https://www.youtube.com/watch?v=BCmFsYFln2k
        if self.cx == player.cx or player.cy == player.tipY: return self.dx, -self.dy
        if player.cx==player.tipX: return -self.dx, self.dy
        bdx, bdy = getDxDy(player)
        magnitude = (self.dx**2 +self.dy**2)**0.5
        return magnitude * bdx/2, magnitude * bdy

class Player:
    def __init__(self, identity, width, height):
        self.identity, score = identity, 0
        if self.identity=='player' :
            self.cx = width/4
            self.cy = height/4*3
            self.theta = 90
            self.armLen = 80
        else:
            self.cx = width*3/4
            self.cy = height/4*3
            self.theta = 90
            self.armLen = 80
        (self.tipX, self.tipY) = getEndpoint(self.cx, self.cy, self.armLen, self.theta)
        self.score = 0
        
    # def moveComputer(self, cx, cy, dx, dy): #trajectory point: https://www.omnicalculator.com/physics/trajectory-projectile-motion
    #     if self.identity == 'player': return
    #     x, y = getEndpoint(self.cx, self.cy, self.armLen-10, self.theta)
    #     if dx == 0:
    #         self.cx = cx - 20
    #         self.tipX = getEndpoint(self.cx, self.cy, self.armLen, self.theta)
    #         return
    #     targetX = intersectPoint(0.49/(2*dx**2), dy/dx, cy-y)
    #     if targetX != None: self.cx = targetX-20
    #     (self.tipX, self.tipY) = getEndpoint(self.cx, self.cy, self.armLen, self.theta)
    
    def reposition(self):
        self.cx, self.cy = (app.width/4*3, app.height/4*3) if self.identity == 'computer' else (app.width/4, app.height/4*3)
        #manage arm movement
        self.theta = 90
        self.TipX, self.TipY = getEndpoint(self.cx, self.cy, self.armLen, self.theta)
        # self.dTheta = 0

class Button:
    def __init__(self, function, colour):
        self.left = self.top = self.width = self.height = 0
        self.function, self.colour = function, colour
    
    def hit(self, mx, my):
        return self.left<=mx<=self.left + self.width and self.top<=my<=self.top + self.height