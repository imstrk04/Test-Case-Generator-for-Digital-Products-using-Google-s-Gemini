# Test Case Generator for Digital Products using Google’s Gemini

## Overview

Welcome to the Test Case Generator for Digital Products! This handy Streamlit app helps you create detailed test cases for images you upload. Using Google’s powerful Gemini API, the app generates step-by-step instructions tailored to your images and any extra context you provide. Whether you’re testing a new feature or validating an image-based functionality, this tool makes the process a breeze.

## Features

- **Image Upload**: Users can upload images for which test cases need to be generated.
- **Optional Input Prompt**: Users can provide additional context or instructions to tailor the generated test cases.
- **Generative AI Model**: Utilizes Google’s Gemini API to generate detailed testing instructions.
- **Streamlit Interface**: A user-friendly interface built with Streamlit for easy interaction.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  - `streamlit`
  - `python-dotenv`
  - `google-generativeai`

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/imstrk04/Test-Case-Generator-for-Digital-Products-using-Google-s-Gemini.git
   cd Test-Case-Generator-for-Digital-Products-using-Google-s-Gemini
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory of the project with the following content:

   ```dotenv
   GOOGLE_API_KEY=your_google_api_key_here
   ```

### Running the Application

Start the Streamlit app by running:

bash
streamlit run testcase-generator.py


Open your web browser and navigate to `http://localhost:8501` to use the application.

## Usage

1. **Upload Images**: Use the file uploader to choose images you want to generate test cases for.
2. **Input Prompt**: Optionally provide additional context in the text input box.
3. **Generate Instructions**: Click on the "Generate Testing Instructions" button to create test cases.
4. **View Results**: Review the generated instructions displayed below the button.

## Example

An example of the output might look like this:

- **Description**: The image displays a login screen.
- **Pre-conditions**: Ensure the application is running and accessible.
- **Testing Steps**: 
  1. Enter valid credentials.
  2. Click on the "Login" button.
- **Expected Result**: User is successfully logged in and redirected to the homepage.

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

T. Sadakopa Ramakrishnan  
Email: [nstsrka04@gmail.com](mailto:nstsrka04@gmail.com)

## Acknowledgments

- [Streamlit](https://streamlit.io/) for providing a powerful tool for building interactive web applications.
- [Google Gemini](https://cloud.google.com/generative-ai) for the generative AI capabilities.



Feel free to customize any sections to better fit your project’s specific details or requirements
