import argparse
import os

def IsImage(img):
    ext = img.split('.')[1]

    if ext == "png" or ext == "jpg":
        return True
    else:
        return False

def Shrink(file, size):
    '''
    This will shrink your input file, but can't grow it.
    '''
    from PIL import Image
    from resizeimage import resizeimage

    with open(file[0], 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, size)
            cover.save(file[1], image.format)
            print(f"SAVED {file[1]} as {image.format}")

def main(command_line=None):
    parser = argparse.ArgumentParser('File Explorer ++',description=
    "\n\n\tIf you're reading this, YOU'VE BEEN HAX!"
    +"\n\n\tInstall Requirements:"
    +"\n\t\tpip install -r requirements.txt"
    +"\n\n\tHow to use:"
    +"\n\t\tpython fepp.py --input 'path_to_image.png' --output '_' shrink --size 64 64"
    +"\n\n\tFile Explorer ++ can currently shrink a single file of your choosing to any size smaller than that, but can also batch this operation! "
    +"Have a directory that has a mix of text files, zip files, exe, etc? No worries, this supports batch processesing for all JPEGs & PNGs & will skip any other files (will test for other formats later)"
    +"\n\n\tThe roadmap consists of:"
    +"\n\t\t- Full resizing features"
    +"\n\t\t- Image Sorter by Color Space"
    +"\n\t\t- Toggle if you want to save all changes into its own directory"
    +"\n\t\t- While using a specific output name, iterate if a folder input was selected"
    +"\n\n\tEnjoy until the next update! ^^"
    ,formatter_class=argparse.RawTextHelpFormatter)#, add_help=False)

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.1', help="Show program's version number and exit.")
    # parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='This script can')
    parser.add_argument('-i', '--input', required=True, type=str, help='designate the input file, or folder. If folder is chosen, FEPP will process all of the JPEGs & PNGs in that folder.')
    parser.add_argument('-o', '--output', default=None, type=str, help='designate the output file. Use "_" to output image_name + _shrink')

    subprasers = parser.add_subparsers(dest='command')
 
    shrink = subprasers.add_parser('shrink', help='shrink images')
    shrink.add_argument('--size', type=int, nargs='+', default=256, help='what size you want to shrink the input to')
 
    # praise = subprasers.add_parser('praise', help='praise someone')
    # praise.add_argument('name', help='name of person to praise')
    # praise.add_argument('reason', help='what to praise for (optional)', default="no reason", nargs='?')
 
    args = parser.parse_args(command_line)

    inp = args.input
    files = []
    location = ''

    folder = False
    
    # 
    if os.path.isdir(inp):
        folder = True

    print("FOLDER DETECTED!" if folder else "FILE DECTECTED!")

    # 
    if folder:
        location = inp
        files = [i for i in os.listdir(inp) if not os.path.isdir(os.path.join(location, i)) and IsImage(os.path.join(location, i)) ]
    else:
        location = './'
        files.append(inp)

    # 
    if args.command == 'shrink':
        size = args.size

        # 
        if len(size) == 1:
            size.append(size[0])

        # 
        for f in files:
            out = args.output
    
            if out == '_':
                out = f.split('.')[0] + "_shrunk." + f.split('.')[1]
            elif out == None:
                out = f

            # 
            Shrink([os.path.join(location, f), os.path.join(location, out)], size)

    elif args.command == 'praise':
        print('praising ' + args.name + ' for ' + args.reason)

if __name__ == '__main__':
    main()