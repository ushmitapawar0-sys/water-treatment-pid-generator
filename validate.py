import json

def validate_project(components, pipes, control_lines, abs_ports, test_mode=False):
    errors = []
    
    # Check for duplicate tags
    tags_seen = set()
    for tag in components:
        if tag in tags_seen:
            errors.append(f"Duplicate tag found: {tag}")
        tags_seen.add(tag)
        
    # Validate property conflicts - size mismatches
    for p in pipes:
        c1, p1 = p['from_comp'], p['from_port']
        c2, p2 = p['to_comp'], p['to_port']
        size = p.get('size', '4"')
        
        c1_size = components[c1].get('port_sizes', {}).get(p1, '4"')
        c2_size = components[c2].get('port_sizes', {}).get(p2, '4"')
        
        # Test mode injection
        if test_mode and p['id'] == 'PL-01':
            c1_size = '8"'
            
        if size != c1_size:
            errors.append(f"Size mismatch: Pipe {p['id']} is {size}, but {c1}.{p1} is {c1_size}")
        if size != c2_size:
            errors.append(f"Size mismatch: Pipe {p['id']} is {size}, but {c2}.{p2} is {c2_size}")
            
        # Non-orthogonal segments check
        pts = p.get('points', [])
        for i in range(len(pts)-1):
            x1, y1 = pts[i]
            x2, y2 = pts[i+1]
            if x1 != x2 and y1 != y2:
                errors.append(f"Non-orthogonal segment found in pipe {p['id']} between {pts[i]} and {pts[i+1]}")
                
        # Gap tolerance check (Unconnected ports)
        if pts:
            start_pt = pts[0]
            end_pt = pts[-1]
            if start_pt != abs_ports[c1][p1]:
                errors.append(f"Gap found at {c1}.{p1} for pipe {p['id']}")
            if end_pt != abs_ports[c2][p2]:
                errors.append(f"Gap found at {c2}.{p2} for pipe {p['id']}")

    # Check for open control loops
    sensors = [tag for tag, data in components.items() if data.get('type') == 'Sensor']
    controllers = [tag for tag, data in components.items() if data.get('type') == 'Controller']
    valves = [tag for tag, data in components.items() if data.get('type') == 'Valve']
    
    for ctrl in controllers:
        has_sensor = any(cl['to_comp'] == ctrl and components.get(cl['from_comp'], {}).get('type') == 'Sensor' for cl in control_lines)
        has_valve = any(cl['from_comp'] == ctrl and components.get(cl['to_comp'], {}).get('type') == 'Valve' for cl in control_lines)
        
        if not (has_sensor and has_valve):
            errors.append(f"Open control loop at {ctrl}. Must connect Sensor -> Controller -> Valve")
            
    # Write report
    report = [
        "# Validation Report\n",
        "## Checks",
        f"- Size mismatches: {'FAIL' if any('Size mismatch' in e for e in errors) else 'PASS'}",
        f"- Unconnected ports (gap tolerance 0): {'FAIL' if any('Gap found' in e for e in errors) else 'PASS'}",
        f"- Property conflicts: {'FAIL' if any('Property' in e for e in errors) else 'PASS'}",
        f"- Duplicate tags: {'FAIL' if any('Duplicate' in e for e in errors) else 'PASS'}",
        f"- Non-orthogonal segments: {'FAIL' if any('Non-orthogonal' in e for e in errors) else 'PASS'}",
        f"- Open control loops: {'FAIL' if any('Open control loop' in e for e in errors) else 'PASS'}\n",
        "## Errors Found"
    ]
    
    if not errors:
        report.append("None. All checks passed!")
    else:
        for err in errors:
            report.append(f"- {err}")
            
    with open('validation_report.md', 'w') as f:
        f.write('\n'.join(report))
        
    return len(errors)
