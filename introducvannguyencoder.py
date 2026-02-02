import random as r, time as t, math as m, shutil as s, os as o, sys as y
from collections import deque

NAMES = ['DUC', 'VAN', 'NGUYEN', 'DUC VAN NGUYEN', 'ducvannguyencoder']
A = NAMES[0]
B = len(A)
C = 3000  
D = 8.0  
E = 0.3  
F = 7.0 
G_DURATION = 60  

def G(r1, g1, b1):
    return f'\x1b[38;2;{int(r1)};{int(g1)};{int(b1)}m'

def H():
    return '\x1b[0m'


I = []
for i in range(C):
    t_val = i / C

    phase = (t_val * 360) % 360
    if phase < 60:
        r1, g1, b1 = 255, int(phase * 4.25), 0
    elif phase < 120:
        r1, g1, b1 = int(255 - (phase - 60) * 4.25), 255, 0
    elif phase < 180:
        r1, g1, b1 = 0, 255, int((phase - 120) * 4.25)
    elif phase < 240:
        r1, g1, b1 = 0, int(255 - (phase - 180) * 4.25), 255
    elif phase < 300:
        r1, g1, b1 = int((phase - 240) * 4.25), 0, 255
    else:
        r1, g1, b1 = 255, 0, int(255 - (phase - 300) * 4.25)
    I.append([r1, g1, b1])


hacker_particles = []
hacker_chars = ['0', '1', '01', '10', '11', '00', '·', '•', '°', '⋅', '∙']

def J():
 
    p = []
    for i in range(C):
        a = i / C * 2 * m.pi
        x = 20 * m.sin(a) ** 3
        y1 = 17 * m.cos(a) - 7 * m.cos(2 * a) - 4 * m.cos(3 * a) - 2 * m.cos(4 * a)
        z = (r.random() - 0.5) * 5
        p.append([x / 4, -y1 / 4, z / 15])
    return p

def K():
 
    p = []
    for i in range(C):
        char_idx = i % 3
        x_offset = (char_idx - 1) * 6
        if char_idx == 0:  # D
            angle = (i % 100) / 100 * 2 * m.pi
            x = x_offset + 2 * m.cos(angle)
            y1 = -3 + (i % 100) / 100 * 6
            z = 2 * m.sin(angle)
        elif char_idx == 1:  # U
            angle = (i % 100) / 100 * m.pi
            x = x_offset + 2 * m.cos(angle)
            y1 = -3 + (i % 100) / 100 * 6
            z = 2 * m.sin(angle)
        else:  # C
            angle = (i % 100) / 100 * 2 * m.pi
            x = x_offset + 2 * m.cos(angle)
            y1 = -3 + (i % 100) / 100 * 6
            z = 2 * m.sin(angle)
        p.append([x, y1, z])
    return p

def L():

    p = []
    for i in range(C):
        char_idx = i % 3
        x_offset = (char_idx - 1) * 5
        if char_idx == 0:  # V
            t1 = (i % 100) / 100
            x = x_offset + (2 - 4 * t1 if t1 < 0.5 else -2 + 4 * (t1 - 0.5))
            y1 = -3 + t1 * 6
            z = m.sin(t1 * m.pi) * 2
        elif char_idx == 1:  # A
            t1 = (i % 100) / 100
            x = x_offset + (2 * t1 - 1) * 2
            y1 = -3 + (1 - abs(2 * t1 - 1)) * 6
            z = m.sin(t1 * m.pi * 2) * 1.5
        else:  # N
            t1 = (i % 100) / 100
            x = x_offset + (2 * t1 - 1) * 2
            y1 = -3 + t1 * 6
            z = m.sin(t1 * m.pi) * 2
        p.append([x, y1, z])
    return p

def M():
 
    p = []
    for i in range(C):
        char_idx = i % 6
        x_offset = (char_idx - 2.5) * 3
        t1 = (i % 100) / 100
        x = x_offset + m.sin(t1 * m.pi * 2) * 1.5
        y1 = -3 + t1 * 6
        z = m.cos(t1 * m.pi * 3) * 2
        p.append([x, y1, z])
    return p

