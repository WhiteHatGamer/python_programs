#import bpy
from math import sin,cos


for i in range (36):
    bpy.ops.mesh.primitive_uv_sphere_add(location = (sin(i),cos(i),0))
    bpy.ops.mesh.primitive_uv_sphere_add(location = (sin(i),0,cos(i)))
    bpy.ops.mesh.primitive_uv_sphere_add(location = (0,sin(i),cos(i)))