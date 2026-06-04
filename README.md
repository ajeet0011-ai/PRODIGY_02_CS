# Image Encryption and Decryption Tool

This Python project implements a simple image encryption and decryption tool using pixel manipulation techniques. The program uses the XOR operation on image pixel values to transform an image into an encrypted version and restore it back to its original form using the same encryption key.

## Features
- Encrypt image files using pixel-level XOR manipulation.
- Decrypt encrypted images using the same key.
- Supports RGB, RGBA, and grayscale images.
- User-friendly command-line interface.
- Lightweight implementation using Python and Pillow.

## Technologies Used
- Python 3
- Pillow (PIL)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python image_encryption_tool.py
```

1. Choose encrypt or decrypt mode.
2. Enter the image path.
3. Enter an encryption key (0–255).
4. The processed image will be saved automatically.

## How It Works

The tool applies an XOR operation between each pixel value and a user-provided key. Since XOR is reversible, applying the same key again decrypts the image and recovers the original image.

## License

This project is open-source and available for educational purposes.
