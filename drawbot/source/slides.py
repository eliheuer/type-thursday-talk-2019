# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/
# 🌍 GIT URL: https://github.com/eliheuer/type-thursday-talk-2019
# ✅ Runebender

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN, [G] GRID UNIT
W, H, M, G = 1344.0, 768.0, 128.0, 32.0
grid_color = 0.3

# EDGE #########################################################################
def edge(C):
    #960, 704
    stroke(C)
    strokeWidth(1)
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# GRID #########################################################################
def grid(X, Y, C):
    stroke(C)
    strokeWidth(1.0)
    stpX, stpY = 0, 0
    incX, incY = G, G
    for x in range(X):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(Y):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY

# BASIC_PAGE ##################################################################
def new_page(F):
    newPage(W, H)
    fill(F)
    rect(-2, -2, W+2, H+2)

# Runebender #####################################################################
new_page(0)
grid(34, 16, grid_color) # Toggle for grid view
edge(grid_color)       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0), M+(G*13), (G*21), (G*3))
rect(M+(G*31), M+(G*13), (G*3),  (G*3))
rect(M+(G*0), M+(G*11), (G*21), (G*1))
rect(M+(G*0), M+(G*6),  (G*10), (G*4))
rect(M+(G*0), M+(G*1),  (G*7),  (G*4))
rect(M+(G*0), M+(G*0),  (G*19), (G*1))

# Line
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(10):
    fill(red, green, blue)
    rect(M+(G*32), M+(0)+(G*i), (G), (G))
    green += 0.1
stroke(grid_color)

# Text Headline
font("fonts/Splinter-Bold.ttf")
fontSize(120)
tracking(-5.0)
stroke(None)
fill(1)
text("Runebender", M-4+(G*0), M+4+(G*13))

fill(0)
stroke(grid_color)
text("1", M-11+(G*32), M+4+(G*13))
fill(1)
stroke(None)

# Bitmaps
#image("images/nmaps.png", (M+(G*26), M+(G*13)), alpha=1)
#image("images/blob_a.png", (749, 69), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontVariations(wght=400)
fontSize(30)
tracking(-0.1)
text("A New Open-Source Font Editor Written in Rust", M+3, M-2+(G*11))
tracking(None)
fill(0.9, 0.9, 0.3)
text("07.11.19", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Eli Heuer", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("@eliheuer", M+2, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("https://elih.blog", M+2, M-2+(G*6))
fill(0.9, 0.5, 0.3)
fill(0.9, 0, 0.3)
text("https://github.com/linebender/runebender", M+2, M-2+(G*0))

# MB42 Type
font("fonts/Isotherma-Alpha.ttf")
fill(0)
stroke(grid_color)
fontSize(120)
text("Runebender", M+3+(G*0), M-12+(G*2))
stroke(None)






# Saar #################################################################
new_page(0)
fill(0)

# image("images/rb001.png", ((G*28)+11, (G*(3))-7), alpha=1)
# Bitmaps
image("images/lgm-1344.jpg", (0, -30), alpha=1)

# black:
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(5):
    fill(green, green, green)
#    rect(M+(G*22)+(G*i), M+(G*15), (G), (G))
    green += 0.1
stroke(grid_color)

# red:
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(5):
    fill(red, green, blue)
#    rect(M+(G*22)+(G*i), M+(G*14), (G), (G))
    green += 0.1
stroke(grid_color)

# yellow:
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(5):
    fill(red, green, blue)
#    rect(M+(G*22)+(G*i), M+(G*13), (G), (G))
    green += 0.1
stroke(grid_color)

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(0)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5.0)
text("Saarbrücken", M-4, M+4+(G*13))

# Text
fontSize(30)
tracking(-1.0)
text("Libre", M+3+(G*22), M-2+(G*15))
text("Graphics", M+3+(G*22), M-2+(G*14))
text("Meeting 2019", M+3+(G*22), M-2+(G*13))





# Berlin #################################################################
new_page(0.5)
grid(34, 16, 0) # Toggle for grid view
edge(0)       # Toggle for safe area
fill(0.8)
stroke(0)

image("images/bg-01.gif", (0,  0), alpha=0.3)

# Shadow
#fill(0)
#rect(M+6+(G*0),  M-6+(G*13),  (G*29), (G*3))
#rect(M+6+(G*31), M-6+(G*13),  (G*3),  (G*3))

#rect(M+6+(G*1),  M-6+(G*6),      (G*10), (G*6))
#rect(M+6+(G*1),  M-6+(G*(1)),     (G*10), (G*4))
#rect(M+6+(G*12), M-6+(G*(5)),   (G*10), (G*6))

