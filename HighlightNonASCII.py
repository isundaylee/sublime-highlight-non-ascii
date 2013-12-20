import sublime, sublime_plugin

class HighlightExtendedCharsCommand(sublime_plugin.TextCommand):
  def highlight_regions(self, regions):
    self.view.add_regions('HighlightNonASCIIRegions',
                          regions,
                          'invalid',
                          '',
                          sublime.HIDE_ON_MINIMAP)

  def run(self, edit):
    self.view.erase_regions('HighlightNonASCIIRegions')
    self.highlight_regions(self.view.find_all('[^\x00-\x7F]'))

class UnhighlightExtendedCharsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.erase_regions('HighlightNonASCIIRegions')