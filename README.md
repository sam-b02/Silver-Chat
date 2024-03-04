# Silver-Chat 1.0

Silver-Chat is a fine-tuned GPT model focused on assisting older adults with technology-related issues. It utilizes handwritten prompts and scraped data from forums to provide accurate and helpful responses.

**Website:** [Silver Support](https://silversupport.in/)

## Files

### Base Data
Contains handwritten prompts and answers. Questions and answers are formatted into question-answer pairs.

### Chat Bot
Uploads the final data files and fine-tunes the chatbot based on them. It also stores the file used to run Silver and the system prompt.

### Clean Data
Stores both unclean and clean data. Unclean data consists of unformatted questions and answers from web scraping, while clean data contains cleaned-up versions and titles of questions.

### Data Interpretation
- **Data Cleaner:** Cleans the data, removes special characters, and formats it properly.
- **Data Counter:** Counts the number of scraped questions and answers.
- **Data Validation:** Validates the data, tokenizes it, and estimates the cost and number of epochs needed for proper training.
- **Final Clean:** Removes bugs in the data and strips it.
- **JSON Creator:** Creates JSON files based on scraped data.
- **JSON Creator 2:** Creates JSON files based on handwritten prompts.

### Data Scraping
Automates the process of extracting questions and answers from the Tom's Hardware forum to gather insights and data for fine-tuning the AI. Includes a retry system, headers, and dynamic URL adjusting.

### Final Data
Contains the final, completely clean data.

### JSON Data
Includes both JSON files, split into test and training data, combined with data in OPENAPI's format for fine-tuning.

### My Past Endeavors
Includes Google's natural dataset, filtered for tech questions, used in combination with scraped data.

## Usage

Silver cannot be run publicly due to API keys being needed. However, you can access an online version at [Silver Support](https://silversupport.in/).

## Future Direction

Silver 2.0 is still actively being developed, aiming to include a fine-tuned system prompt and better datasets. For updates, visit the [Silver Support website](https://silversupport.in/links).

## License

[MIT License](LICENSE)
