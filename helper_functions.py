from cmu_graphics import *
import math

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def getEndpoint(cx, cy, r, theta):
    return (cx + r*math.cos(math.radians(theta)),
            cy - r*math.sin(math.radians(theta)))
            
def acute(x1, y1,x2, y2, cx, cy, r):
    vaX, vaY = cx-x1, y1-cy
    vbX, vbY = x2-x1, y1-y2
    
    # theta = abs(math.atan((vaX * vbY - vaY - vbX)/(vaX * vbX + vaY * vbY)))
    theta = abs(math.atan2((vaX * vbY - vaY - vbX), (vaX * vbX + vaY * vbY)))
    return theta < math.pi/2
    
def getDxDy(player):
    dx, dy = (player.tipX-player.cx)/((player.tipX-player.cx)**2)**0.5, (player.tipY-player.cy)/((player.tipY-player.cy)**2)**0.5
    return (-dy, dx) if player.tipX<player.cx else (dy, -dx)

def intersectPoint(a, b, c):
    delta = b*2 - 4*a*c
    if delta >= 0:
        sol1, sol2 = (-b-(delta)**0.5)/(2*a), (-b+(delta)**0.5)/(2*a)
        return sol2
    return None

def scoreBall(app, lastHit):
    if app.ball.cy>350 or ((app.ball.cx>1200 or app.ball.cx<0)):
        if lastHit.identity == 'computer':
            app.computer.score += int(app.ball.cx < 600 and app.ball.cy>350)
            app.player.score += int((app.ball.cx > 600 and app.ball.cy>350) or (app.ball.cx>1200 or app.ball.cx<0))
        elif lastHit.identity == 'player':
            app.player.score += int(app.ball.cx > 600 and app.ball.cy>350)
            app.computer.score += int((app.ball.cx<600 and app.ball.cy>350) or (app.ball.cx>1200 or app.ball.cx<0))
    return app.ball.cy>350 or ((app.ball.cx>1200 or app.ball.cx<0))