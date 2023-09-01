"""Brief description of what the script does."""

import argparse
import pandas as pd

def generate_plot(infile,outfile):
    df = pd.read_csv(infile, header=None,
                    names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                        method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency',
                            y='inverse_rank',
                            figsize=[12, 6],
                            grid=True)
    fig = scatplot.get_figure()
    fig.savefig(outfile)

def main(args):
    """Run the program."""
    generate_plot(args.infile,args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Word count csv file name')
    parser.add_argument('--outfile', type=str,
                        default='plotcounts.png',
                        help='Output image file name')
    parser.add_argument('--xlim', type=float, nargs=2,
                        metavar=('XMIN', 'XMAX'),
                        default=None, help='X-axis limits')
    args = parser.parse_args()
    main(args)