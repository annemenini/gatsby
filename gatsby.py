import argparse
import math
import xml.etree.ElementTree

"""
Render an awesome Art Deco SVG
"""


def generate_polygon(num_vertices, scale, offset):
    vertices_list = []
    for i in range(num_vertices):
        alpha = i * 2 * math.pi / num_vertices
        v = (offset[0] + scale * math.cos(alpha), offset[1] + scale * math.sin(alpha))
        vertices_list.append(v)
    return vertices_list


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

    def draw_polygon(self, num_vertices):

        vertices_list = generate_polygon(num_vertices, 0.1 * self.width, (self.width / 2, self.height / 2))

        d_value = 'M '
        for vertex in vertices_list:
            d_value += str(vertex[0]) + ',' + str(vertex[1]) + ' '
        d_value += 'z'

        style_value = 'fill:#000000;stroke:none'

        svg = self.root
        g = svg.find('g')
        xml.etree.ElementTree.SubElement(g, 'path', {'d': d_value, 'style': style_value})

    def write(self, svg_path):
        tree = xml.etree.ElementTree.ElementTree(self.root)
        tree.write(svg_path)


def cli():
    """"Command Line Interface"""
    parser = argparse.ArgumentParser(description='Render an awesome Art Deco SVG.')

    parser.add_argument('--num-vertices', type=int, required=True,
                        help='Number of vertices of the polygon to start with.')
    parser.add_argument('--svg-path', type=str, required=True,
                        help='Path of the output SVG file.')

    args = parser.parse_args()

    return args.num_vertices, args.svg_path


if __name__ == "__main__":
    num_vertices, svg_path = cli()

    svg = SVG()
    svg.draw_polygon(num_vertices)
    svg.write(svg_path)
