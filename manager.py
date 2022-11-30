from UI import UI, Mesh


class Manager:

    def __init__(self, ui: UI):
        self.ui: UI = ui
        dimensionality: int = self.ui.get_dimensionality()
        mesh_dict: dict = dict()
        anchor: tuple = tuple(1 for i in range(dimensionality))
        outputs: set = [anchor]
        for point in outputs:
            if point not in mesh_dict:
                mesh_dict[point]: set = set()
                for component in range(dimensionality):
                    new_point = *point[:component], -point[component], *point[component+1:]
                    mesh_dict[point].add(new_point)
                    outputs.append(new_point)

        self.mesh: Mesh = Mesh(self.ui, mesh_dict)
