import io
class G:
    def __init__(self):
        self.s = io.open('parent-guide-week-25.html', encoding='utf-8').read()
    def between(self, start, end, new):
        s = self.s; i = s.index(start); j = s.index(end, i + len(start)); self.s = s[:i] + new + s[j:]
    def sec(self, head_text, new_inner):
        s = self.s; k = s.index(head_text); i = s.rindex('<section', 0, k); i = s.index('>', i) + 1; j = s.index('</section>', k)
        self.s = s[:i] + new_inner + s[j:]
    def rows(self, rows):
        s = self.s; i = s.index('        <tr>\n          <td class="day-n">25.1'); j = s.index('        <tr class="extra-row">', i)
        self.s = s[:i] + rows + s[j:]
