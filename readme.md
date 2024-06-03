# AutoGen AI agent Google Trends analysis using LangChain tools

AutoGen is a Microsoft open-source library for enabling Large Language Model (LLM) applications with multi-agent collaborations, teach ability and personalisation. With the AutoGen framework, users can build LLM workflows.

AutoGen can use self-made tools, or use already existing LangChain tools from the LangChain library.

This example uses OpenAI's ChatGPT 4 model and two LangChain tools.

The "ReadFileTool" reads the file `google_trends.txt` from the local file system. The content of this file is the text "Artificial Intelligence".

This text is then used as the search term for the "GoogleTrendsQueryRun" tool. This tool fetches trend information from [Google Trends](https://trends.google.com/trends/).

The Google Trends data is then analysed and explained by the LLM.

To avoid unnecessary round trips between the user and the Google Trends Agent, the maximum number of turns is limited to 3.

You need an OpenAI API key for this example. [Get your OpenAI API key here](https://platform.openai.com/login). You can insert your OpenAI API key in the `main.py` script, or you can supply your OpenAI API key either via the `.env` file, or through an environment variable called `OPENAI_API_KEY`. If you don't want to use an OpenAI model, then you can also use other models, including local models.

You also need a free SerpApi API key for this example to use the Google Trends tool. [Get your free SerpApi API key here](https://serpapi.com/users/sign_up). You can insert your SerpApi API key in the `main.py` script, or you can supply your SerpApi API key either via the `.env` file, or through an environment variable called `SERPAPI_API_KEY`.

| >>>>> The final answer will look similar to this example: <<<<< |
| --------------------------------------------------------------- |

```
The Google Trends data for the term "Artificial Intelligence" from May 28, 2023, to June 8, 2024, shows a detailed analysis of how interest in this topic has fluctuated over time. Here are the key points extracted from the trends data:

1. **Interest Fluctuations:**
   - **Minimum Interest:** The lowest recorded interest value is 66.
   - **Maximum Interest:** The highest recorded value hit 100.
   - **Average Interest:** On average, the interest level stood at approximately 85.59.
   - **Percent Change:** There was a -21.0% percent change in interest over the observed period, suggesting a decrease towards the latter part of the year.

2. **Interest Over Time:**
    - The data begins with very high interest, hitting the peak value at multiple times but primarily is above 80, except towards the ending phases.
    - A noticeable decline in the interest is observed in later periods, which corresponds to the stated percent change.

3. **Rising and Top Related Queries:**
   - **Rising Related Queries:** These include diverse and specific topics like "austria-forex.com," "kmspico download," and more nuanced inquiries such as the role of generative AI in drug discovery, implications of AI in ethical practices, and various aspects of prompt engineering in generative AI systems.
   - **Top Related Queries:** General curiosity around AI such as "what is artificial intelligence," "machine learning," "artificial intelligence course," and specific products or tools like "artificial intelligence chatgpt" highlights both educational interests and direct applications.

This data indicates a strong and sustained interest in artificial intelligence with a varied audience exploring both foundational knowledge and advanced applications in AI. The drop in interest might be due to multiple factors, such for instance, seasonal changes, market saturation, or shifts in technology trends which might be worth exploring further in specific contexts. The related queries section indicates both a general awareness and specialized interests in the field, showcasing the breadth and depth of how artificial intelligence is perceived and explored across different sectors.
```
