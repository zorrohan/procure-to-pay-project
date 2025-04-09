# Procure-to-Pay System

## Description

The Procure-to-Pay System is a command-line application that allows users to manage purchase orders, vendor invoices, and goods received. The system provides a structured way to track procurement activities, ensuring a streamlined and organized approach to purchasing and payment processes.

## Features

- **Purchase Order Management**

  - Add new purchase orders with a unique PO number.
  - View all purchase orders.
  - View specific purchase order details.
  - Update items in a purchase order.
  - Delete purchase orders.

- **Vendor Invoice Management**

  - Add vendor invoices to purchase orders.
  - View all vendor invoices.
  - View specific vendor invoices.
  - Update vendor invoice details.
  - Delete vendor invoices.

- **Good Receive Management**

  - Add good receive data including completeness of goods and payment status.
  - View all good receive data.
  - View specific good receive records.
  - Update good receive details.
  - Delete good receive records.

## Installation

### Prerequisites

Ensure you have Python installed on your system (Python 3.x recommended). You also need to install the `tabulate` library for table formatting.

### Steps

1. Clone the repository or download the script.
2. Navigate to the project directory.
3. Install dependencies by running:
   ```sh
   pip install tabulate
   ```
4. Run the script:
   ```sh
   python Procure-to-pay (P2P) capstone project.py
   ```

## Usage

1. The program presents a main menu with the following options:
   - Purchase Order
   - Vendor Invoice
   - Good Receive
   - Exit
2. Navigate through the menus by selecting the corresponding option number.
3. Follow the prompts to enter data or perform actions.

## File Structure

- `Procure-to-pay (P2P) capstone project.py`: The main script containing all functions and logic for the application.
- `README.md`: Documentation for installation and usage.

## Technologies Used

- Python
- `tabulate` for table formatting
- Random and string modules for generating unique identifiers

## License

This project is open-source and available for personal and educational use.

## Author

Muhammad Hanafi
