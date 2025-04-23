# CRM Application

The **CRM Application** is a desktop-based customer relationship management tool built using **Tkinter** and **SQLite3**. It provides users with an intuitive interface to manage customer data, including adding, editing, searching, deleting, and organizing records.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Structure](#structure)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

---

## Program Demo

![CRM Application](https://github.com/Poyamohamadi/CRM_Application/blob/main/image.png)

---

## Features

- **Customer Data Management**:
  - Add, edit, delete, and view customer information such as name, family name, national ID, address, city, state, and postal code.
- **Search Functionality**:
  - Search for customers based on specific fields like name, family name, national ID, address, city, state, or postal code.
- **Real-Time Updates**:
  - Instantly update customer records and see changes reflected in the table.
- **Data Persistence**:
  - All customer data is stored in a local SQLite database (`data.db`), ensuring data retention between sessions.
- **Table Operations**:
  - Move records up or down within the table.
  - Clear all entries or reset the entire database.
- **User-Friendly Interface**:
  - Built using **Tkinter**, providing a clean and simple GUI.

---

## Installation

### Prerequisites

- Python 3.7 or higher installed on your system.
- Install the required dependencies by running:

```bash
pip install tkinter
```

### Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/Poyamohamadi/CRM.git
cd CRM
```

---

## Usage

1. Run the application by executing the Python script:

   ```bash
   python main.py
   ```

2. Use the provided interface to perform various operations:
   - **Add Customer**: Fill in the customer details in the "Register/Edit" section and click "Add".
   - **Edit Customer**: Select a customer from the table, modify the details, and click "Update Edit".
   - **Delete Customer**: Select one or more customers and click "Delete".
   - **Search**: Use the "Search" option under the "Tools" menu to find specific records.
   - **Clear Table**: Use the "Clear Table" option to remove all records from the database.

---

## Structure

The code is organized into the following components:

1. **Main Application Class (`MyApp`)**:
   - Inherits from `tk.Tk` to create the main application window.
   - Initializes the GUI elements such as the table, entry fields, buttons, and menus.

2. **GUI Elements**:
   - **Table (Treeview)**: Displays customer records in a tabular format.
   - **Entry Fields**: For entering customer details (name, family name, national ID, etc.).
   - **Buttons**: Perform actions like adding, editing, deleting, and clearing records.
   - **Menus**: Provide additional functionality like searching and refreshing the table.

3. **Database Operations**:
   - Uses SQLite3 to store and retrieve customer data.
   - Functions like `add()`, `update()`, `remove()`, and `query_database()` handle database interactions.

4. **Helper Functions**:
   - Functions like `lookup()` for searching, `clear_entries()` for clearing input fields, and `up()`/`down()` for moving records within the table.

5. **Main Execution Block**:
   - Ensures the application runs only when executed directly.

---

## Dependencies

- **Python**: Version 3.6 or higher.
- **Tkinter**: A built-in Python library for creating GUI applications.
- **SQLite3**: A lightweight database library used for storing customer data.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request detailing your changes.

Please ensure your code adheres to the existing style and includes appropriate documentation.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](https://github.com/Poyamohamadi/CRM_Application/blob/main/LICENSE.md) file for more details.

---

## Acknowledgments

- **Tkinter Library**: Thanks to the developers of `tkinter` for creating a robust and easy-to-use GUI toolkit.
- **SQLite3**: Special thanks to the SQLite team for providing a lightweight and efficient database solution.

---

## Contact

For questions or feedback, feel free to reach out:

- **GitHub**: [Poyamohamadi](https://github.com/Poyamohamadi)

---

Thank you for using the **CRM Application**! 😊
