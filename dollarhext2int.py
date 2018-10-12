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
                    result = self.convert_hex(isHex[0])
                    statusline.append('{} = {}'.format(isHex[0], result)+"  ")

        view.erase_status('Hexcode')
        view.set_status('Hexcode', '{}'.format(", ".join(statusline)))

    def convert_hex(self, s):
        i = int(s.replace('$', '0x'), 16)
        b = bin(i).replace("0b", "")
        result = "#" + str(i) + "  |  " + "%" + str(b)
        return result
