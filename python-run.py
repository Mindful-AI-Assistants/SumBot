# This script connects OpenAI GPT-3.5 Turbo with Slack, allowing you to summarize messages
# and automatically post the summarized content into Slack channels.

# Place this file at the root of your GitHub repository for easy access and execution.
# The environment variables (like API keys) should be stored in a separate .env file,
# which should be excluded from your Git repository for security purposes.

# After cloning the repository, you can install the necessary dependencies
# using the following command:
# pip install -r requirements.txt

# To execute this script, simply run:
# python run.py

# Make sure you configure your .env file with the following variables:
# OPENAI_API_KEY=your_openai_api_key
# SLACK_BOT_TOKEN=your_slack_bot_token



# Import necessary libraries
import os
import openai
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

# Load environment variables from a .env file (such as API keys)
load_dotenv()

# Set up OpenAI and Slack API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

# Function to summarize a given message using GPT-3.5 Turbo
def summarize_message(message):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Summarize the following message: {message}",
        max_tokens=50
    )
    summary = response.choices[0].text.strip()
    return summary

# Function to post the summarized message to a Slack channel
def post_summary_to_slack(channel, summary):
    try:
        client.chat_postMessage(
            channel=channel,
            text=f"Summary: {summary}"
        )
    except SlackApiError as e:
        print(f"Error posting to Slack: {e.response['error']}")

# Main section to summarize and post a message
if __name__ == "__main__":
    # Example Slack message to summarize (can be replaced with dynamic input)
    message = "Here is a long Slack message that needs summarizing."
    
    # Summarize the message using OpenAI's GPT-3.5 Turbo
    summary = summarize_message(message)
    
    # Post the summary to a Slack channel (replace '#general' with your channel)
    post_summary_to_slack("#general", summary)

