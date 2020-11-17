import argparse
import itertools




def main(in_data):


    print('things')




if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='''vis tool''',  epilog="""Version 0.1""")

    parser.add_argument('--input', type=str, help='Input file')

    args = parser.parse_args()

    main(args.input)

