# Arxiv Paper Accumulator User Manual

## Introduction

The Arxiv Paper Accumulator is a web application that allows users to automatically accumulate daily papers from any specified domain on the arXiv website. Users can input their interested domains and set the update interval to determine how often the app retrieves the paper list from arXiv. The app then searches arXiv under the specified domains and lists the paper titles, abstracts, and links in a diagram. Users can also use filters to check the papers list under different domains.

## Installation

To use the Arxiv Paper Accumulator, you need to follow these steps to install the necessary dependencies:

1. Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt and navigate to the directory where you want to install the Arxiv Paper Accumulator.

3. Clone the repository by running the following command:

   ```
   git clone https://github.com/your-username/arxiv-paper-accumulator.git
   ```

4. Navigate to the project directory:

   ```
   cd arxiv-paper-accumulator
   ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Arxiv Paper Accumulator, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the web app:

   ```
   python main.py
   ```

3. The web app window will open. You will see the following input fields:

   - **Enter domains (comma-separated):** Enter the domains you are interested in, separated by commas. For example, "machine learning, computer vision".

   - **Enter update interval (in minutes):** Enter the update interval in minutes. This determines how often the app retrieves the paper list from arXiv.

4. After entering the domains and update interval, click the "Search" button. The app will start searching arXiv under the specified domains and retrieve the paper list.

5. The retrieved papers will be displayed in the listbox below. Each paper will show the title, abstract, and link.

6. To filter the papers by domain, enter the domain in the "Filter papers by domain" field and click the "Filter" button. The app will display only the papers that match the specified domain.

7. You can scroll through the paper list using the scrollbar on the right side of the window.

8. To stop the app, close the web app window or press Ctrl+C in the terminal or command prompt where the app is running.

## Conclusion

The Arxiv Paper Accumulator is a powerful web app that allows users to automatically accumulate daily papers from any specified domain on the arXiv website. By following the installation and usage instructions provided in this manual, you can easily use the app to stay updated with the latest research papers in your field of interest. Enjoy exploring the world of arXiv!