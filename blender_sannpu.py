import os
import csv
import bpy


# 既存のメッシュオブジェクトを削除
for msh in bpy.data.meshes:
   bpy.data.meshes.remove(msh)

# 既存のマテリアルを削除
for mat in bpy.data.materials:
   bpy.data.materials.remove(mat)


# 新規マテリアルを作成
mat_r = bpy.data.materials.new('red')
mat_r.diffuse_color = (1.0, 0.0, 0.0, 1.0)

mat_b = bpy.data.materials.new('blue')
mat_b.diffuse_color = (0.0, 0.0, 1.0, 1.0)

mat_g = bpy.data.materials.new('green')
mat_g.diffuse_color = (0.0, 1.0, 0.0, 1.0)

mat_y = bpy.data.materials.new('yelow')
mat_y.diffuse_color = (0.5, 0.5, 0.0, 1.0)

mat_p = bpy.data.materials.new('purple')
mat_p.diffuse_color = (0.5, 0.0, 0.5, 1.0)

mat_lb = bpy.data.materials.new('l-blue')
mat_lb.diffuse_color = (0.0, 0.5, 0.5, 1.0)

mat_bk = bpy.data.materials.new('brack')
mat_bk.diffuse_color = (0.0, 0.0, 0.0, 1.0)

mat_w = bpy.data.materials.new('white')
mat_w.diffuse_color = (1.0, 1.0, 1.0, 1.0)


# CSVを読み込み、表示
with open(r"") as f:
   reader = csv.reader(f)
   for row in reader:
       bpy.ops.mesh.primitive_cube_add(
       size=5,location=(float(row[0])*0.3, float(row[1])*0.3, float(row[2])*0.3))
       if row[3] == 'red':
           bpy.context.object.data.materials.append(mat_r)
       elif row[3] == 'blue':
           bpy.context.object.data.materials.append(mat_b)
       elif row[3] == 'green':
           bpy.context.object.data.materials.append(mat_g)
       elif row[3] == 'yelow':
           bpy.context.object.data.materials.append(mat_y)
       elif row[3] == 'purple':
           bpy.context.object.data.materials.append(mat_p)
       elif row[3] == 'l-blue':
           bpy.context.object.data.materials.append(mat_lb)
       elif row[3] == 'brack':
           bpy.context.object.data.materials.append(mat_bk)
       elif row[3] == 'white':
          bpy.context.object.data.materials.append(mat_w)
