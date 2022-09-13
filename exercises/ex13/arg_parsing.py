import argparse


parser = argparse.ArgumentParser()
   
parser.add_argument('-n', type=str, default='Larry', help='first name')
parser.add_argument('-l', type=str, default='Hanson', help='last name')
parser.add_argument('-a', type=int, default='100', help='age')
parser.add_argument('--f', action='store_true', help='initial position')

args = parser.parse_args()

if args.f:
    print('Hello', args.n , args.l,'I see that you have had', args.a + 1,'birthdays','\n''Fast mode enabled')
else:
    print('Hello', args.n , args.l,'I see that you have had', args.a + 1, 'birthdays')
