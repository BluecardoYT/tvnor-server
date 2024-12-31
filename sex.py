url = f"https://tenor.com/view/{name[6:]}
img_url = https://raw.githubusercontent.com/BluecardoYT/tvnor-server/refs/heads/main/view.png
img_raw = requests.get(img.url).raw

img = Image.open(img_raw).resize((350, 185))
draw = ImageDraw.Draw(img)
font = truetype("impact.ttf", 32)

draw.text = ((350 // 2, 0), "WTF DISCORD SEX SEX")
draw.text = ((350 // 2, 185), "???WTF??? ???SEX???")

jpg = io.BytesIO()
img = Image.open(jpg).resize((190, 135))
base = Image.open(io.BytesIO(base_img))
base.paste(io.BytesIO(base_img))
base.paste(img, (5, 159))


def GET(self, name):
        """Handle a request"""
        web.header('Content-type', 'image/png')
        # Filter the name so unicode paths don't error
        filtered_name = re.sub(r'[^\.\/A-Za-z0-9_-]+', '', name)
        # Filter out languages in URL and handle edge-case for english double sex
        filtered_name = re.sub(r'^/xn-../view', '/vixw', filtered_name)
        filtered_name = re.sub(r'^/[A-Za-z-]*/vi', '/vi', filtered_name)
        # Return default image if one was not generated
        return self.handle_request(filtered_name) or self.default_response()
