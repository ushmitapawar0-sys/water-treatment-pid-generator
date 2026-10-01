import ezdxf

class SymbolLibrary:
    def __init__(self, doc):
        self.doc = doc
        self.ports = {}
        self._create_tank_vert()
        self._create_pump_centrifugal()
        self._create_valve_gate()
        self._create_valve_check()
        self._create_valve_control()
        self._create_valve_safety()
        self._create_filter()
        self._create_instrument()
        self._create_instrument_panel()
        self._create_flow_arrow()
        self._create_line_break()

    def _create_tank_vert(self):
        block = self.doc.blocks.new(name="TANK_VERT")
        block.add_lwpolyline([(0, 0), (20, 0), (20, 40), (0, 40), (0, 0)])
        self.ports["TANK_VERT"] = {"inlet": (0, 30), "outlet": (20, 5), "top": (10, 40), "bottom": (10, 0)}

    def _create_pump_centrifugal(self):
        block = self.doc.blocks.new(name="PUMP_CENTRIFUGAL")
        block.add_circle((10, 10), 10)
        block.add_lwpolyline([(10, 10), (20, 20), (20, 0), (10, 10)])
        self.ports["PUMP_CENTRIFUGAL"] = {"inlet": (0, 10), "outlet": (10, 20)}

    def _create_valve_gate(self):
        block = self.doc.blocks.new(name="VALVE_GATE")
        block.add_lwpolyline([(0, 0), (0, 10), (10, 0), (10, 10), (0, 0)])
        self.ports["VALVE_GATE"] = {"inlet": (0, 5), "outlet": (10, 5)}

    def _create_valve_check(self):
        block = self.doc.blocks.new(name="VALVE_CHECK")
        block.add_lwpolyline([(0, 0), (0, 10), (10, 0), (10, 10), (0, 0)])
        block.add_lwpolyline([(3, 3), (3, 7), (7, 3), (7, 7)]) # N shape inside
        self.ports["VALVE_CHECK"] = {"inlet": (0, 5), "outlet": (10, 5)}

    def _create_valve_control(self):
        block = self.doc.blocks.new(name="VALVE_CONTROL")
        block.add_lwpolyline([(0, 0), (0, 10), (10, 0), (10, 10), (0, 0)])
        block.add_line((5, 5), (5, 15))
        block.add_lwpolyline([(1, 15), (9, 15), (9, 18), (1, 18), (1, 15)])
        self.ports["VALVE_CONTROL"] = {"inlet": (0, 5), "outlet": (10, 5), "signal": (5, 18)}

    def _create_valve_safety(self):
        block = self.doc.blocks.new(name="VALVE_SAFETY")
        block.add_lwpolyline([(0, 0), (0, 10), (5, 5), (0, 0)]) # Left triangle
        block.add_lwpolyline([(5, 5), (10, 10), (0, 10), (5, 5)]) # Top triangle
        self.ports["VALVE_SAFETY"] = {"inlet": (0, 5), "outlet": (5, 10)}

    def _create_filter(self):
        block = self.doc.blocks.new(name="FILTER")
        block.add_lwpolyline([(0, 0), (15, 0), (15, 20), (0, 20), (0, 0)])
        block.add_line((0, 20), (15, 0)) # Diagnoal line for filter
        self.ports["FILTER"] = {"inlet": (0, 10), "outlet": (15, 10)}

    def _create_instrument(self):
        block = self.doc.blocks.new(name="INSTRUMENT")
        block.add_circle((5, 5), 5)
        self.ports["INSTRUMENT"] = {"bottom": (5, 0), "top": (5, 10), "left": (0, 5), "right": (10, 5)}

    def _create_instrument_panel(self):
        block = self.doc.blocks.new(name="INSTRUMENT_PANEL")
        block.add_circle((5, 5), 5)
        block.add_line((0, 5), (10, 5))
        self.ports["INSTRUMENT_PANEL"] = {"bottom": (5, 0), "top": (5, 10), "left": (0, 5), "right": (10, 5)}

    def _create_flow_arrow(self):
        block = self.doc.blocks.new(name="FLOW_ARROW")
        block.add_lwpolyline([(0, 2), (5, 2), (5, 4), (10, 0), (5, -4), (5, -2), (0, -2), (0, 2)])
        self.ports["FLOW_ARROW"] = {}

    def _create_line_break(self):
        block = self.doc.blocks.new(name="LINE_BREAK")
        block.add_line((0, -3), (0, 3))
        block.add_line((2, -3), (2, 3))
        self.ports["LINE_BREAK"] = {}
