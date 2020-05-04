import argparse
import xml.etree.ElementTree

import polygon_utils


"""
Render an awesome Art Deco SVG
"""


class SVG:
    def __init__(self):
        self.width = 210
        self.height = 297
        self.root = None
        self.initialize()

    def initialize(self):
        attribute = dict()
        attribute['xmlns'] = 'http://www.w3.org/2000/svg'
        attribute['viewBox'] = '0 0 ' + str(self.width) + ' ' + str(self.height)
        attribute['width'] = str(self.width)
        attribute['height'] = str(self.height)
        self.root = xml.etree.ElementTree.Element('svg', attribute)
        xml.etree.ElementTree.SubElement(self.root, 'g')

    def draw_polygon(self, vertices_list, color):

        d_value = 'M '
        for vertex in vertices_list:
            d_value += str(vertex[0]) + ',' + str(vertex[1]) + ' '
        d_value += 'z'

        color_string = "{:02x}".format(int(color)) * 3
        style_value = 'fill:#' + color_string + ';stroke:none'

        svg = self.root
        g = svg.find('g')
        xml.etree.ElementTree.SubElement(g, 'path', {'d': d_value, 'style': style_value})

    def draw_polygon_spiral(self, num_vertices, num_steps):
        vertices_list = polygon_utils.generate_polygon(num_vertices, 0.1 * self.width, (self.width / 2, self.height / 2))
        self.draw_polygon(vertices_list, 0)
        for i in range(1, num_steps):
            vertices_list = polygon_utils.generate_interior_polygon(vertices_list, 0.01 * self.width)
            self.draw_polygon(vertices_list, (i + 1) * 255 / num_steps)

    def write(self, svg_path):
        tree = xml.etree.ElementTree.ElementTree(self.root)
        tree.write(svg_path)


def cli():
    """"Command Line Interface"""
    parser = argparse.ArgumentParser(description='Render an awesome Art Deco SVG.')

    parser.add_argument('--num-vertices', type=int, required=True,
                        help='Number of vertices of the polygon to start with.')
    parser.add_argument('--num-steps', type=int, required=True,
                        help='Number of polygons.')
    parser.add_argument('--svg-path', type=str, required=True,
                        help='Path of the output SVG file.')

    args = parser.parse_args()

    return args.num_vertices, args.num_steps, args.svg_path


if __name__ == "__main__":
    num_vertices, num_steps, svg_path = cli()

    svg = SVG()
    svg.draw_polygon_spiral(num_vertices, num_steps)
    svg.write(svg_path)
