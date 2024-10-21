# Web Scraper

>This project is a simple web scraper that extracts product details from e-commerce websites, such as the product name, ASIN (Amazon Standard Identification Number), price, and availability. It uses `Streamlit` for a web-based interface, allowing users to enter a URL and retrieve the product details by clicking a button.

## Features
- Scrapes product details like title, availability, price, buy box holder, MRP, shipping charge, and fulfillment type (FBA/MFN).
- Detects special deals like Deal of the Day (DOTD) and Lightning Deals (LD).
- Uses `Streamlit` for easy-to-use web interface.
- Displays extracted data in real-time after the user inputs the product URL.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/web-scraper.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd web-scraper
    ```

3. **Install dependencies:**
    This project requires `Streamlit`, `BeautifulSoup`, and `requests`. Install them using:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Enter the product URL** in the text box provided on the web page.

3. **Click the "Get Data" button** to fetch product details. If the URL is valid, the details will be displayed on the page. Otherwise, an error message will be shown.

### Sample Output
For a valid URL, the following details will be displayed:
- Product Name
- ASIN
- Price
- Availability
- Buy Box Holder
- MRP
- Shipping Charge
- Fulfillment (FBA/MFN)
- Deal of the Day (DOTD)
- Lightning Deal (LD)

## Dependencies
- `Streamlit`: For building the web interface.
- `BeautifulSoup`: For web scraping and parsing HTML.
- `Requests`: For making HTTP requests.

Install the dependencies using the provided `requirements.txt`.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
