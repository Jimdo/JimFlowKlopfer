import zbar
import Image
import ImageDraw
import kanban


class Scanner(object):
    def __init__(self, imagepath):
        self.image = Image.open(imagepath).convert('L')
        self.width, self.height = self.image.size
        self.informations = []
        # create a reader
        self.scanner = zbar.ImageScanner()
        # configure the scanner
        self.scanner.parse_config('enable')

    def scan(self):
        pieces_size = int(self.get_qr_code_size() * 2)
        step_size = int(pieces_size / 5)

        y_start = 0

        iy = 0
        while y_start < self.height:
            y_start = iy * step_size
            y_end = y_start + pieces_size
            iy += 1
            ix = 0
            x_start = 0
            while x_start < self.width:
                x_start = ix * step_size
                x_end = x_start + pieces_size
                crop_to = (x_start, y_start, x_end, y_end)
                img_crop = self.image.crop(crop_to)
                self.scan_image(img_crop, x_start, y_start)
                ix += 1
        return self.informations

    def get_qr_code_size(self):
        zbar_img = zbar.Image(self.width, self.height, 'Y800', self.image.tostring())

        qr_sizes = []
        # scan the image for barcodes
        self.scanner.scan(zbar_img)
        for symbol in zbar_img:
            qr_width = symbol.location[3][0] - symbol.location[0][0]
            qr_height = symbol.location[1][1] - symbol.location[0][1]
            qr_sizes.append(qr_width)
            qr_sizes.append(qr_height)

        if len(qr_sizes) == 0:
            raise IOError('Klopfer says: no qr code scanned')

        return sum(qr_sizes, 0.0) / len(qr_sizes)

    def scan_image(self, img_scan, x_start, y_start):
        crop_width, crop_height = img_scan.size
        zbar_img = zbar.Image(crop_width, crop_height, 'Y800', img_scan.tostring())

        # scan the image for barcodes
        self.scanner.scan(zbar_img)

        # Create a draw object
        draw = ImageDraw.Draw(self.image)
        draw_crop = ImageDraw.Draw(img_scan)

        for symbol in zbar_img:
            top_left = (symbol.location[0][0] + x_start, symbol.location[0][1] + y_start)
            bottom_left = (symbol.location[1][0] + x_start, symbol.location[1][1] + y_start)
            bottom_right = (symbol.location[2][0] + x_start, symbol.location[2][1] + y_start)
            top_right = (symbol.location[3][0] + x_start, symbol.location[3][1] + y_start)
            self.informations.append(kanban.Information(symbol.data, (top_left, bottom_left, bottom_right, top_right)))
            draw.rectangle([(top_left), (bottom_right)], fill="black")
            draw_crop.rectangle([symbol.location[0], symbol.location[2]], fill="black")
        if len(zbar_img.symbols) > 0:
            self.scan_image(img_scan, x_start, y_start)
