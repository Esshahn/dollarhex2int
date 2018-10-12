# https://github.com/unknownuser88/hex2int
# based on hex2int by unknownuser88
# To make this work the word separators in Sublime Text need to be adjusted
# In your settings, change
# "word_separators": "./\\()\"'-:,.;<>~!@#$%^&*|+=[]{}`~?" to
# "word_separators": "./\\()\"'-:,.;<>~!@#%^&*|+=[]{}`~?"


import sublime_plugin
import re


class HtointCommand(sublime_plugin.EventListener):
    def on_new(self, view):
        self.run(view)

    def on_selection_modified(self, view):
        self.run(view)

    def on_activated(self, view):
        self.run(view)

    def run(self, view):
        statusline = []
        for region in view.sel():
            if region.begin() == region.end():
                word = view.word(region)
            else:
                word = region

            if not word.empty():

                keyword = view.substr(word)
                isHex = re.findall(r'\$[0-9a-fA-F]+', keyword)

                if isHex:
                    abc = self.str_to_int(isHex[0].replace('$', '0x'))
                    statusline.append('{} = #{}'.format(isHex[0], abc)+"  ")

        view.erase_status('Hexcode')
        view.set_status('Hexcode', '{}'.format(", ".join(statusline)))

    def str_to_int(self, s):
        i = int(s, 16)
        if i >= 2**23:
            i -= 2**24
        return i
