"""
Program name: textured_cubes_rotation_1.py 
Objective: Fully cover two cubes with photo images. 
Observe the result of ignoring pixel depth. 


comments: There are six 256 x 256 bmp images on the faces of a cube. 
Usable image types:    bmp  and jpg work fine, but png does not.  
Attempting to use png we get: "SystemError: unknown raw mode"  

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3       
Author:    De Fine 
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

# Rotation angles for each cube.
xrot1 = yrot1 = zrot1 = 0.0
xrot2 = yrot2 = zrot2 = 0.0
# =================================================================
texture_1 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
image_proto = pygame.image.load("chess.png")
ix = image_proto.get_width()
iy = image_proto.get_height()

print('ix:', ix)                          # Just checking.
print('iy:', iy)


def texture_setup(image_name, texture_num, ix, iy):
    """  Assign texture attributes to specific images. 
    """
    glBindTexture(GL_TEXTURE_2D, texture_1[texture_num])
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glEnable(GL_TEXTURE_2D)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, image_name)


def LoadTextures():
    """  Open images and convert them to "raw" pixel maps and 
             bind or associate each image with and integer refernece number. 
    """
    image_12 = pygame.image.load("chess.png")
    image_11 = pygame.image.load("chess.png")
    image_10 = pygame.image.load("chess.png")
    image_9 = pygame.image.load("chess.png")
    image_8 = pygame.image.load("chess.png")
    image_7 = pygame.image.load("chess.png")

    image_6 = pygame.image.load("chess.png")
    image_5 = pygame.image.load("chess.png")
    image_4 = pygame.image.load("chess.png")
    image_3 = pygame.image.load("chess.png")
    image_2 = pygame.image.load("chess.png")
    image_1 = pygame.image.load("chess.png")

    # convert bmp to the type needed for textures
    image_1 = pygame.image.tostring(image_1, "RGBA", 1)
    image_2 = pygame.image.tostring(image_2, "RGBA", 1)
    image_3 = pygame.image.tostring(image_3, "RGBA", 1)
    image_4 = pygame.image.tostring(image_4, "RGBA", 1)
    image_5 = pygame.image.tostring(image_5, "RGBA", 1)
    image_6 = pygame.image.tostring(image_6, "RGBA", 1)

    image_7 = pygame.image.tostring(image_7, "RGBA", 1)
    image_8 = pygame.image.tostring(image_8, "RGBA", 1)
    image_9 = pygame.image.tostring(image_9, "RGBA", 1)
    image_10 = pygame.image.tostring(image_10, "RGBA", 1)
    image_11 = pygame.image.tostring(image_11, "RGBA", 1)
    image_12 = pygame.image.tostring(image_12, "RGBA", 1)

    glGenTextures(11, texture_1)   # Create texture number and names and sizw.
    # =====================================
    texture_setup(image_1, 0, ix, iy)
    texture_setup(image_2, 1, ix, iy)
    texture_setup(image_3, 2, ix, iy)
    texture_setup(image_4, 3, ix, iy)
    texture_setup(image_5, 4, ix, iy)
    texture_setup(image_6, 5, ix, iy)

    texture_setup(image_7, 6, ix, iy)
    texture_setup(image_8, 7, ix, iy)
    texture_setup(image_9, 8, ix, iy)
    texture_setup(image_10, 9, ix, iy)
    texture_setup(image_11, 10, ix, iy)
    texture_setup(image_12, 11, ix, iy)


def InitGL(Width, Height):
    """ A general OpenGL initialization function.  Sets all of the initial parameters. 
            We call this right after our OpenGL window is created. 
    """
    glClearColor(
        0.0, 0.0, 0.0, 0.0)          # Clear the background color to black.
    glClearDepth(1.0)                              # Clear the Depth buffer.
    glDepthFunc(GL_LESS)                   # The type Of depth test to do.
    # Leave this Depth Testing and observe the visual weirdness.
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    # Reset The Projection Matrix.
    glLoadIdentity()
    # Aspect ratio. Make window resizable.
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# ==============================================================


def make_cube_1(texture, texture_index):
    """   A generic cube. A texture binding created with glBindTexture remains active until a different 
                    texture is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
    """
    glBindTexture(GL_TEXTURE_2D, texture[texture_index])
    # Front Face (Each texture's corner is matched a quad's corner.)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)  # Bottom Left of The Texture and Quad
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)  # Bottom Right of The Texture and Quad
    glTexCoord2f(1.0, 1.0)
    # Top Right of The Texture and Quad
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)  # Top Left of The Texture and Quad
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[texture_index+1])
    # Back Face
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)  # Top Rightn
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)  # Top Left
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Left
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[texture_index+2])
    # Top Face
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)  # Top Left
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0,  1.0,  1.0)             # Bottom Left
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0,  1.0,  1.0)	             # Bottom Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)  # Top Right
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[texture_index+3])
    # Bottom Face
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Top Right
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)  # Top Left
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)  # Bottom Left
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)  # Bottom Right
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[texture_index+4])
    # Right face
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)  # Top Right
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0,  1.0,  1.0)	              # Top Left
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)  # Bottom Left
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[texture_index+5])
    # Left Face
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)  # Bottom Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)  # Top Right
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)  # Top Left
    glEnd()


def DrawFrontFace():
    """   A texture binding created with glBindTexture remains active until a different texture 
              is bound to the same target, or until the bound texture is deleted with glDeleteTextures.      
    """
    global xrot1, yrot1, zrot1, xrot2, yrot2, zrot2
    # Clear the screen and Depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # First textured cube.
    glLoadIdentity()					# Reset The View
    glTranslatef(-2.0, 0.0, -5.0)			# Shift cube left and back.
    glRotatef(xrot1, 1.0, 0.0, 0.0)			# Rotate the cube on It's X axis.
    glRotatef(yrot1, 0.0, 1.0, 0.0)			# Rotate the cube on It's Y axis.
    glRotatef(zrot1, 0.0, 0.0, 0.0)			# Rotate the cube on It's Z axis.
    # "0" is the first index no. of a six member sequence - images.
    make_cube_1(texture_1, 0)
    xrot1 = xrot1 + 0.2                # X rotation of first cube.
    yrot1 = yrot1 - 0.1                 # Y rotation
    zrot1 = zrot1 + 0.1                 # Z rotation

    # Second textured cube.
    glLoadIdentity()					# Reset The view
    glTranslatef(1.5, 0.0, -5.0)			             # Shift cube right and back.
    glRotatef(xrot2, 1.0, 0.0, 0.0)			# Rotate the cube on It's X axis.
    glRotatef(yrot2, 0.0, 1.0, 0.0)			# Rotate the cube on It's Y axis.
    glRotatef(zrot2, 0.0, 0.0, 0.0)			# Rotate the cube on It's Z axis
    # "6" is the first index no. of a different six member sequence - images.
    make_cube_1(texture_1, 6)
    xrot2 = xrot2 - 0.1                 # X rotation of second cube.
    yrot2 = yrot2 + 0.2                 # Y rotation
    zrot2 = zrot2 + 0.4                 # Z rotation

    glutSwapBuffers()
# =================================================================


def main():
    glutInit("")
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(1000, 480)
    window = glutCreateWindow(b"Textured rotating cubes")
    LoadTextures()
    glutDisplayFunc(DrawFrontFace)
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawFrontFace)
    InitGL(1000, 480)                               # Initialize our window.
    glutMainLoop()                                   # Start the event processing engine


main()
