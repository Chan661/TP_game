from cmu_graphics import *
from objectsTP3 import *
from helper_functions import *
from drawObject import *
import math

def onAppStart(app):
    app.paused = False
    app.width, app.height = 1200, 400
    
    app.player = Player('player', app.width, app.height)
    app.computer = Player('computer', app.width, app.height)
    app.ball = Ball(app)
    app.lastHit = app.player

    #UI
    app.controlPanelX, app.controlPanelY, app.controlPanelR = 970, 30, 10
    app.playing = True
    app.homePage = False
    app.explanationVisible = False
    app.startButton = Button('start', 'pink')
    app.exitExplanation = Button('got it', 'cyan')

    #UI-Menu
    app.menuVisible = False
    app.menuLeft, app.menuTop, app.menuWidth = 400, 100, 400
    app.menuButtons = [Button('Exit', 'orange'), Button('resume', 'limeGreen'), Button('Guidance and Rules', 'pink'), Button('one more!', 'yellow')]

def onKeyHold(app, keys):
    if 'a' in keys:
        app.player.cx -= 5
        app.player.tipX -= 5
        if app.ball.checkCollide(app.player): app.ball.dx -=5
    elif 'd' in keys:
        app.player.cx += 5
        app.player.tipX += 5
        if app.ball.checkCollide(app.player): app.ball.dx +=5
    if 'w' in keys:
        app.player.theta += 10
        app.player.tipX, app.player.tipY = getEndpoint(app.player.cx, app.player.cy, app.player.armLen, app.player.theta)
        # if app.ball.checkCollide(app.player):
        #     ax, ay = getDxDy(app.player)
        #     app.ball.dx += ax/10
        #     app.ball.dy += ay/10
    elif 's' in keys:
        app.player.theta -= 10
        app.player.tipX, app.player.tipY = getEndpoint(app.player.cx, app.player.cy, app.player.armLen, app.player.theta)

    if 250<=app.player.cy<=400:
        if '/' in keys:
            app.computer.cy += 3
            app.computer.tipY += 3
        elif '.' in keys:
            app.computer.cy -= 3
            app.computer.tipY -= 3

    if 'left' in keys:
        app.computer.cx -= 5
        app.computer.tipX -= 5
        if app.ball.checkCollide(app.player): app.ball.dx -=5

    elif 'right' in keys:
        app.computer.cx += 5
        app.computer.tipX += 5
        if app.ball.checkCollide(app.player): app.ball.dx -=5

    if 'up' in keys:
        app.computer.theta += 10
        app.computer.tipX, app.computer.tipY = getEndpoint(app.computer.cx, app.computer.cy, app.computer.armLen, app.computer.theta)
    elif 'down' in keys:
        app.computer.theta -= 10
        app.computer.tipX, app.computer.tipY = getEndpoint(app.computer.cx, app.computer.cy, app.computer.armLen, app.computer.theta)

    if 250<=app.computer.cy<=400:
        if 'e' in keys:
            app.player.cy += 3
            app.player.tipY += 3
        elif 'r' in keys:
            app.player.cy -= 3
            app.player.tipY -= 3

#UI control
def onMousePress(app, mouseX, mouseY):
    if distance(mouseX, mouseY, app.controlPanelX, app.controlPanelY)<= app.controlPanelR:
        app.menuVisible = True
        app.paused = True
    if distance(mouseX, mouseY, app.menuLeft+380, app.menuTop+15) <= 10:
        app.menuVisible = False
    if app.menuLeft+50<=mouseX<=app.menuLeft-50+app.menuWidth and app.menuVisible:
        for i in range(len(app.menuButtons)):
            if app.menuButtons[i].hit(mouseX, mouseY):
                if i==0:
                    app.playing = False
                    app.paused = True
                    app.menuVisible = False
                    app.homePage = True
                    restart(app)
                    app.player.score = app.computer.score = 0
                if i==1:
                    app.playing = True
                    app.paused = False
                    app.menuVisible = False
                    # restart(app)
                if i==2:
                    app.explanationVisible = True
                    app.menuVisible = False
                if i==3:
                    app.playing = True
                    app.paused = False
                    app.menuVisible = False
                    restart(app)

    if app.explanationVisible and app.exitExplanation.hit(mouseX, mouseY):
        app.explanationVisible = False
        app.menuVisible = True
    if not app.playing and app.startButton.hit(mouseX, mouseY):
        app.playing = True
        app.paused = False
        app.homePage = False
        # restart(app)
        # app.player.score = app.computer.score = 0

def takeStep(app):
    app.ball.airResistance()
    app.ball.projectile()
    if app.ball.checkCollide(app.player):
        app.ball.dx, app.ball.dy = app.ball.bounceSpeed(app.player)
        app.lastHit = app.player
    elif app.ball.checkCollide(app.computer):
        app.ball.dx, app.ball.dy = app.ball.bounceSpeed(app.computer)
        app.lastHit = app.computer
    #if app.lastHit == app.player: app.computer.moveComputer(app.ball.cx, app.ball.cy, app.ball.dx, app.ball.dy)
    if scoreBall(app, app.lastHit): app.paused = True

def onStep(app):
    if not app.paused:
        takeStep(app)

def restart(app):
    app.ball.cx, app.ball.cy = app.width/4, app.height/5
    app.ball.dx, app.ball.dy = -0, -10
    app.player.reposition()
    app.computer.reposition()

def redrawAll(app):
    drawNet(app)
    drawScoreBoard(app)
    drawControlIcon(app)

    drawPlayer(app.player)
    drawPlayer(app.computer)
    drawBall(app.ball)

    if app.menuVisible: drawMenu(app.menuLeft, app.menuTop, app.menuWidth, app.menuButtons)
    if app.homePage: homePage(app.width, app.height, app.startButton)
    if app.explanationVisible: explanation(app.width, app.height, app.exitExplanation)

runApp()