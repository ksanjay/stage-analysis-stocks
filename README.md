Stock Stage Analysis Program

This program analyzes the stage of a given stock using Stan Weinstein’s Stage Analysis model. It identifies which stage the stock is currently in and calculates the duration it has been in that stage.

Overview

The Stan Weinstein Stage Analysis model categorizes stocks into four stages based on their price behavior relative to moving averages:

	1.	Stage 1 (Basing Phase): The stock is moving sideways, consolidating after a downtrend.
	2.	Stage 2 (Advancing Phase): The stock is trending upwards.
	3.	Stage 3 (Top Area): The stock is peaking and starting to move sideways again.
	4.	Stage 4 (Declining Phase): The stock is trending downwards.

This program fetches historical stock data, calculates the 50-day and 200-day moving averages, identifies the current stage, and determines how long the stock has been in that stage.

Requirements

	•	Python 3.6+
	•	yfinance library
