# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/
# 🌍 GIT URL: https://github.com/eliheuer/type-thursday-talk-2019
# ✅ Runebender

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN, [G] GRID UNIT
W, H, M, G = 1344, 768, 128, 32

# Set variation 
fontVariations(wght=700)

# EDGE #########################################################################
def edge():
    #960, 704
    stroke(0.3)
    strokeWidth(1)
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# GRID #########################################################################
def grid(X, Y):
    stroke(0.3)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = G, G
    for x in range(X):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(Y):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY


# BASIC_PAGE ##################################################################
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)
    # LOAD BASIC FONT
    # Fonts
    font("fonts/Inter-upright.var.ttf")
    # Set axis from font
    for axis, data in listFontVariations().items():
        print((axis, data))
    #font("fonts/Blob-Black.ttf")  # Set the font
    #font("fonts/a.ttf")  # Set the font
    # Set variation 
    fontVariations(wght=500)

# #############################################################################
new_page()
grid(34, 16) # Toggle for grid view
edge()       # Toggle for safe area

fill(0)
rect(M+(G*0), M+(G*13), (G*21), (G*3))
rect(M+(G*0), M+(G*11), (G*24), (G*1))

fill(1)
stroke(None)

fontSize(120)
fontVariations(wght=700)
tracking(-5)
text("Runebender", M-4, M+4+(G*13))

fontSize(36)
fontVariations(wght=500)
tracking(-1)
text("A new open-source, cross-platform font editor.", M+2, M+3+(G*11))

# #############################################################################
new_page()
grid(35, 16) # Toggle for grid view
edge() # Toggle for safe area

fill(1)
stroke(None)
fontSize(M)
e = 8
text("ELI HEUEr",    (M)+e, (M*10)+e)
text("FONT ENGINEEr", (M)+e, (M*9)+e)
#text("ELIHEUEr",   (M)+e, (M*6)+e)

step = 100
fontSize(M*8)
stroke(0)
#for i in range(20):
#    fontVariations(wght=step)
#    text("I", (M-100)+(step*3), (M*4)+(4)-(step/2))
#    step +=20
    #if i == 3:
        #image("images/cli-01.png", (400, 200), alpha=1)
    #else:
    #    pass


new_page()
grid(35, 16) # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/thaw.jpg", (400, 200), alpha=1)


new_page()
grid(35, 16) # Toggle for grid view
edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/multi-bg-sm.jpg", (M+100, 0), alpha=1)


new_page()
#grid() # Toggle for grid view
#edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/TruFont.png", (0, 0), alpha=1)

new_page()
#grid() # Toggle for grid view
#edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
image("images/emacs-02.png", (0, 0), alpha=1)


new_page()
#grid() # Toggle for grid view
#edge() # Toggle for safe area
fill(1)
stroke(None)
fontSize(M)
text("LIBRE GRAPHICS MEETING",    (M)+e, (M*10)+e)
image("images/saar_big-sm.jpg", (300, 100), alpha=1)





saveImage("slides.pdf")

