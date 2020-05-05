import argparse
import xml.etree.ElementTree

import tile_utils
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
        self.path = None

    def initialize(self):
        attribute = dict()
        attribute['xmlns'] = 'http://www.w3.org/2000/svg'
        attribute['viewBox'] = '0 0 ' + str(self.width) + ' ' + str(self.height)
        attribute['width'] = str(self.width)
        attribute['height'] = str(self.height)
        self.root = xml.etree.ElementTree.Element('svg', attribute)
        xml.etree.ElementTree.SubElement(self.root, 'g')

        self.draw_polygon([(0, 0), (0, self.height), (self.width, self.height), (self.width, 0)],
                          255,
                          'fill:#ffffff;stroke:none')

    def draw_polygon(self, vertices_list, color=None, style_value=None):

        d_value = 'M '
        for vertex in vertices_list:
            d_value += str(vertex[0]) + ',' + str(vertex[1]) + ' '
        d_value += 'z'

        if style_value is None:
            # color_string = "{:02x}".format(int(color)) * 3
            # style_value = 'fill:#' + color_string + ';stroke:none'
            style_value = 'fill:none;stroke:#000000;stroke-width:0.1px'

        svg = self.root
        g = svg.find('g')
        xml.etree.ElementTree.SubElement(g, 'path', {'d': d_value, 'style': style_value})

    def draw_polygon_spiral(self, polygon_list, color_step):
        for polygon in polygon_list:
            step = 0
            new_polygon = polygon
            while new_polygon is not None:
                self.draw_polygon(new_polygon, step * color_step)
                new_polygon = polygon_utils.generate_interior_polygon(new_polygon, 0.01 * self.width)
                step += 1

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

    return args.svg_path


if __name__ == "__main__":
    svg_path = cli()

    svg = SVG()
    svg.path = svg_path
    polygon_list = tile_utils.tile_hhvv(svg.width, svg.height, 2, 4)
    svg.draw_polygon_spiral(polygon_list, 1)
    svg.write(svg_path)
