

# Django Login Page with Contact Information

![SCREENSHOT](/projectdjango/images/redmeimg.png)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

This project is basically a full stack webpage which comprises of a login page,register page fully done using pure html css and grains of java script

## Features

- User authentication and login.
- A user-friendly interface for entering and managing contact information.
- Secure password storage and authentication using Django's built-in features.

## Getting Started

Having basic Knowledge in HTML,CSS is more than enough (u need brain,laptop too)

### Prerequisites

Install before they can use your project. 

- Python 3.x
- Django 3.x
- VS code
- Django 

### Installation


1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-project.git
   ```

2. Change into the project directory:

   ```bash
   cd your-project
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations to create the database:

   ```bash
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the project in your web browser at `http://localhost:8000`.

## Usage

### Accessing the Login Page:

Open your web browser and navigate to the login page by entering the following URL in the address bar:

http://localhost:8000/login


### Registering or Logging In:

- **New User Registration:**
  - Click on the "Register" or "Sign Up" link.
  - Enter your details in the registration form (username, email, password, etc.).
  - Submit the form to create a new account.

- **Existing User Login:**
  - Enter your registered username and password in the login form.
  - Click the "Login" or "Sign In" button to access your account.

### Accessing Contact Information:

Once logged in, you'll gain access to the contact information page.

- Click on the "Contacts" or "Contact Information" link/button in the user dashboard or navigation menu.

### Managing Contact Details:

On the contact information page:

- **Adding Contacts:**
  - Look for an "Add Contact" or "New Contact" button.
  - Fill in the necessary details such as name, email, phone number, etc.
  - Save the contact to add it to your list.

- **Editing Contacts:**
  - Each contact entry may have an "Edit" or "Update" option.
  - Update the required information and save the changes.

- **Deleting Contacts:**
  - Find a "Delete" or "Remove" option associated with each contact.
  - Select this option to delete the respective contact from your list.

### Logging Out:

To log out from your account:

- Look for a "Logout" or "Sign Out" option, usually available in the user profile or the navigation menu.
- Click on it to securely log out from your account.

## Contributing:

Explain how others can contribute to your project, such as reporting issues, submitting pull requests, or suggesting new features. Include a code of conduct if applicable.

## License

Specify the license under which your project is released. If you're not sure, consult with your internship supervisor or use an open-source license like the MIT License.

## Acknowledgments

Give credit to anyone or any resources that helped you during your internship or in the development of your project.

---

Feel free to adapt and expand on this template to suit your specific project. Including detailed information in your README file will make it easier for others to understand and use your Django project.