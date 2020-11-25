import argparse
import itertools
import pickle
from testing_code import *
from new_functions import *

def main(in_data):

    infile = open('GWAS_data.pickle', 'rb')

    test_data = pickle.load(infile)

    print(in_data)

    print(test_data)

    plot_fig = ManhattanPlot(test_data, gene=None)


    # ---------- Find out what should be linked

    # Find significant snps

    # group by same pathway

    # Add to link list

    point_1 = {'x': 1081000000, 'y': 8.761}
    point_2 = {'x': 1771000000, 'y': 8.737}
    point_3 = {'x': 1814000000, 'y': 13.142}

    # TODO: points need to be in order of x coordinates
    links = [
        {'pathway': 'M00082', 'links': [point_1, point_2, point_3]}
    ]


    # ---------- Iterate over linkage lists ---- (one at a time method)

    for pathway in links:

        node_number = 0

        while node_number < len(pathway['links']) - 1:

                add_line_between_points(plot_fig, pathway['links'][node_number], pathway['links'][node_number + 1], "Blue")

                node_number += 1

    '''
    
    plot_fig.add_shape(
        type="path",
        path="M 1081000000,8.761 Q 1400000000,10 1771000000,8.737",
        hoverinfo="SOMETHING"
    )
    '''

    plot_fig.show()




if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='''vis tool''',  epilog="""Version 0.1""")

    parser.add_argument('--input', type=str, help='Input file')

    args = parser.parse_args()

    main(args.input)