# Blocks
fill(0.5)
rect(M+(G*0),  M+(G*13), (G*29), (G*3))
rect(M+(G*31), M+(G*13), (G*3),  (G*3))

# Bitmaps
#image("images/berlin-03-672.jpg", (0, 300), alpha=1)
#image("images/berlin-04-672.jpg", (672, 300), alpha=1)
image("images/berlin-02-672.jpg", (M+(G*12), (G*(-5))), alpha=1)
image("images/berlin-03-320.jpg", (M+(G*1),  (G*10)), alpha=1)
image("images/berlin-01-320.jpg", (M+(G*1),  (G*5)), alpha=1)
#image("images/berlin-01-672.jpg", (672, -150), alpha=1)

# outlines
fill(None)
stroke(0)
rect(M+(G*1), M+(G*6), (G*10), (G*6))
rect(M+(G*1), M+(G*1), (G*10), (G*4))
rect(M+(G*12), M+(G*(-5)), (G*21), (G*17))

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(0)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-6.6)
text("Berlin Hack Week", M-2, M+4+(G*13))
tracking(None)

fill(None)
stroke(0)
text("3", M+8+(G*31), M+4+(G*13))
stroke(None)






# PROJECT GOALS  #################################################################
new_page(0)
grid(34, 16, grid_color) # Toggle for grid view
edge(grid_color)       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*23), (G*3))
rect(M+(G*31), M+(G*13), (G*3),  (G*3))
rect(M+(G*0),  M+(G*0),  (G*12), (G*12))
rect(M+(G*13), M+(G*0),  (G*12), (G*12))

# Top edge
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(6):
    fill(red, green, blue)
    rect(M+(G*24)+(G*i), M+(G*14), (G), (G))
    green += 0.1
