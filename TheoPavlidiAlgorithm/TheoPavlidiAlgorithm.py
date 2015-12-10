from PIL import Image
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(260,210))
        self.SetBackgroundColour('gray')

        self.panel = wx.Panel(self, wx.ID_ANY)

        first_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        first_textbox_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.topSizer = wx.BoxSizer(wx.VERTICAL)

        #Setup First Text
        first_text = wx.StaticText(self.panel, wx.ID_ANY, 'Theo Pavlidi Algorithm')
        first_text_sizer.Add(first_text)

        #Setup First Text Box
        self.first_text_box = wx.TextCtrl(self.panel, -1, size=(220, 100), style=wx.TE_MULTILINE)
        first_textbox_sizer.Add(self.first_text_box , wx.ALL|wx.EXPAND, 5)

        #Setup Make Make Button
        self.make_thumbnail_button = wx.Button(self.panel, wx.ID_ANY, 'Do the Algorithm')
        self.make_thumbnail_button.Bind(wx.EVT_BUTTON, self.execute_algorithm)
        btn_sizer.Add(self.make_thumbnail_button, 0, wx.ALL, 5)

        self.topSizer.Add(first_text_sizer, 0, wx.CENTER, 5)
        self.topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        self.topSizer.Add(first_textbox_sizer, 0, wx.CENTER, 5)
        self.topSizer.Add(btn_sizer, 0, wx.ALL|wx.CENTER, 5)


        self.panel.SetSizer(self.topSizer)
        self.Show(True)

    def execute_algorithm(self, event):
        raw_data = self.first_text_box.GetValue()
        size = self.get_size(raw_data)
        structured_data = raw_data.split('\n')
        for i in range(0, size):
            structured_data[i] = structured_data[i].split(',')

        modified_data = [[0 for i in range(size)] for j in range(size)]
        print modified_data
        pos_x = 1
        pos_y = 2
        modified_data[1][1] = 1
        while(1):
            try:
                p1 = int(structured_data[pos_y][pos_x-1])
                p2 = int(structured_data[pos_y][pos_x])
                p3 = int(structured_data[pos_y][pos_x+1])
                print p1
                print p2
                print p3
                if p2 == 1:
                    if p1 == 1:
                        pos_x -= 1
                        modified_data[pos_y][pos_x] = 1
                    elif p3 == 1:
                        pos_x += 1
                        modified_data[pos_y][pos_x] = 1
                    else:
                        modified_data[pos_y][pos_x] = 1
                    pos_y += 1
                else:
                    break
            except:
                break

        print modified_data
        self.make_image(structured_data, size, 0)
        self.make_image(modified_data, size, 1)

    def make_image(self, data, size, mode):
        black_pixel = Image.open("black_pixel.png")
        if mode == 1:
            sub_pixel = Image.open("blue_pixel.png")
        else:
            sub_pixel = Image.open("yellow_pixel.png")
        size_in_pixels = size * 25
        final_image = Image.new("RGB", (size_in_pixels, size_in_pixels))
        height = -25
        for i in range(0, size):
            line = data[i]
            width = 0
            height += 25
            for i2 in range(0, size):
                if int(line[i2]) == 0:
                    final_image.paste(black_pixel, (width,height))
                if int(line[i2]) == 1:
                    final_image.paste(sub_pixel, (width,height))
                width += 25

        if mode == 1:
            final_image.save("final.png","PNG")
        else:
            final_image.save("start.png", "PNG")

    def get_size(self, raw_data):
        number_of_lines = len(raw_data.split('\n'))
        print number_of_lines
        return number_of_lines

app = wx.App(False)
frame = MyFrame(None, 'Theo Pavlidi Algorithm')
app.MainLoop()