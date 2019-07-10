# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/
# 🌍 GIT URL: https://github.com/eliheuer/type-thursday-talk-2019
# ✅ Runebender

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN, [G] GRID UNIT
W, H, M, G = 1344.0, 768.0, 128.0, 32.0
grid_color = 0.3

# EDGE #########################################################################
def edge():
    #960, 704
    stroke(grid_color)
    strokeWidth(1)
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# GRID #########################################################################
def grid(X, Y):
    stroke(grid_color)
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
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)

# Runebender #####################################################################
new_page()
grid(34, 16) # Toggle for grid view
edge()       # Toggle for safe area
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
for i in range(8):
    fill(red, green, blue)
    rect(M+(G*32), M+(G)+(G*i), (G), (G))
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
text("1", M-14+(G*32), M+4+(G*13))
fill(1)
stroke(None)

# Bitmaps
#image("images/nmaps.png", (M+(G*26), M+(G*13)), alpha=1)
image("images/blob002s.png", (749, 69), alpha=1)

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

# Frame Done

# PROJECT GOALS  #################################################################
new_page()
grid(34, 16) # Toggle for grid view
edge()       # Toggle for safe area
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
text("2", M-21+(G*32), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
image("images/rb001.png", ((G*28)+11, (G*(3))-7), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("2019", M+2, M-2+(G*11))
#fill(0.9, 0.9, 0.3)
text("Rust UFO Support", M+2, M-2+(G*9))
#fill(0.9, 0.8, 0.3)
text("Rust Interpolation", M+2, M-2+(G*8))
#fill(0.9, 0.7, 0.3)
text("Foo", M+2, M-2+(G*7))
#fill(0.9, 0.6, 0.3)
text("Foo", M+2, M-2+(G*6))
#fill(0.9, 0.5, 0.3)
text("Foo", M+2, M-2+(G*5))
#fill(0.9, 0.4, 0.3)
text("Foo", M+2, M-2+(G*4))
#fill(0.9, 0.3, 0.3)
text("Foo", M+2, M-2+(G*3))
#fill(0.9, 0.2, 0.3)
text("Foo", M+2, M-2+(G*2))
#fill(0.9, 0.1, 0.3)
text("Foo", M+2, M-2+(G*1))
#fill(0.9, 0, 0.3)
text("Foo", M+2, M-2+(G*0))

v_edge = M+2+(G*13)
fill(1)
text("2020", v_edge, M-2+(G*11))
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

# Page 2 Done

# Why Rust? #################################################################
new_page()
grid(34, 16) # Toggle for grid view
edge()       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*18), (G*3))
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
text("Why Rust?", M-4, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
text("3", M-21+(G*32), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
#image("images/rb001.png", ((G*28)+11, (G*(3))-7), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("Rust Has:", M+2, M-2+(G*11))
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
text("Python", v_edge, M-2+(G*11))
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

# Page 3 Done

# Why Open-Source? #################################################################
new_page()
grid(34, 16) # Toggle for grid view
edge()       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*18), (G*3))
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
text("Why Rust?", M-4, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
text("3", M-21+(G*32), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
#image("images/rb001.png", ((G*28)+11, (G*(3))-7), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("Rust Has:", M+2, M-2+(G*11))
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
text("Python", v_edge, M-2+(G*11))
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

# Page 3 Done

# Other Editor #################################################################
new_page()
grid(34, 16) # Toggle for grid view
edge()       # Toggle for safe area
fill(0)

# Blocks
stroke(grid_color)
rect(M+(G*0),  M+(G*13), (G*18), (G*3))
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
text("Why Rust?", M-4, M+4+(G*13))

# Number
fill(0)
stroke(grid_color)
text("3", M-21+(G*32), M+4+(G*13))
stroke(None)
fill(1)

# Bitmaps
#image("images/rb001.png", ((G*28)+11, (G*(3))-7), alpha=1)

# Text
font("fonts/Splinter-Regular.ttf")
fontSize(30)
tracking(None)
text("Rust Has:", M+2, M-2+(G*11))
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
text("Python", v_edge, M-2+(G*11))
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

# Page 3 Done













# #############################################################################
new_page()
grid(34, 16) # Toggle for grid view
edge()       # Toggle for safe area
fill(0)

fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5)
text("History", M-4, M+4+(G*13))

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
# #############################################################################
new_page()
grid(34, 16) # Toggle for grid view
edge()       # Toggle for safe area
fill(0)
rect(M+(G*0), M+(G*13), (G*21), (G*3))
rect(M+(G*0), M+(G*11), (G*21), (G*1))
rect(M+(G*0), M+(G*9),  (G*9),  (G*1))
rect(M+(G*0), M+(G*8),  (G*10), (G*1))

red, green, blue = 0.9, 0.0, 0.2
for i in range(11):
    fill(red, green, blue)
    rect(M+(G*33), M+(G*i), (G), (G))
    green += 0.1

fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5)
text("Why Rust?", M-4, M+4+(G*13))
fontSize(30)
fontVariations(wght=400)
tracking(None)


