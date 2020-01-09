#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import subprocess
import colorama




result = subprocess.run(['git', 'for-each-ref', '--sort=creatordate', '--format', "---<begin>--- ---<tag_date>--- %(creatordate:relative) /---<tag_date>--- ---<tag_name>--- %(refname:strip=2) /---<tag_name>--- ---<tag_author>--- %(creator) /---<tag_author>--- ---<commit_subject>--- %(subject) /---<commit_subject>--- ---<commit_author>--- %(authorname) /---<commit_author>--- ---<commit_date>--- %(authordate:relative) /---<commit_date>--- ---<end>---", 'refs/tags'], stdout=subprocess.PIPE)


class git_tag():

    """Docstring for git_tag. """

    def __init__(self, string):
        """TODO: to be defined1.

        :param tag_date: TODO
        :param tag_name: TODO
        :param tag_author: TODO
        :param commit_subject: TODO
        :param commit_author: TODO
        :param commit_date: TODO

        """

        def find(mark):
            pattern = "---<{}>--- (.*) /---<{}>---".format(mark,mark)
            return re.search(pattern, string).group(1)
        self.tag_date = find("tag_date")
        self.tag_name = find("tag_name")
        self.tag_author = find("tag_author").split(' <')[0]
        self.commit_subject = find("commit_subject")
        self.commit_author = find("commit_author")
        self.commit_date = find("commit_date")

    def __str__(self):
        return (
(colorama.Fore.BLUE + self.tag_date + colorama.Style.RESET_ALL).ljust(25)
+(colorama.Back.WHITE + colorama.Fore.RED + self.tag_name + colorama.Style.RESET_ALL).ljust(40)
+(colorama.Fore.WHITE + self.tag_author + colorama.Style.RESET_ALL).ljust(35)
+(colorama.Fore.GREEN + self.commit_subject.ljust(70)[:70].ljust(71) + colorama.Style.RESET_ALL)
+(colorama.Fore.RED + self.commit_author + colorama.Style.RESET_ALL).ljust(35)
+(colorama.Fore.CYAN + self.commit_date).rjust(25)
                )


inp = result.stdout.decode('utf-8')
for entry in re.finditer("---<begin>--- (.*) ---<end>---", inp):
    print(git_tag(entry.group(1)))
