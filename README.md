# Silver-Chat 1.0
A finetuned gpt model with a focus on helping older adults with technology.

website: https://silversupport.in/

Based on Handwritten prompts as well as scraped data from forums

# **Files**
**BRIEF EXPLANATION OF WHAT EACH FILE IS**

**Base Data** - 
Contains handwritten prompts and answers. Questions and Answers contain their respected contents, where as Data is both of them formated into a question followed by a new line.

**Chat Bot** - 
Actually uploads the final data files and finetunes the chatbot based off of them. Also stores the file used to actually run Silver*, as well as the system prompt.

**Clean Data** - 
Stores both the Unclean and Clean data. All the unformatted questions and answers from the web scraping, as well as the cleaned up version and the titles of the questions.

**Data Interpretation** - 
Each file is described sequentially.

Data Cleaner:
 Cleans the data, removes special characters, encodes and formats it properly.

Data Counter:
 Counts the number of scraped questions and answers (17318 questions and answers)

Data Validation:
 Validates the data, tokenizes it and estimates the cost and number of epochs needed for proper training

Final Clean:
 Removes bugs in the data, strips it.

Json Creator:
 Creates the first JSON based on scraped data

Json Creator 2:
 Creates the second JSON based on handwritten prompts
 
**Data Scraping** - 
Tom's Hardware is a popular online forum where users discuss various topics related to technology, including networking, system building, operating systems, and more. This web scraper automates the process of extracting questions and answers from different forum categories to gather insights and data for the AI to be finetuned off of. Includes a retry system, headers, and dynamic URL adjusting. 

**Final data** - 
The final, completely clean data.

**Json data** -
Contains both JSON files, as well as having them be split up into test and training data, combined with data in OPENAPI's format for finetuning.

**My Past Endevours** - 
Google's natural dataset, filtered for tech questions, that was used in combination with the scraped data. Took a LOT of human filtering and reorganizing. you can see the semi filtered questions. most of them are completely unrelated to tech.

# **USAGE**

Silver cannot be run by the public due to api keys being needed. You can find an online version at (https://silversupport.in)

# **FUTURE DIRECTION**

Silver 2.0 is still being actively developed on. It contains a finetuned system prompt and better datasets. Please visit the website and read the blogs (https://silversupport.in/links) to be completely updated. 