text("https://www.rust-lang.org", M+2, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("Rust is fun.", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Cargo: One coheasive tool.", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Performance", M+2, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Community", M+2, M-2+(G*6))


text("https://www.rust-lang.org", M+2, M-2+(G*11))
fill(0.9, 0.9, 0.3)
text("Rust is fun.", M+2, M-2+(G*9))
fill(0.9, 0.8, 0.3)
text("Cargo: One coheasive tool.", M+2, M-2+(G*8))
fill(0.9, 0.7, 0.3)
text("Performance", M+2, M-2+(G*7))
fill(0.9, 0.6, 0.3)
text("Community", M+2, M-2+(G*6))

# #############################################################################
new_page()
#grid(34, 16) # Toggle for grid view
#edge()       # Toggle for safe area
fill(0)
rect(M+(G*0), M+(G*13), (G*21), (G*3))
rect(M+(G*0), M+(G*11), (G*22), (G*1))
rect(M+(G*0), M+(G*9), (G*9), (G*1))
rect(M+(G*0), M+(G*8), (G*10), (G*1))
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5)
text("Runebender", M-4, M+4+(G*13))
fontSize(30)
fontVariations(wght=400)
tracking(None)
text("A new open-source, cross-platform font editor.", M+2, M-2+(G*11))
text("Speaker: Eli Heuer", M+2, M-2+(G*9))
text("Date: July 11th, 2019", M+2, M-2+(G*8))
# #############################################################################


# #############################################################################
new_page()
#grid(34, 16) # Toggle for grid view
#edge()       # Toggle for safe area
fill(0)
rect(M+(G*0), M+(G*13), (G*21), (G*3))
rect(M+(G*0), M+(G*11), (G*24), (G*1))
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5)
text("Why Rust?", M-4, M+4+(G*13))
fontSize(36)
fontVariations(wght=500)
tracking(-1)
fill(1,0,0)
text("Rust is FUN", M+2, M+3+(G*11))
fill(1,0.5,0)
text("Cargo: Tooling is easy to use", M+2, M+3+(G*10))


# #############################################################################
new_page()
#grid(34, 16) # Toggle for grid view
#edge()       # Toggle for safe area
fill(0)
rect(M+(G*0), M+(G*13), (G*21), (G*3))
rect(M+(G*0), M+(G*11), (G*24), (G*1))
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5)
text("Berlin Hack Week", M-4, M+4+(G*13))
fontSize(36)
fontVariations(wght=500)
tracking(-1)
fill(1,0,0)
text("Rust is FUN", M+2, M+3+(G*11))
fill(1,0.5,0)
text("Cargo: Tooling is easy to use", M+2, M+3+(G*10))


# #############################################################################
new_page()
#grid(34, 16) # Toggle for grid view
#edge()       # Toggle for safe area
fill(0)
rect(M+(G*0), M+(G*13), (G*21), (G*3))
rect(M+(G*0), M+(G*11), (G*24), (G*1))
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5)
text("GNU+Linux", M-4, M+4+(G*13))
fontSize(36)
fontVariations(wght=500)
tracking(-1)
fill(1,0,0)
text("I", M+2, M+3+(G*11))
fill(1,0.5,0)
text("Cargo: Tooling is easy to use", M+2, M+3+(G*10))


# #############################################################################
new_page()
#grid(34, 16) # Toggle for grid view
#edge()       # Toggle for safe area
fill(0)
rect(M+(G*0), M+(G*13), (G*21), (G*3))
rect(M+(G*0), M+(G*11), (G*24), (G*1))
fill(1)
stroke(None)
fontSize(120)
fontVariations(wght=700)
tracking(-5)
text("GNU+Linux", M-4, M+4+(G*13))
fontSize(36)
fontVariations(wght=500)
tracking(-1)
fill(1,0,0)
text("In the long run, making programs free is a step towards a postscarcity", M+2, M+3+(G*11))
fill(1,0.5,0)
text("world, where nobody will have to work very hard just to make a living. ", M+2, M+3+(G*10))







saveImage("slides.pdf")

