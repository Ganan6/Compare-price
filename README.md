# Grocery Price Comparison using Distance Metrics

This project analyzes and compares real-world grocery prices using two distance-based methods: Manhattan distance and Euclidean distance. The objective is to determine price trends or classify the pricing of groceries from different stores or time periods based on the price of new items.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Distance Methods](#distance-methods)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Overview
The project is designed to analyze grocery prices and compare them using distance metrics:
- **Manhattan Distance**: Sum of absolute differences in prices between two sets of groceries.
- **Euclidean Distance**: Straight-line distance calculated between the price points of groceries using the square root of the sum of squared differences.

The comparison helps identify which store or dataset (historical or real-time) is more closely aligned with a given new set of grocery prices.

## Technologies Used
- Python 3.x
- Matplotlib

## Distance Methods

### Manhattan Distance
The Manhattan distance metric calculates the absolute differences between the prices of grocery items. It is particularly useful for identifying large price gaps in individual items.

### Euclidean Distance
The Euclidean distance calculates the square root of the sum of the squared differences between item prices, providing a more direct comparison between two price sets.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/grocery-price-comparison.git
