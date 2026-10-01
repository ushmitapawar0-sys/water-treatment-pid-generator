# Project 4: Water Treatment P&ID

## Overview
This project generates a full Piping and Instrumentation Diagram (P&ID) for a Water Treatment System autonomously using Python and `ezdxf`.

## How to Run
To run the generator and produce all outputs, execute:
```bash
python main.py
```
*(Requires `ezdxf` and `matplotlib` pip packages)*

This will generate:
- `water_treatment_pid.dxf`: AutoCAD compatible DXF file.
- `water_treatment_pid.png` & `.svg`: Image previews.
- `tags.json`: JSON registry of all components and tags.
- `validation_report.md`: Automated validation engine report.
- `checklist.md`: The final requirement checklist.

## Mapping to DecodeLabs Requirements
1. **Symbol Library (`symbols.py`)**: Defines a standardized, reusable object-oriented DXF block library with explicit coordinate connection ports for 0-gap snapping.
2. **Orthographic Routing (`router.py`)**: An intelligent routing function ensures that pipes only make 90-degree horizontal or vertical turns, avoiding any diagonal layouts.
3. **Tagging (`main.py`)**: All instruments and equipment use standard ISA 5.1 tagging logic (T-101, FCV-101, etc.) and save into a centralized JSON registry (`tags.json`).
4. **Systems Logic (`validate.py`)**: The system mathematically ensures pipe sizes match nozzle sizes, control loops form a complete Sensor->Controller->Valve loop, and segments are purely orthogonal.

## PFD vs P&ID
- **Process Flow Diagram (PFD)**: A high-level overview showing the core chemical or process flow. It highlights major equipment and overall plant design without getting bogged down in minor details.
- **Piping and Instrumentation Diagram (P&ID)**: A precise, highly detailed schematic that includes every single pipe, valve, sensor, and control system. It is the blueprint used for actual construction and safety validations, which is exactly what this project generates.
