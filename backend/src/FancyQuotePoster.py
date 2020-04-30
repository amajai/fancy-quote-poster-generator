from PIL import Image, ImageFont, ImageDraw
import os


class FancyQuotePoster:
    def __init__(
        self, bg, base_size=(1200, 1200), img_name='img.png'
    ):
        self.bg = Image.open(bg).resize(base_size)
        self.add_to_bg = ImageDraw.Draw(self.bg)
        self.base_size = base_size
        self.max_width, self.max_height = base_size
        self.img_name = img_name
        self.bg.save(self.img_name)

    def add_bg_filter(self, rgb, opacity=180):
        r, g, b = rgb
        bg_filter = Image.new('RGBA', self.base_size, (r, g, b, opacity))
        self.bg.paste(bg_filter, (0, 0), bg_filter.convert('RGBA'))
        self.bg.save(self.img_name)

    def add_bg_text_model(self, size=(750, 750), rgb=(255, 255, 255), opacity=200, position=(0, 0), frame=False):
        r, g, b = rgb
        x, y = position
        bg_text = Image.new('RGBA', size, (r, g, b, opacity))
        width, height = bg_text.size
        cw = (self.max_width - width)//2 + x
        ch = (self.max_height - height)//2 + y
        self.bg.paste(bg_text, (cw, ch), bg_text)
        if frame:
            self.add_to_bg.rectangle(
                [(30, 30), (1170, 1065)], outline='white', width=12)
            self.add_to_bg.rectangle([(30, 1065), (1170, 1120)], fill='white')
        self.bg.save(self.img_name)

    def add_text_quote(self, text, position=(0, 0), min_text_height=353, max_text_width=700, base_text_size=100, font_style='PlayfairDisplay.ttf', align='center', position_reset=False):
        text_height_is_big = True
        x, y = position
        while text_height_is_big:
            lines = []
            font = ImageFont.truetype(os.path.join(
                'fonts', font_style), base_text_size)
            if font.getsize(text)[0] <= max_text_width:
                lines.append(text)
            else:
                words = text.split(' ')
                i = 0
                while i < len(words):
                    line = ''
                    while i < len(words) and font.getsize(line + words[i])[0] <= max_text_width:
                        line = line + words[i] + " "
                        i += 1
                    if not line:
                        line = words[i]
                        i += 1
                    lines.append(line)
            if self.add_to_bg.multiline_textsize('\n'.join(lines), font=font)[1] > min_text_height:
                base_text_size -= 1
            else:
                text_height_is_big = False
        wrappedText = '\n'.join(lines)
        width, height = self.add_to_bg.multiline_textsize(
            wrappedText, font=font)
        cw = (self.max_width - width)//2 + x
        ch = (self.max_height - height)//2 + y
        if position_reset:
            self.add_to_bg.text((x, y), wrappedText, fill='black', font=font, align=align)
        else:
           self.add_to_bg.text((cw, ch), wrappedText, fill='black', font=font, align=align)
        self.bg.save(self.img_name)

    def add_text_quote_source(self, source_text, font_style='DejaVuSans.ttf', base_text_size=50, position=(0, 0), max_text_width=650, position_reset=False):
        text_width_is_wide = True
        while text_width_is_wide:
            font = ImageFont.truetype(os.path.join(
                'fonts', font_style), base_text_size)
            if font.getsize(source_text)[0] <= max_text_width:
                text_width_is_wide = False
            else:
                base_text_size -= 1
        width, height = self.add_to_bg.textsize(source_text, font=font)
        x, y = position
        cw = (self.max_width - width)//2 + x
        ch = (self.max_height - height)//2 + y
        if position_reset:
            self.add_to_bg.text((x, y), source_text,fill='black', font=font, align='center')
        else:
            self.add_to_bg.text((cw, ch), source_text,fill='black', font=font, align='center')
        self.bg.save(self.img_name)

    def add_text_quote_owner(self, quote_text, font_style='PlayfairDisplay.ttf', base_text_size=50, position=(0, 0), position_reset=False):
        font = ImageFont.truetype(os.path.join('fonts', font_style), base_text_size)
        width, height = self.add_to_bg.textsize(quote_text, font=font)
        x, y = position
        cw = (self.max_width - width)//2 + x
        ch = (self.max_height - height)//2 + y
        if position_reset:
            self.add_to_bg.text((x, y), quote_text, fill='black', font=font)
        else:
            self.add_to_bg.text((cw, ch), quote_text, fill='black', font=font)
        self.bg.save(self.img_name)

    def add_logo(self, logo_file_name, position=(0, 0), resize=(120, 120)):
        add_logo = Image.open(logo_file_name).resize(resize, Image.ANTIALIAS)
        width, height = add_logo.size
        x, y = position
        cw = (self.max_width - width)//2 + x
        ch = (self.max_height - height)//2 + y
        self.bg.paste(add_logo, (cw, ch), add_logo.convert('RGBA'))
        self.bg.save(self.img_name)

    def add_social_profile(self, social_icon, profile_link, font_style='DejaVuSans.ttf', base_text_size=50, icon_position=(60, 60), text_position=(60, 0)):
        if social_icon != None:
            add_social_icon = Image.open(social_icon).resize((60, 60))
            self.bg.paste(add_social_icon, icon_position,
                          add_social_icon.convert('RGBA'))
            x1, y1 = icon_position
        x2, y2 = text_position
        font = ImageFont.truetype(os.path.join(
            'fonts', font_style), base_text_size)
        if social_icon == None:
            x1, y1 = (0, 0)
        self.add_to_bg.text((x1+x2, y1+y2), profile_link, font=font)
        self.bg.save(self.img_name)

    def add_website(self, domain, font_style='DejaVuSans.ttf', base_text_size=50, icon_position=(60, 60), text_position=(0, 0)):
        font = ImageFont.truetype(os.path.join('fonts', font_style), base_text_size)
        width, height = self.add_to_bg.textsize(domain, font=font)
        x, y = text_position
        cw = (self.max_width - width)//2 + x
        ch = (self.max_height - height)//2 + y
        self.add_to_bg.text((cw, ch), domain, font=font)
        self.bg.save(self.img_name)
