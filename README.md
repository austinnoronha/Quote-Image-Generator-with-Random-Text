# Quote Image Generator with Random Text 🚀

## 📓 Overview
Welcome to the Image Generator! 

This Python-based script allows you to create engaging images in square dimensions using random text generated from [Quotable API](https://api.quotable.io/).

The script utilizes popular libraries such as PIL (Pillow), textwrap, and requests.

## 📜 Key Features:
- Random Text from Quotable API: Fetch dynamic and inspiring quotes from [https://api.quotable.io/](Quotable API)
- Easily configurable to customize the appearance of generated images.
- onfiguration via .env: Easily customize your experience with a configuration file.
- Learn the process of generating images with text using the Python Imaging Library (PIL).

## ⚙️ Dependencies
Make sure you have the following dependencies installed:

- Pillow (PIL): ```pip install Pillow```
- Requests: ```pip install requests```

## 🐺 How to Use

Clone the repository:
```bash
git clone https://github.com/austinnoronha/insta_gen_bot.git
```

Navigate to the project directory:
```bash
cd insta_gen_bot
```

Run the script:
```bash
python main.py
```

## Customize the script by modifying the configuration parameters.

### Configuration
You can easily customize the script by adjusting the following parameters in ```.env```:

- IMAGE_SIZE: Set the size of the generated image.
- FONT_SIZE: Adjust the font size of the text.
- QUOTE_GEN_API: Change the URL for fetching random quotes.
- FONT_TYPE: Choose from the set of fonts in the ```/font``` folder
- BG_COLOR_SET: A list having background colors tuples
- TEXT_COLOR_SET: A list having text colors tuples

```the BG_COLOR_SET and TEXT_COLOR_SET set should have equal no.of sets, as it chooses a random int index to choose the color tuple for RGB```

# Example

<div class="Box-sc-g0xbh4-0 iIZCet"><img alt="quote.png" src="https://github.com/austinnoronha/insta_gen_bot/blob/development/quote.png?raw=true" data-hpc="true" class="Box-sc-g0xbh4-0 kzRgrI"></div>


# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
- Thanks to the [https://api.quotable.io/](https://api.quotable.io/) for providing inspirational quotes.
- Feel free to explore, modify, and share your generated Instagram posts! If you encounter any issues or have suggestions, feel free to open an issue or contribute to the project. Happy coding!