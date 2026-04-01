from PIL import Image, ImageDraw, ImageFont
import math

def make_icon(size):
    img = Image.new('RGBA', (size, size), (10, 22, 40, 255))
    draw = ImageDraw.Draw(img)
    
    # Water ripple circles
    cx, cy = size//2, size//2
    for i in range(3):
        r = int(size * (0.25 + i*0.12))
        alpha = 80 - i*20
        for dx in range(-r, r+1):
            for dy in range(-r, r+1):
                dist = math.sqrt(dx*dx + dy*dy)
                if abs(dist - r) < size*0.015:
                    x, y = cx+dx, cy+dy
                    if 0 <= x < size and 0 <= y < size:
                        draw.point((x,y), fill=(29, 158, 117, alpha))
    
    # Lure body - elongated ellipse
    lw = int(size*0.55)
    lh = int(size*0.18)
    lx = cx - lw//2
    ly = cy - lh//2
    draw.ellipse([lx, ly, lx+lw, ly+lh], fill=(255, 140, 0, 255))
    
    # Lure shine
    draw.ellipse([lx+int(lw*0.1), ly+int(lh*0.1), lx+int(lw*0.4), ly+int(lh*0.45)], fill=(255, 200, 100, 180))
    
    # Hook
    hx = lx + lw - int(size*0.04)
    hy = ly + lh//2
    hook_r = int(size*0.1)
    draw.arc([hx-hook_r, hy, hx+hook_r, hy+hook_r*2], start=0, end=180, fill=(180,180,200,255), width=max(2,size//64))
    
    # Eye
    ex = lx + int(lw*0.15)
    ey = cy - int(lh*0.05)
    er = max(2, size//32)
    draw.ellipse([ex-er, ey-er, ex+er, ey+er], fill=(255,255,255,255))
    draw.ellipse([ex-er//2, ey-er//2, ex+er//2, ey+er//2], fill=(0,0,0,255))
    
    return img

for sz in [192, 512]:
    img = make_icon(sz)
    img.save(f'/home/claude/lure-app/icon-{sz}.png')
    print(f'icon-{sz}.png done')
