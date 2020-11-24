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


    point_1 = {'x': 1081000000, 'y': 8.761}
    point_2 = {'x': 1771000000, 'y': 8.737}

    link_type = "PPI"

    add_line_between_points(plot_fig, point_1, point_2, "Blue")

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

