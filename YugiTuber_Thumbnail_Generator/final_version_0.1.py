from PIL import Image
import urllib2
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(260,180))
        self.SetBackgroundColour('gray')

        self.panel = wx.Panel(self, wx.ID_ANY)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        first_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        second_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        first_textbox_sizer = wx.BoxSizer(wx.HORIZONTAL)
        second_textbox_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #Setup First Text
        first_text = wx.StaticText(self.panel, wx.ID_ANY, 'First Card')
        first_text_sizer.Add(first_text , wx.ALL|wx.EXPAND, 5)

        #Setup Second Text
        second_text = wx.StaticText(self.panel, wx.ID_ANY, 'Second Card')
        second_text_sizer.Add(second_text , wx.ALL|wx.EXPAND, 5)

        #Setup First Textbox
        self.first_text_box = wx.TextCtrl(self.panel, -1, size=(220, -1))
        first_textbox_sizer.Add(self.first_text_box , wx.ALL|wx.EXPAND, 5)

        #Setup Second Textbox
        self.second_text_box = wx.TextCtrl(self.panel, -1, size=(220, -1))
        second_textbox_sizer.Add(self.second_text_box , wx.ALL|wx.EXPAND, 5)

        #Setup Make Thumbnail Button
        self.make_thumbnail_button = wx.Button(self.panel, wx.ID_ANY, 'Make Thumbnail')
        self.make_thumbnail_button.Bind(wx.EVT_BUTTON, self.create_thumbnail)
        btn_sizer.Add(self.make_thumbnail_button, 0, wx.ALL, 5)

        topSizer.Add(first_text_sizer, 0, wx.CENTER, 5)
        topSizer.Add(first_textbox_sizer, 0, wx.CENTER, 5)
        topSizer.Add(second_text_sizer, 0, wx.CENTER, 5)
        topSizer.Add(second_textbox_sizer, 0, wx.CENTER, 5)
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(btn_sizer, 0, wx.ALL|wx.CENTER, 5)

        self.panel.SetSizer(topSizer)
        self.Show(True)

    def create_thumbnail(self, event):
        first_card_name = self.first_text_box.GetValue()
        second_card_name = self.second_text_box.GetValue()
        self.download_card(first_card_name, second_card_name)
        first_card = Image.open("card1.png")
        second_card = Image.open("card2.png")
        line = Image.open("line.png")
        final_image = Image.new("RGB", (450, 225))

        first_image = first_card.crop((40, 80, 265, 305))
        second_image = second_card.crop((40, 80, 265, 305))

        final_image.paste(first_image, (0,0))
        final_image.paste(second_image, (225,0))
        for i in range(0, 5):
            final_image.paste(line, ((202+i), 0), line)

        final_image.save("final.png","PNG")

    def download_card(self, card1, card2):
        card1 = card1.replace(" ", "_")
        card_url = 'http://yugioh.wikia.com/wiki/' + (card1)
        f = urllib2.urlopen(card_url)
        text = f.read()
        text = text.split("image-thumbnail")[1]
        text = text.split("img src=\"")[1]
        text = text.split("alt=")[0]
        text = text.split("/revision")[0]
        img = urllib2.urlopen(text)
        localFile = open('card1.png', 'wb')
        localFile.write(img.read())
        localFile.close()
        card2 = card2.replace(" ", "_")
        card_url = 'http://yugioh.wikia.com/wiki/' + (card2)
        f = urllib2.urlopen(card_url)
        text = f.read()
        text = text.split("image-thumbnail")[1]
        text = text.split("img src=\"")[1]
        text = text.split("alt=")[0]
        text = text.split("/revision")[0]
        img = urllib2.urlopen(text)
        localFile = open('card2.png', 'wb')
        localFile.write(img.read())
        localFile.close()

app = wx.App(False)
frame = MyFrame(None, 'Thumbnail Generator')
app.MainLoop()