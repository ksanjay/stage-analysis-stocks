Sure! Here's a detailed README content for the stock stage analysis program:

---

# Stock Stage Analysis Program

This program analyzes the stage of a given stock using Stan Weinstein's Stage Analysis model. It identifies which stage the stock is currently in and calculates the duration it has been in that stage.

## Overview

The Stan Weinstein Stage Analysis model categorizes stocks into four stages based on their price behavior relative to moving averages:

1. **Stage 1 (Basing Phase):** The stock is moving sideways, consolidating after a downtrend.
2. **Stage 2 (Advancing Phase):** The stock is trending upwards.
3. **Stage 3 (Top Area):** The stock is peaking and starting to move sideways again.
4. **Stage 4 (Declining Phase):** The stock is trending downwards.

This program fetches historical stock data, calculates the 50-day and 200-day moving averages, identifies the current stage, and determines how long the stock has been in that stage.

## Requirements

- Python 3.6+
- `yfinance` library
- `pandas` library
- `numpy` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-stage-analysis.git
   cd stock-stage-analysis
   ```

2. Install the required libraries:
   ```bash
   pip install yfinance pandas numpy
   ```

## Usage

1. Run the program:
   ```bash
   python analyze_stock.py
   ```

2. Enter the stock ticker when prompted (e.g., `AMZN` for Amazon).

3. The program will output the current stage of the stock and the duration it has been in that stage.

## Example

```bash
Enter stock ticker: AMZN
Ticker: AMZN
Current Stage: 2
Duration in Current Stage (days): 150
```

## Code Explanation

### `get_stock_data(ticker)`

Fetches historical stock data for the given ticker using the `yfinance` library.

### `calculate_moving_average(df, window)`

Calculates the moving average of the stock's closing price over the specified window (e.g., 50 days, 200 days).

### `identify_stage(df)`

Identifies the current stage of the stock based on the closing price, 50-day moving average, and 200-day moving average.

### `analyze_stock(ticker)`

Analyzes the stock for its current stage and the duration in that stage. Outputs the results.

## Customization

You can customize the program by modifying the conditions for each stage in the `identify_stage` function. The current implementation uses simplified conditions focusing on moving averages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the Apache License. 

## Contact

If you have any questions or suggestions, feel free to open an issue or contact the author.
