# Stock Search and Chart Visualization

## Project Description
This project is a web application that allows users to search for stock information and visualize stock price data over a specified date range. Users can view stock closing prices, percentage changes, and 50-day moving averages through interactive charts and data tables.

The application is built using Python and leverages the following libraries:
- **Streamlit**: For creating the web interface.
- **yfinance**: For fetching stock data from Yahoo Finance.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating visualizations.

---

## Features

1. **Stock Search**:
   - Users can input a stock ticker (e.g., AAPL, TSLA) to search for stock data.

2. **Date Range Selection**:
   - Users can select the start and end dates for the data they wish to analyze.

3. **Interactive Tabs**:
   - **Price Chart**: Displays the closing price of the stock within the selected date range.
   - **Statistics**: Shows percentage changes, 50-day moving averages, and a summary of the last 10 days.

4. **Dynamic Visualizations**:
   - Line charts for closing prices and moving averages.

5. **Error Handling**:
   - Alerts users if no data is available for the selected date range or if an invalid stock ticker is entered.

---

## Installation

### Prerequisites
- Python 3.8 or higher installed on your system.

### Required Libraries
Install the necessary libraries using `pip`:

```bash
pip install streamlit yfinance pandas matplotlib
```

---

## How to Run the Application

1. Clone this repository to your local machine.

2. Navigate to the project directory:
   ```bash
   cd path/to/project
   ```

3. Run the application:
   ```bash
   streamlit run stock_app.py
   ```

4. Open the URL provided by Streamlit (typically `http://localhost:8501`) in your web browser.

---

## File Structure

```
Stock Search Project
├── stock_app.py         # Main application file
├── requirements.txt     # List of required libraries (optional)
└── README.md            # Project documentation
```

---

## Usage

1. **Input Stock Ticker**:
   - Enter a valid stock ticker symbol (e.g., `AAPL`, `GOOG`).

2. **Select Date Range**:
   - Choose the desired start and end dates for the stock data.

3. **View Results**:
   - Explore the "Price Chart" tab for closing prices.
   - Check the "Statistics" tab for data insights such as percentage changes and moving averages.

---

## Example

- Searching for Apple Inc. (`AAPL`) stock data from `2023-01-01` to `2023-12-01` will display:
  - A line chart of the closing prices.
  - A table with percentage changes and 50-day moving averages.

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests for new features or bug fixes.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements
- **Yahoo Finance** for providing stock data.
- **Streamlit** for the easy-to-use web framework.
- **Matplotlib** and **Pandas** for their powerful data visualization and manipulation tools.

---

## Contact
For any inquiries or issues, please contact [Your Email Address].