def N():

    p = []
    v = 5.0
    golden_ratio = (1 + 5 ** 0.5) / 2
    for i in range(C):
        theta = 2 * m.pi * i / golden_ratio
        phi = m.acos(1 - 2 * (i + 0.5) / C)
        p.append([v * m.sin(phi) * m.cos(theta), v * m.sin(phi) * m.sin(theta), v * m.cos(phi)])
    return p

def O():
 
    p = []
    r1 = 4.0
    r2 = 1.8
    for i in range(C):
        a = i % int(m.sqrt(C)) * (2 * m.pi / m.sqrt(C))
        b = i // int(m.sqrt(C)) * (2 * m.pi / (C / m.sqrt(C)))
        x = (r1 + r2 * m.cos(a)) * m.cos(b)
        y1 = (r1 + r2 * m.cos(a)) * m.sin(b)
        z = r2 * m.sin(a)
        p.append([x, y1, z])
    return p

def P():

    p = []
    points = 8
    outer_radius = 5
    inner_radius = 2.5
    for i in range(C):
        angle = i / C * 2 * m.pi * points
        if i % 2 == 0:
            radius = outer_radius
        else:
            radius = inner_radius
        x = radius * m.cos(angle)
        y1 = radius * m.sin(angle)
        z = m.sin(angle * 4) * 2
        p.append([x, y1, z])
    return p

def Q():
 
    p = []
    for i in range(C):
        t1 = i / C * 12 * m.pi
        strand = i % 3
        if strand == 0:
            x = 3 * m.cos(t1)
            z = 3 * m.sin(t1)
        elif strand == 1:
            x = 3 * m.cos(t1 + 2*m.pi/3)
            z = 3 * m.sin(t1 + 2*m.pi/3)
        else:
            x = 3 * m.cos(t1 + 4*m.pi/3)
            z = 3 * m.sin(t1 + 4*m.pi/3)
        y1 = -6 + i / C * 12
        p.append([x, y1, z])
    return p

def R():
  
    p = []
    for i in range(C):
        angle = i / C * 15 * m.pi
        radius = (i / C) ** 0.5 * 5
        height = -6 + i / C * 12
        x = radius * m.cos(angle)
        y1 = height
        z = radius * m.sin(angle)
        p.append([x, y1, z])
    return p

def S():

    p = []
    petals = 8
    for i in range(C):
        petal = i % petals
        t1 = i / C * 2 * m.pi
        radius = 4 * (1 + 0.6 * m.cos(petals * t1))
        x = radius * m.cos(t1)
        y1 = radius * m.sin(t1)
        z = m.sin(t1 * 4) * 1
        p.append([x, y1, z])
    return p

def T():

    p = []
    for i in range(C):
        angle = i / C * 8 * m.pi
        radius = 4 * (1 + 0.4 * m.sin(8 * angle))
        x = radius * m.cos(angle)
        y1 = radius * m.sin(angle)
        z = m.sin(angle * 16) * 0.5
        p.append([x, y1, z])
    return p

def U():

    p = []
    phi = (1 + 5 ** 0.5) / 2
    vertices = [
        [0, 1, phi], [0, 1, -phi], [0, -1, phi], [0, -1, -phi],
        [1, phi, 0], [1, -phi, 0], [-1, phi, 0], [-1, -phi, 0],
        [phi, 0, 1], [phi, 0, -1], [-phi, 0, 1], [-phi, 0, -1]
    ]
    for v in vertices:
        norm = m.sqrt(sum(x**2 for x in v))
        v[:] = [x / norm * 4.5 for x in v]
    
    edges = [
        (0, 1), (0, 2), (0, 8), (0, 10), (1, 3), (1, 8), (1, 9),
        (2, 3), (2, 6), (2, 10), (3, 6), (3, 9), (4, 5), (4, 6),
        (4, 8), (4, 11), (5, 7), (5, 9), (5, 11), (6, 7), (6, 10),
        (7, 9), (7, 10), (7, 11), (8, 9), (8, 10), (9, 11), (10, 11)
    ]
    
    n = C // len(edges)
    for a, b in edges:
        p1, p2 = (vertices[a], vertices[b])
        for i in range(n):
            p.append([p1[j] + (p2[j] - p1[j]) * (i / n) for j in range(3)])
    while len(p) < C:
        p.append(p[-1])
    return p

