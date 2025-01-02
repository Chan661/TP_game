from cmu_graphics import *

def drawPlayer(player):
    drawCircle(player.cx, player.cy, 5, fill=None, border='black')
    drawLine(player.cx, player.cy, player.tipX, player.tipY)

    
def drawBall(ball):
    drawCircle(ball.cx, ball.cy, ball.r, fill='limeGreen')

def drawNet(app):
    drawPolygon(30, 250, 1200, 250, 1170, 400, 0, 400, fill='azure')
    drawLine(app.width/2-15, app.height-120-30, app.width/2-15, app.height, fill='orange')
    drawLine(app.width/2+15, app.height-270-30, app.width/2+15, app.height-150, fill='orange')
    drawLine(app.width/2-15, app.height-120-30, app.width/2+15, app.height-270-30, fill='orange')

def drawControlIcon(app): # definitely pause and return to home page (maybe music?)
    drawCircle(app.controlPanelX, app.controlPanelY, app.controlPanelR, fill='yellow', border='brown')
    drawRegularPolygon(app.controlPanelX, app.controlPanelY, app.controlPanelR-1, 3, fill='orange', rotateAngle=210)

def drawScoreBoard(app):
    drawRect(600, 30, 50, 50, fill='violet', border='purple')
    drawLabel('opponent Score', 650, 10, size=16, italic=True)
    drawLabel(f'{app.computer.score}', 625, 55, size=32)
    drawRect(550, 30, 50, 50, fill='violet', border='purple')
    drawLabel('my Score', 550, 10, size=16, italic=True)
    drawLabel(f'{app.player.score}', 575, 55, size=32)

def drawMenu(left, top, width, buttons):
    drawRect(left, top, width, 300, fill='white', border='brown')
    drawCircle(left+380, top+15, 10, fill='red')
    for i in range(len(buttons)):
        drawRect(left+50, top+15+i*60, width-100, 50, fill=buttons[i].colour)
        drawLabel(buttons[i].function, left+width/2, top+40+i*60, size=18)
        b=buttons[i]
        b.left, b.top, b.width, b.height = left+50, top+15+i*60, width-100, 50

def explanation(width, height, b):
    drawRect(70, 70, 650, 220, fill='pink', border='black')
    drawLabel("1. Click the menu icon on top right to pause, resume, and check this rule explanation", 400, 100, size=16) # continue later
    drawLabel("2. 'a w s d e r' and '. / [arrow kays]' are two groups of control pad", 400, 130, size=16)
    drawLabel("to change position and arm angle - try it!", 400, 160, size=16)
    drawLabel("3. Press the arrow signs to move right and left", 400, 190, size=16)
    drawLabel("4. Letting the ball drop on your side of the court earns a point for your opponent.", 400, 220, size=16)
    drawRect(600, 310, 100, 50, fill='cyan')
    drawLabel('Got it!', 650, 330, size=16)
    b.left, b.top, b.width, b.height = 600, 310, 100, 50

def homePage(width, height, b):
    drawLabel('Play this volleyball game!', width/2, 250, size=42)
    drawRect(width/2-100, 300, 200, 70, fill='pink')
    drawLabel('START', width/2, 335, size=36)
    b.left, b.top, b.width, b.height = width/2-100, 300, 200, 70