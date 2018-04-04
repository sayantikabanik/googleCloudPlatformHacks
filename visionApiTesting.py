import  io
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from google.cloud import vision
from urllib import urlopen
from google.cloud.vision import types
from google.cloud import vision
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def detect_document_uri(uri):
    """Detects document features in the file located in Google Cloud
    Storage."""
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    

    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            

            if( symbol.text=='_' or symbol.text=='8' or symbol.text=='0' or symbol.text=='r' ):
            	print('{}'.format(block_text))

	            
            '''if( symbol.text=='r'):	
	            pattern = Image.open("DANK.jpg", "r").convert('RGBA')
	            size = width, height = pattern.size
				draw = ImageDraw.Draw(pattern,'RGBA')
				font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 100)

				draw.text((300,10), "Hello World", (0, 0, 0, 0),font=font)
				pattern.save('sample-out.jpg')	'''
	            	
	            
         
            print('sysmbol',symbol.text)
          
            

if __name__ == '__main__':
    detect_document_uri('gs://botofficer/mandatesign.jpeg')
    #detect_document_uri('mandate.jpeg')
