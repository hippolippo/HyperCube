from tkinter import *


class Mesh:
    def __init__(self, ui, graph_dict):
        self.ui = ui
        self.graph_dict = graph_dict
        self.lines = set()
        self.translated_lines = set()
        for point in self.graph_dict:
            for point2 in self.graph_dict[point]:
                self.lines.add(frozenset({point, point2}))
                self.translated_lines.add(frozenset({self.translate(point), self.translate(point2)}))
        print(self.translated_lines)

    def translate(self, point: tuple):
        x, y = 0, 0
        for component in range(len(point)):
            x += point[component] * self.ui.get_unit_vectors()[component][0] + 20
            y += point[component] * self.ui.get_unit_vectors()[component][1] + 20
        return x, y

    def get_lines(self):
        return self.lines

    def get_translated_lines(self):
        return self.translated_lines


class UI:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root)
        self.canvas.pack()

    def start(self):
        self.root.mainloop()

    def get_dimensionality(self):
        return 6

    def get_unit_vectors(self):
        return [(20, 0), (0, 20), (10, 10), (15, 5), (30, 20), (-20, -30)]

    def draw_2D_Mesh(self, mesh: Mesh):
        lines = mesh.get_translated_lines()
        for line in lines:
            self.canvas.create_line(*(i for i in line))
