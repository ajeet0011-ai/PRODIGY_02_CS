from PIL import Image
import os

def encrypt_decrypt_image(input_image, output_image, key):
    try:
        img = Image.open(input_image)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]

                if isinstance(pixel, int):  # Grayscale image
                    pixels[x, y] = pixel ^ key
                else:  # RGB image
                    r, g, b = pixel[:3]

                    r ^= key
                    g ^= key
                    b ^= key

                    if len(pixel) == 4:  # RGBA image
                        a = pixel[3]
                        pixels[x, y] = (r, g, b, a)
                    else:
                        pixels[x, y] = (r, g, b)

        img.save(output_image)
        print(f"Operation completed successfully!")
        print(f"Output saved as: {output_image}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    print("=== Image Encryption Tool ===")

    choice = input("Type 'encrypt' or 'decrypt': ").lower()

    input_image = input("Enter image path: ")
    key = int(input("Enter encryption key (0-255): "))

    if choice == "encrypt":
        output_image = "encrypted_image.png"
    elif choice == "decrypt":
        output_image = "decrypted_image.png"
    else:
        print("Invalid choice!")
        return

    encrypt_decrypt_image(input_image, output_image, key)


if __name__ == "__main__":
    main()
