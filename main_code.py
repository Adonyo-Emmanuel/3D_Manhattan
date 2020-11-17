import argparse
import itertools
import pickle
from testing_code import *


def main(in_data):

    infile = open('GWAS_data.pickle', 'rb')

    test_data = pickle.load(infile)

    print(test_data)

    plot_fig = ManhattanPlot(test_data, gene=None)

    plot_fig.show()




if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='''vis tool''',  epilog="""Version 0.1""")

    parser.add_argument('--input', type=str, help='Input file')

    args = parser.parse_args()

    main(args.input)