stroke(grid_color)

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-3.4)
text("Project Goals", M-4, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
text("4", M+6+(G*31), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
image("images/rb001.png", ((G*28)+11, (G*(3))-7), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("2019", M+2, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("A working editor", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Basic GNU+Linux support", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("UFO Support (Norad)", M+2, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("", M+2, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("", M+2, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("", M+2, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("", M+2, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("", M+2, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("", M+2, M-2+(G*1))
fill(0.9, 0, 0.3)
text("", M+2, M-2+(G*0))

v_edge = M+2+(G*13)
fill(1)
text("2020+", v_edge, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("Full GNU+Linux support", v_edge, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Metaballs", v_edge, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Spiro curves", v_edge, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Foo", v_edge, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Foo", v_edge, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Foo", v_edge, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("Foo", v_edge, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Foo", v_edge, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Foo", v_edge, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Foo", v_edge, M-2+(G*0))






# Rust? #################################################################
new_page(0)
grid(34, 16, grid_color) # Toggle for grid view
edge(grid_color)       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*33), (G*3))
rect(M+(G*31), M+(G*13), (G*3),  (G*3))
rect(M+(G*0),  M+(G*0),  (G*12), (G*12))
rect(M+(G*13), M+(G*0),  (G*12), (G*12))

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-6.0)
text("Rust Programming", M-4, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
text("5", M-21+(G*32), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
image("images/rb002.png", ((G*28)+11, (G*(-9))-18), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("Pros", M+2, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("C/C++ level performance", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Ca", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Foo", M+2, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Foo", M+2, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Foo", M+2, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Foo", M+2, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("Foo", M+2, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Foo", M+2, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Foo", M+2, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Foo", M+2, M-2+(G*0))

v_edge = M+2+(G*13)
fill(1)
text("Cons", v_edge, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("GNU+Linux support", v_edge, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("UFO Support (Norad)", v_edge, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Foo", v_edge, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Foo", v_edge, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Foo", v_edge, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Foo", v_edge, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("Foo", v_edge, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Foo", v_edge, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Foo", v_edge, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Foo", v_edge, M-2+(G*0))






# Open-Source #################################################################
new_page(0)
grid(34, 16, grid_color) # Toggle for grid view
edge(grid_color)       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*22), (G*3))
rect(M+(G*31), M+(G*13), (G*3),  (G*3))
rect(M+(G*0),  M+(G*0),  (G*12), (G*12))
rect(M+(G*13), M+(G*0),  (G*12), (G*12))

# Top edge
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(6):
    fill(red, green, blue)
    rect(M+(G*24)+(G*i), M+(G*14), (G), (G))
    green += 0.1
stroke(grid_color)

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5.7)
text("Open Source", M-4, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
text("6", M-21+(G*32), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
#image("images/rb001.png", ((G*28)+11, (G*(3))-7), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("Education:", M+2, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("FAR", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("FAR", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Foo", M+2, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Foo", M+2, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Foo", M+2, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Foo", M+2, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("Foo", M+2, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Foo", M+2, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Foo", M+2, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Foo", M+2, M-2+(G*0))

v_edge = M+2+(G*13)
fill(1)
text("Customazation:", v_edge, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("GNU+Linux support", v_edge, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("UFO Support (Norad)", v_edge, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Foo", v_edge, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Foo", v_edge, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Foo", v_edge, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Foo", v_edge, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("Foo", v_edge, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Foo", v_edge, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Foo", v_edge, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Foo", v_edge, M-2+(G*0))


v_edge = M+2+(G*27)
fill(1)
text("How can you own [...] numbers? Numbers belong to the world.", v_edge, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("Numbers belong to the world.", v_edge, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("UFO Support (Norad)", v_edge, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Foo", v_edge, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Foo", v_edge, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Foo", v_edge, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Foo", v_edge, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("Foo", v_edge, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Foo", v_edge, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Foo", v_edge, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Foo", v_edge, M-2+(G*0))

# In the long run, making programs free is a step toward the postscarcity world, where nobody will have to work very hard just to make a living. People will be free to devote themselves to activities that are fun, such as programming,





# EJS #################################################################
new_page(0)
#grid(34, 16, grid_color) # Toggle for grid view
#edge(grid_color)       # Toggle for safe area
fill(0)

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-6.0)
text("Lil UFO&", M-4, M+4+(G*10))
text("TruFont&", M-4, M+4+(G*13))
text("FontForge&", M-4, M+4+(G*7))
text("RuneBender.", M-4, M+4+(G*4))

# Bitmaps
#image("images/rb001.png", ((G*28)+11, (G*(3))-7), alpha=1)






# Fontforge #################################################################
new_page(0)
grid(34, 16, grid_color) # Toggle for grid view
edge(grid_color)       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*18), (G*3))
rect(M+(G*31), M+(G*13), (G*3),  (G*3))

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5.7)
text("FontForge", M-4, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
text("3", M-21+(G*32), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
image("images/fontforge-1344.jpg", (0, 0), alpha=1)


# Headline Tex
font("fonts/Splinter-Bold.ttf")
stroke(0)
fontSize(120)
fontVariations(wght=700)
tracking(-6.0)
step = 0.0
for i in range(3):
    f = (i*0.2) + step
    fill(f)
    text("Font Forge", M-4+(i*4), M+4+(G*13)+(i*(-4)))
tracking(None)






# TruFont #########################################
new_page(0)

image("images/trufont.png", (0, 0), alpha=1)

# Headline Tex
font("fonts/Splinter-Bold.ttf")
stroke(0)
fontSize(120)
fontVariations(wght=700)
tracking(-6.0)
step = 0.2
for i in range(6):
    f = (i*0.1) + step
    fill(f)
    text("Tru Font", M-4+(i*4), M+4+(G*13)+(i*(-4)))
tracking(None)


# Lil UFO #########################################
new_page(0)
image("images/lilufo.png", (0, 0), alpha=1)


# Headline Text
font("fonts/Splinter-Bold.ttf")
stroke(0)
fontSize(120)
fontVariations(wght=700)
tracking(-6.0)
step = 0.0
for i in range(9):
    f = (i*0.1) + step
    fill(f)
    text("Lil UFO", M-4+(i*4), M+4+(G*13)+(i*(-4)))
tracking(None)







# Education #################################################################
new_page(0)
grid(34, 16, grid_color) # Toggle for grid view
edge(grid_color)       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*17), (G*3))
rect(M+(G*31), M+(G*13), (G*3),  (G*3))
rect(M+(G*0),  M+(G*0),  (G*12), (G*12))
rect(M+(G*13), M+(G*0),  (G*12), (G*12))

# Top edge
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(12):
    fill(red, green, blue)
    rect(M+(G*18)+(G*i), M+(G*14), (G), (G))
    green += 0.1
stroke(grid_color)

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5.7)
text("Education", M-0, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
tracking(-8.0)
text("11", M-0+(G*31), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
image("images/free-320.jpg", ((G*30), (G*(3))), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("We need", M+2, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("Early Users", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Bug reports", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("UI concepts", M+2, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("", M+2, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Foo", M+2, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Foo", M+2, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("Foo", M+2, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Foo", M+2, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Foo", M+2, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Foo", M+2, M-2+(G*0))

v_edge = M+2+(G*13)
fill(1)
text("Foo", v_edge, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("Foo", v_edge, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Foo", v_edge, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Foo", v_edge, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Foo", v_edge, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Foo", v_edge, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Foo", v_edge, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("Foo", v_edge, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Foo", v_edge, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Foo", v_edge, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Foo", v_edge, M-2+(G*0))







# Get Involved #################################################################
new_page(0)
grid(34, 16, grid_color) # Toggle for grid view
edge(grid_color)       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*21), (G*3))
rect(M+(G*30), M+(G*13), (G*4),  (G*3))
rect(M+(G*0),  M+(G*0),  (G*12), (G*12))
rect(M+(G*13), M+(G*0),  (G*12), (G*12))

# Top edge
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(7):
    fill(red, green, blue)
    rect(M+(G*22)+(G*i), M+(G*14), (G), (G))
    green += 0.1
stroke(grid_color)

# Headline Text
font("fonts/Splinter-Bold.ttf")
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5.7)
text("Get Involved", M-0, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
tracking(-9)
text("12", M-0+(G*30), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
image("images/rc-320.png", ((G*30), (G*(3))+3), alpha=1)
image("images/pi-320.png", ((G*30), (G*(10))+6), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("We need:", M+2, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("Early users", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Bug reports", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("UI concepts", M+2, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Documentation", M+2, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Rust programmers", M+2, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("Python programmers", M+2, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("New programmers", M+2, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Your ideas and feedback", M+2, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Tool requests", M+2, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Help with Arabic support", M+2, M-2+(G*0))

v_edge = M+2+(G*13)
fill(1)
text("You will learn:", v_edge, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("How a font editor works", v_edge, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Unix command line skills", v_edge, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Rust programming", v_edge, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Software engineering", v_edge, M-2+(G*6))
fill(0.9, 0.5, 0.3)
text("Git", v_edge, M-2+(G*5))
fill(0.9, 0.4, 0.3)
text("GitHub", v_edge, M-2+(G*4))
fill(0.9, 0.3, 0.3)
text("GNU+Linux", v_edge, M-2+(G*3))
fill(0.9, 0.2, 0.3)
text("Math", v_edge, M-2+(G*2))
fill(0.9, 0.1, 0.3)
text("Vim", v_edge, M-2+(G*1))
fill(0.9, 0, 0.3)
text("Cargo", v_edge, M-2+(G*0))


fill(None)
stroke(grid_color)
rect(M+(G*26),  M+(G*(-1)), (G*10), (G*7))






# Thank You #####################################################################
new_page(0)
grid(34, 16, grid_color) # Toggle for grid view
edge(grid_color)       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0), M+(G*13), (G*19), (G*3))
rect(M+(G*30), M+(G*13), (G*4),  (G*3))
rect(M+(G*0), M+(G*11), (G*32), (G*1))
rect(M+(G*0), M+(G*6),  (G*10), (G*4))
rect(M+(G*0), M+(G*1),  (G*7),  (G*4))
rect(M+(G*0), M+(G*0),  (G*19), (G*1))

# Line
stroke(0)
red, green, blue = 0.9, 0.1, 0.2
for i in range(10):
    fill(red, green, blue)
    rect(M+(G*22), M+(0)+(G*i), (G), (G))
    green += 0.1
stroke(grid_color)

# Text Headline
font("fonts/Splinter-Bold.ttf")
fontSize(120)
tracking(-5.0)
stroke(None)
fill(1)
text("Thank You!", M-0+(G*0), M+4+(G*13))

fill(0)
stroke(grid_color)
tracking(-8.0)
text("13", M-0+(G*30), M+4+(G*13))
fill(1)
stroke(None)

# Bitmaps
#image("images/nmaps.png", (M+(G*26), M+(G*13)), alpha=1)
image("images/berlin-04-320.jpg", ((G*28), (G*4)), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontVariations(wght=400)
fontSize(30)
tracking(-0.1)
text("Slides made with DrawBot: github.com/eliheuer/type-thursday-talk-2019", M+3, M-2+(G*11))
tracking(None)
fill(0.9, 0.9, 0.3)
text("Eli Heuer", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("@eliheuer", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("https://elih.blog", M+2, M-2+(G*7))
fill(0.9, 0.5, 0.3)
text("elih@member.fsf.org", M+2, M-2+(G*6))
fill(0.9, 0.6, 0.3)
fill(0.9, 0, 0.3)
text("https://github.com/linebender/runebender", M+2, M-2+(G*0))

# MB42 Type
font("fonts/Isotherma-Alpha.ttf")
fill(0)
stroke(grid_color)
fontSize(120)
text("Runebender", M+3+(G*0), M-12+(G*2))
stroke(None)

saveImage("slides.pdf")