def V():

    p = []
    for i in range(C):
        theta = i / C * 2 * m.pi
        phi = m.acos(1 - 2 * i / C)
        radius = 4.5 * (1 + 0.4 * m.sin(8 * theta) * m.sin(6 * phi))
        x = radius * m.sin(phi) * m.cos(theta)
        y1 = radius * m.sin(phi) * m.sin(theta)
        z = radius * m.cos(phi)
        p.append([x, y1, z])
    return p

def W():

    p = []
    v = [[0, -6, 0], [5, 4, 5], [-5, 4, 5], [0, 4, -6]]
    e = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1)]
    n = C // len(e)
    for a, b in e:
        p1, p2 = (v[a], v[b])
        for i in range(n):
            p.append([p1[j] + (p2[j] - p1[j]) * (i / n) for j in range(3)])
    while len(p) < C:
        p.append(p[-1])
    return p

def X():

    p = []
    s1 = 4.0
    v = [[x, y, z] for x in (-s1, s1) for y in (-s1, s1) for z in (-s1, s1)]
    e = [(0, 1), (1, 3), (3, 2), (2, 0), (4, 5), (5, 7), (7, 6), (6, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    n = C // len(e)
    for a, b in e:
        p1, p2 = (v[a], v[b])
        for i in range(n):
            p.append([p1[j] + (p2[j] - p1[j]) * (i / n) for j in range(3)])
    while len(p) < C:
        p.append(p[-1])
    return p

def Y():

    p = []
    s1 = 5.0
    v = [[s1, 0, 0], [-s1, 0, 0], [0, s1, 0], [0, -s1, 0], [0, 0, s1], [0, 0, -s1]]
    e = [(4, 0), (4, 2), (4, 1), (4, 3), (5, 0), (5, 2), (5, 1), (5, 3), (0, 2), (2, 1), (1, 3), (3, 0)]
    n = C // len(e)
    for a, b in e:
        p1, p2 = (v[a], v[b])
        for i in range(n):
            p.append([p1[j] + (p2[j] - p1[j]) * (i / n) for j in range(3)])
    while len(p) < C:
        p.append(p[-1])
    return p

def Z(v, x, y, z):
    a, b, c = v
    b, c = (b * m.cos(x) - c * m.sin(x), b * m.sin(x) + c * m.cos(x))
    a, c = (a * m.cos(y) + c * m.sin(y), -a * m.sin(y) + c * m.cos(y))
    a, b = (a * m.cos(z) - b * m.sin(z), a * m.sin(z) + b * m.cos(z))
    return [a, b, c]

def AA(v, x, y, z):
    p = 18 / (v[2] + 25)
    return (int(x + v[0] * z * p * 1.8), int(y + v[1] * z * p), v[2])

def AB(p1, p2, w, h, b):
    x1, y1 = (p1[0], p1[1])
    x2, y2 = (p2[0], p2[1])
    dx, dy = (abs(x2 - x1), abs(y2 - y1))
    s1 = max(dx, dy)
    if not s1:
        return

    for i in range(0, s1, 1):
        k = i / s1
        x, y1 = (int(x1 + (x2 - x1) * k), int(y1 + (y2 - y1) * k))
        if 1 <= x <= w and 1 <= y1 <= h:

            color_shift = int((t.time() * 500) % 360)
            r1 = int(50 + 50 * m.sin(color_shift * 0.1))
            g1 = int(200 + 55 * m.sin(color_shift * 0.15))
            b1 = int(50 + 50 * m.sin(color_shift * 0.2))
            r1, g1, b1 = (int(r1 * b), int(g1 * b), int(b1 * b))

            hacker_chars = ['█', '▓', '▒', '░', '▄', '▀', '■', '□', '▪', '▫']
            char = hacker_chars[i % len(hacker_chars)]
            y.stdout.write(f'\x1b[{y1};{x}H{G(r1, g1, b1)}{char}')

def AC():
    y.stdout.write('\x1b[?25l')

def AD():
    y.stdout.write('\x1b[?25h')


AE = [J(), K(), L(), M(), N(), O(), P(), Q(), R(), S(), T(), U(), V(), W(), X(), Y()]
AF = [[r.uniform(-40, 40) for _ in range(3)] for _ in range(C)]

AC()
o.system('cls' if o.name == 'nt' else 'clear')
AG = t.time()
AH = -1
AI = 0
AK = deque(maxlen=300)  
hacker_particles = []  
AL = []
current_name_idx = 0
name_change_time = 0

try:
    while True:
        w1, h1 = s.get_terminal_size()
        cx, cy = (w1 // 2, h1 // 2)
        sc = min(w1, h1) // 3.5
        n1 = t.time()
        e1 = n1 - AG
        a1, a2, a3 = (e1 * 0.3, e1 * 0.5, e1 * 0.2)
        

        if e1 > 20 and current_name_idx < len(NAMES) - 1:
            if n1 - name_change_time > 10:  
                current_name_idx += 1
                A = NAMES[current_name_idx]
                B = len(A)
                AH = -1  
                name_change_time = n1
        
        sx = cx - B // 2
        p3 = []
        
        if e1 < F:
            k = e1 / F
            v = k * k * (3 - 2 * k)
            for i in range(C):
                p3.append([AF[i][j] + (AE[0][i][j] - AF[i][j]) * v for j in range(3)])
        else:
            m1 = (e1 - F) / D
            idx = int(m1) % len(AE)
            nx = (idx + 1) % len(AE)
            k = m1 - int(m1)
            v = k * k * (3 - 2 * k)
            for k1 in range(C):
                p3.append([AE[idx][k1][j] + (AE[nx][k1][j] - AE[idx][k1][j]) * v for j in range(3)])
        
        if e1 > 25 and AH < 0:
            AH = 0
            AI = n1
            
        if AH >= 0 and AH < B and (n1 - AI > E):
            AH += 1
            AI = n1
            
        AL = [l for l in AL if n1 < l[2]]
        
      
        if r.random() < 0.25: 
            for _ in range(r.randint(3, 6)): 
                hacker_particles.append({
                    'x': r.randint(1, w1),
                    'y': 1,
                    'speed': r.uniform(0.5, 1.5),  
                    'length': r.randint(5, 12),  
                    'color_phase': r.uniform(0, 360),
                    'char': r.choice(hacker_chars),
                    'life': r.uniform(1.0, 2.5)  
                })
        
    
        hacker_particles = [p for p in hacker_particles if p['y'] < h1 and p['life'] > 0]
        for particle in hacker_particles:
            particle['y'] += particle['speed']
            particle['life'] -= 0.016
            particle['color_phase'] = (particle['color_phase'] + 3) % 360  
            
           
            phase = particle['color_phase']
            r1 = int(80 + 80 * m.sin(phase * 0.05))  
            g1 = int(220 + 35 * m.sin(phase * 0.08))  
            b1 = int(80 + 80 * m.sin(phase * 0.06)) 
            
           
            alpha = max(0.4, particle['life'] / 2.5) 
            r1, g1, b1 = int(r1 * alpha), int(g1 * alpha), int(b1 * alpha)
            
            for i in range(int(particle['length'])):
                y_pos = int(particle['y'] - i)
                if 1 <= y_pos <= h1:
                    fade = 1.0 - (i / particle['length']) * 0.5 
                    fr, fg, fb = int(r1 * fade), int(g1 * fade), int(b1 * fade)
                    char_idx = (int(n1 * 5) + i) % len(particle['char'])
                    char = particle['char'][char_idx] if len(particle['char']) > 1 else particle['char']
                    y.stdout.write(f'\x1b[{y_pos};{int(particle["x"])}H{G(fr, fg, fb)}{char}')
            
        y.stdout.write('\x1b[H')
        pd = []
        for i in range(C):
            rd = Z(p3[i], a1, a2, a3)
            pd.append(AA(rd, cx, cy, sc))
            

        for l in AK:
            p1, p2 = (pd[l[0]], pd[l[1]])
            az = (p1[2] + p2[2]) / 2
            br = max(0.1, min(1.0, (az + 4) / 8))
            AB(p1, p2, w1, h1, br * 3.5)
            
        for i in range(C):
            px, py, pz = pd[i]
            if 1 <= px <= w1 and 1 <= py <= h1:
                br = max(0.5, min(2.0, (pz + 5) / 10)) * 3.5
                r1, g1, b1 = (int(I[i][0] * br), int(I[i][1] * br), int(I[i][2] * br))
                ci = i % B
                
                if ci < AH:
                    fx, fy = (sx + ci, cy)
                    fc = G(I[i][0], I[i][1], I[i][2])
                elif ci == AH:
                    k = min((n1 - AI) / E, 1)
               
                    angle = k * m.pi * 3
                    radius = (1 - k) * 4
                    offset_x = m.sin(angle * 4) * radius
                    offset_y = m.cos(angle * 3) * radius
                    fx = int(px + (sx + ci - px) * k + offset_x)
                    fy = int(py + (cy - py) * k + offset_y)
                    fc = G(r1, g1, b1)
                else:
                    fx, fy = (px, py)
                    fc = G(r1, g1, b1)
                    
                if 1 <= fx <= w1 and 1 <= fy <= h1:
       
                    if ci <= AH:
                        char = A[ci]
                        if ci == AH and (n1 - AI) < E / 2:
                            stars = ['✦', '✧', '★', '☆', '✨', '✪', '✫', '✬', '✭', '✮']
                            char = stars[r.randint(0, len(stars)-1)]
                        elif ci < AH:
                            if r.random() < 0.15:
                                char = '✧'
                    else:
                        chars = ['·', '•', '°', '⋅', '∙', '·', '•', '°', '⋅', '∙']
                        char = chars[i % len(chars)]
                    y.stdout.write(f'\x1b[{fy};{fx}H{fc}{char}')
                    
        if AH >= B and current_name_idx == len(NAMES) - 1:
            # Hiệu ứng kết thúc cực hoành tráng với ASCII art nhấp nháy
            ascii_arts = [
                """
                                                                                                                                            
                                                                                 ,--.                                                       
    ,---,                                                                      ,--.'|                                                       
  .'  .' `\\                               ,---.                            ,--,:  : |                                                       
,---.'     \\          ,--,               /__./|                   ,---, ,`--.'`|  ' :                    ,--,                        ,---,  
|   |  .`\\  |       ,'_ /|          ,---.;  ; |               ,-+-. /  ||   :  :  | |  ,----._,.       ,'_ /|                    ,-+-. /  | 
:   : |  '  |  .--. |  | :    ,---./___/ \\  | |   ,--.--.    ,--.'|'   |:   |   \\ | : /   /  ' /  .--. |  | :     .--,   ,---.  ,--.'|'   | 
|   ' '  ;  :,'_ /| :  . |   /     \\   ;  \\ ' |  /       \\  |   |  ,"' ||   : '  '; ||   :     |,'_ /| :  . |   /_ ./|  /     \\|   |  ,"' | 
'   | ;  .  ||  ' | |  . .  /    / '\\   \\  \\: | .--.  .-. | |   | /  | |'   ' ;.    ;|   | .\\  .|  ' | |  . ., ' , ' : /    /  |   | /  | | 
|   | :  |  '|  | ' |  | | .    ' /  ;   \\  ' .  \\__\\/: . . |   | |  | ||   | | \\   |.   ; ';  ||  | ' |  | /___/ \\: |.    ' / |   | |  | | 
'   : | /  ; :  | : ;  ; | '   ; :__  \\   \\   '  ," .--.; | |   | |  |/ '   : |  ; .''   .   . |:  | : ;  ; |.  \\  ' |'   ;   /|   | |  |/  
|   | '` ,/  '  :  `--'   \\'   | '.'|  \\   `  ; /  /  ,.  | |   | |--'  |   | '`--'   `---`-'| |'  :  `--'   \\\\  ;   :'   |  / |   | |--'   
;   :  .'    :  ,      .-./|   :    :   :   \\ |;  :   .'   \\|   |/      '   : |       .'__/\\_: |:  ,      .-./ \\  \\  ;|   :    |   |/       
|   ,.'       `--`----'     \\   \\  /     '---" |  ,     .-./'---'       ;   |.'       |   :    : `--`----'      :  \\  \\\\   \\  /'---'        
'---'                        `----'             `--`---'                '---'          \\   \\  /                  \\  ' ; `----'              
                                                                                        `--`-'                    `--`                      
                """,
                """
  o__ __o                               o              o                        o          o                                                               
 <|     v\\                             <|>            <|>                      <|\\        <|>                                                              
 / \\     <\\                            < >            < >                      / \\\\o      / \\                                                              
 \\o/       \\o    o       o       __o__  \\o            o/  o__ __o/  \\o__ __o   \\o/ v\\     \\o/    o__ __o/   o       o    o      o     o__  __o   \\o__ __o  
  |         |>  <|>     <|>     />  \\    v\\          /v  /v     |    |     |>   |   <\\     |    /v     |   <|>     <|>  <|>    <|>   /v      |>   |     |> 
 / \\       //   < >     < >   o/          <\\        />  />     / \\  / \\   / \\  / \\    \\o  / \\  />     / \\  < >     < >  < >    < >  />      //   / \\   / \\ 
 \\o/      /      |       |   <|             \\o    o/    \\      \\o/  \\o/   \\o/  \\o/     v\\ \\o/  \\      \\o/   |       |    \\o    o/   \\o    o/     \\o/   \\o/ 
  |      o       o       o    \\\\             v\\  /v      o      |    |     |    |       <\\ |    o      |    o       o     v\\  /v     v\\  /v __o   |     |  
 / \\  __/>       <\\__ __/>     _\\o__</        <\\/>       <\\__  / \\  / \\   / \\  / \\        < \\   <\\__  < >   <\\__ __/>      <\\/>       <\\/> __/>  / \\   / \\ 
                                                                                                       |                    /                              
                                                                                               o__     o                   o                               
                                                                                               <\\__ __/>                __/>                               
                """,
                """
                                                                                  
  ▄▄▄▄▄▄              ▄▄▄                   ▄▄     ▄▄▄                            
 █▀██▀▀██            █▀██  ██▀▀             ██▄   ██▀                             
   ██   ██             ██  ██       ▄       ███▄  ██    ▄▄                   ▄    
   ██   ██ ██ ██ ▄███▀ ██  ██ ▄▀▀█▄ ████▄   ██ ▀█▄██ ▄████ ██ ██ ██ ██ ▄█▀█▄ ████▄
 ▄ ██   ██ ██ ██ ██    ██▄ ██ ▄█▀██ ██ ██   ██   ▀██ ██ ██ ██ ██ ██▄██ ██▄█▀ ██ ██
 ▀██▀███▀ ▄▀██▀█▄▀███▄  ▀███▀▄▀█▄██▄██ ▀█ ▀██▀    ██▄▀████▄▀██▀█▄▄▀██▀▄▀█▄▄▄▄██ ▀█
                                                        ██         ██             
                                                      ▀▀▀        ▀▀▀              
                """,
                """
      d8b                                                                                                      
      88P                                                                                                      
     d88                                                                                                       
 d888888  ?88   d8P d8888b?88   d8P d888b8b    88bd88b   88bd88b  d888b8b  ?88   d8P?88   d8P  d8888b  88bd88b 
d8P' ?88  d88   88 d8P' `Pd88  d8P'd8P' ?88    88P' ?8b  88P' ?8bd8P' ?88  d88   88 d88   88  d8b_,dP  88P' ?8b
88b  ,88b ?8(  d88 88b    ?8b ,88' 88b  ,88b  d88   88P d88   88P88b  ,88b ?8(  d88 ?8(  d88  88b     d88   88P
`?88P'`88b`?88P'?8b`?888P'`?888P'  `?88P'`88bd88'   88bd88'   88b`?88P'`88b`?88P'?8b`?88P'?8b `?888P'd88'   88b
                                                                        )88                )88                 
                                                                       ,88P               ,d8P                 
                                                                   `?8888P             `?888P'                 
                """,
                """
╦ ╦┌─┐┌─┐┬┌─┌─┐┬─┐  ╔╦╗┬ ┬┌─┐╦  ╦┌─┐┌┐┌╔╗╔┌─┐┬ ┬┬ ┬┌─┐┌┐┌╔═╗┌─┐┌┬┐┌─┐┬─┐
╠═╣├─┤│  ├┴┐├┤ ├┬┘   ║║│ ││  ╚╗╔╝├─┤│││║║║│ ┬│ │└┬┘├┤ │││║  │ │ ││├┤ ├┬┘
╩ ╩┴ ┴└─┘┴ ┴└─┘┴└─  ═╩╝└─┘└─┘ ╚╝ ┴ ┴┘└┘╝╚╝└─┘└─┘ ┴ └─┘┘└┘╚═╝└─┘─┴┘└─┘┴└─
                """
            ]
            

            for art_idx in range(len(ascii_arts)):
                for phase in range(30): 
                    y.stdout.flush()
                    t.sleep(0.08)
                    
          
                    y.stdout.write('\x1b[2J')
                    
            
                    art_lines = ascii_arts[art_idx].strip().split('\n')
                    
             
                    max_line_length = max(len(line) for line in art_lines)
                    start_x = max(1, (w1 - max_line_length) // 2)
                    start_y = max(1, (h1 - len(art_lines)) // 2)
                    
                 
                    for line_idx, line in enumerate(art_lines):
                        for char_idx, char in enumerate(line):
                            if char != ' ':
                              
                                color_phase = (phase * 12 + line_idx * 5 + char_idx * 3) % 360
                                if color_phase < 120:
                                    r1, g1, b1 = int(50 + 205 * (color_phase / 120)), 255, 50
                                elif color_phase < 240:
                                    r1, g1, b1 = 50, int(255 - 205 * ((color_phase - 120) / 120)), int(50 + 205 * ((color_phase - 120) / 120))
                                else:
                                    r1, g1, b1 = int(50 + 205 * ((color_phase - 240) / 120)), 50, 255
                                
                              
                                brightness = 0.5 + 0.5 * m.sin(phase * 0.3 + line_idx * 0.2 + char_idx * 0.1)
                                r1, g1, b1 = int(r1 * brightness), int(g1 * brightness), int(b1 * brightness)
                                
                      
                                x = start_x + char_idx
                                y_pos = start_y + line_idx
                                if 1 <= x <= w1 and 1 <= y_pos <= h1:
                                    y.stdout.write(f'\x1b[{y_pos};{x}H{G(r1, g1, b1)}{char}')
                    
  
                    for i in range(50):
                        angle = (phase * 0.1 + i * 0.13) % (2 * m.pi)
                        radius = 10 + 5 * m.sin(phase * 0.05 + i * 0.2)
                        px = int(cx + m.cos(angle) * radius)
                        py = int(cy + m.sin(angle) * radius)
                        
                        if 1 <= px <= w1 and 1 <= py <= h1:
                            color_phase = (phase * 15 + i * 7) % 360
                            r1 = int(128 + 127 * m.sin(color_phase * 0.01))
                            g1 = int(128 + 127 * m.sin(color_phase * 0.01 + 2))
                            b1 = int(128 + 127 * m.sin(color_phase * 0.01 + 4))
                            
                            stars = ['✦', '✧', '★', '☆', '✨', '✪', '✫', '✬']
                            char = stars[i % len(stars)]
                            y.stdout.write(f'\x1b[{py};{px}H{G(r1, g1, b1)}{char}')
            
            t.sleep(2)
            break
            
        y.stdout.flush()
        t.sleep(0.003)  
        y.stdout.write('\x1b[2J')
        
except KeyboardInterrupt:
    pass
AD()
o.system('cls' if o.name == 'nt' else 'clear')
