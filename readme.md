# FileExplorer++ v1.1
```
usage: File Explorer ++ [-h] [-v] -i INPUT [-o OUTPUT] {shrink} ...

        If you're reading this, YOU'VE BEEN HAX!

        Install Requirements:
                pip install -r requirements.txt

        How to use:
                python fepp.py --input 'path_to_image.png' --output '_' shrink --size 64 64

        File Explorer ++ can currently shrink a single file of your choosing to any size smaller than that, but can also batch this operation! Have a directory that has a mix of text files, zip files, exe, etc? No worries, this supports batch processesing for all JPEGs & PNGs & will skip any other files (will test for other formats later)

        The roadmap consists of:
                - Full resizing features
                - Image Sorter by Color Space
                - Toggle if you want to save all changes into its own directory
                - While using a specific output name, iterate if a folder input was selected

        Enjoy until the next update! ^^

positional arguments:
  {shrink}
    shrink              shrink images

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Show program's version number and exit.
  -i INPUT, --input INPUT
                        designate the input file, or folder. If folder is chosen, FEPP will process all of the JPEGs & PNGs in that folder.
  -o OUTPUT, --output OUTPUT
                        designate the output file. Use "_" to output image_name + _shrink
```