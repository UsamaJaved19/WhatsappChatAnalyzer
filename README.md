# WhatsApp Chat Analyzer

### Overview
The **WhatsApp Chat Analyzer** is a comprehensive tool designed to extract insights and analyze WhatsApp chat data. The system parses exported WhatsApp chats and provides meaningful visualizations and statistical information about conversations, user behavior, message patterns, and more.

### Features
- **Message Count**: Analyze the number of messages sent by each participant.
- **Most Active Users**: Identify which users are the most active in the conversation.
- **Message Timeline**: Visualize message activity over a specific period.
- **Word Cloud**: Generate word clouds to highlight the most frequently used words.
- **Media Tracking**: Track the usage of emojis, links, and media messages.

  
### Technologies Used
- **Python**: The main programming language used for data processing and analysis.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.
- **NLTK**: For natural language processing and sentiment analysis.
- **Regular Expressions (Regex)**: For parsing the WhatsApp chat file.

### Installation
To run the WhatsApp Chat Analyzer, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WhatsApp-Chat-Analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd WhatsApp-Chat-Analyzer
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Export your WhatsApp chat by following these steps:
   - Open WhatsApp on your phone.
   - Go to the chat you want to analyze.
   - Tap the menu (three dots) > More > Export Chat.
   - Choose to export "Without Media" (for now).
   - Save the exported `.txt` file to your computer.
   
2. Run the chat analyzer:
   ```bash
   python whatsapp_analyzer.py path_to_chat_file.txt
   ```
   
3. The script will output various statistics, graphs, and sentiment analysis of the chat.


### Contributing
Contributions are welcome! If you would like to contribute to the project, please fork the repository and create a pull request with detailed information about the changes.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Contact Information
For further inquiries or suggestions, feel free to reach out at:
- **Email**: usama11javed@outlook.com
