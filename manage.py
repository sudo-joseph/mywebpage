#!/usr/bin/env python3

__author__ = 'Joseph Reid'

import utils
import sys

def main():
    """
    main() - Main Loop for manage.py.
    """

    if sys.argv[1] == "build":
        print("Building...")
        utils.build()
        print("Build Complete.")
    elif sys.argv[1] == "new":
        if len(sys.argv) == 3:
            if sys.argv[2] == 'blog':
                print("Generating new blog post")
                utils.gen_new_post("blog")
                print("Page Generated")
            elif sys.argv[2] == 'project':
                print("Generating new project post")
                utils.gen_new_post("projects")
                print("Page Generated")
            else:
                print("Unknown Page Type")
                helper()
        else:
            print("Generating new blog post")
            utils.gen_new_post("blog")
            print("Page Generated")
    else:
        print("Please specify ’build’ or ’new’")

def helper():
    """
    helper()

    Prints help message explaining correct manage.py usage.
    """
    help_msg = """
        Usage:
            Rebuild site: python3 manage.py build

            Create new page: python3 manage.py new {type}
                {type} - optional argument for page type (blog or projects),
                defaults to blog.

        """
    print(help_msg)

if __name__ == "__main__" and len(sys.argv)>1:
    main()
else:
    helper()
