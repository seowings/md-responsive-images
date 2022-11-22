from responsive_images import ImageExtension
import markdown

input = """
![a remote image](feature-image.webp)
"""

html = markdown.markdown(input, extensions=[ImageExtension()])
print(html)
