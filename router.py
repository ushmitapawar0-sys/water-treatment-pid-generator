def route_pipe(start, end, preference='H'):
    """
    Routes a pipe from start (x1, y1) to end (x2, y2) using only orthogonal segments (90-degree bends).
    preference: 
    'H' - Horizontal then Vertical
    'V' - Vertical then Horizontal
    'Z_H' - Z-shape starting horizontally
    'Z_V' - Z-shape starting vertically
    """
    x1, y1 = start
    x2, y2 = end
    
    # Snap EXACTLY to the port coordinates to ensure zero micro-gaps
    if preference == 'H':
        return [(x1, y1), (x2, y1), (x2, y2)]
    elif preference == 'V':
        return [(x1, y1), (x1, y2), (x2, y2)]
    elif preference == 'Z_H':
        mid_x = (x1 + x2) / 2
        return [(x1, y1), (mid_x, y1), (mid_x, y2), (x2, y2)]
    elif preference == 'Z_V':
        mid_y = (y1 + y2) / 2
        return [(x1, y1), (x1, mid_y), (x2, mid_y), (x2, y2)]
    else:
        return [(x1, y1), (x2, y1), (x2, y2)]
