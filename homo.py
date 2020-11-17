
from library import unicodes
import argparse

def logo():
    logo = '''                                                                      
    HHHHHHHHH     HHHHHHHHH                                                          
    H:::::::H     H:::::::H                                                          
    H:::::::H     H:::::::H                                                          
    HH::::::H     H::::::HH                                                          
      H:::::H     H:::::H     ooooooooooo      mmmmmmm    mmmmmmm      ooooooooooo   
      H:::::H     H:::::H   oo:::::::::::oo  mm:::::::m  m:::::::mm  oo:::::::::::oo 
      H::::::HHHHH::::::H  o:::::::::::::::om::::::::::mm::::::::::mo:::::::::::::::o
      H:::::::::::::::::H  o:::::ooooo:::::om::::::::::::::::::::::mo:::::ooooo:::::o
      H:::::::::::::::::H  o::::o  b  o::::om:::::mmm::::::mmm:::::mo::::o     o::::o
      H::::::HHHHH::::::H  o::::o  e  o::::om::::m   m::::m   m::::mo::::o     o::::o
      H:::::H     H:::::H  o::::o  t  o::::om::::m   m::::m   m::::mo::::o v1  o::::o
      H:::::H     H:::::H  o::::o  a  o::::om::::m   m::::m   m::::mo::::o     o::::o
    HH::::::H     H::::::HHo:::::ooooo:::::om::::m   m::::m   m::::mo:::::ooooo:::::o
    H:::::::H     H:::::::Ho:::::::::::::::om::::m   m::::m   m::::mo:::::::::::::::o
    H:::::::H     H:::::::H oo:::::::::::oo m::::m   m::::m   m::::m oo:::::::::::oo 
    HHHHHHHHH     HHHHHHHHH   ooooooooooo   mmmmmm   mmmmmm   mmmmmm   ooooooooooo   
    [Homo]graph  
'''
    print(logo)


if __name__ == '__main__':
    logo()
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    group_domain = parser.add_argument_group('domain')
    group_domain.add_argument('-d', '--domain', type=str, help='Generates domain variations')
    group_domain.add_argument('-v', '--all_domain', action='store_true', help='Show all domains variations')
    group_domain.add_argument('-rd', '--random_domain', type=int, help='Random domain homograph', default=1)

    args = parser.parse_args()

    try:
        if args.domain:
            unicodes = unicodes.Unicodes(args.domain, args.all_domain)
            unicodes.gen()

        if args.random_domain:
            unicodes.random_domain(n=args.random_domain)

    except Exception as msg:
        parser.error(str(msg))




