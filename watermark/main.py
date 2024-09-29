import cv2

img = cv2.imread(r'C:\Users\vampi\Desktop\pycharm_project\github\watermark\img.png')

height, width = img.shape[:2]
aspect_ratio = width / height

new_width = 500
new_height = int(new_width / aspect_ratio)

# Resize the image with aspect ratio in mind for better display
img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
print(img)


img_or_text = input("Will the watermark be an image or text? (img/txt): ")

if img_or_text == 'img':
    wat = input("Enter the path to the watermark image: ")
    watermark = cv2.imread(wat)
    watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))  # Resize watermark to match main image
    result = cv2.addWeighted(img, 1, watermark, 0.3, 0)  # Blend the two images
    cv2.imshow('Watermarked Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif img_or_text == 'txt':
    text = input("Enter the text for the watermark: ")
    font_scale = float(input("Enter the font scale\nThis is the size of the text: "))
    color = input("Enter the font color\nOptions are 'red', 'blue', 'green', 'black', and 'white': ")
    
    color_dict = {'red': (0, 0, 255), 'blue': (255, 0, 0), 'green': (0, 255, 0), 'black': (0, 0, 0), 'white': (255, 255, 255)}
    color = color_dict.get(color.lower(), (0, 0, 0)) 
    
    thickness = int(input("Enter the thickness of the text in px: "))
    

    position = input("Enter the position of the text\nOptions are: top-left, top-right, bottom-left, bottom-right, center: ")
    
    if position == 'top-left':
        position = (10, 30)
    elif position == 'top-right':
        position = (img.shape[1] - 200, 30)
    elif position == 'bottom-left':
        position = (10, img.shape[0] - 10)
    elif position == 'bottom-right':
        position = (img.shape[1] - 200, img.shape[0] - 10)
    elif position == 'center':
        position = (img.shape[1] // 2 - 100, img.shape[0] // 2)
    else:
        position = (200, 400) 

    cv2.putText(img, text, position, cv2.FONT_HERSHEY_COMPLEX_SMALL, font_scale, color=color, thickness=thickness)
    cv2.imshow('Watermarked Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
