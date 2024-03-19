"""
Capital One's marketing team is working on a project to analyze customer feedback from their feedback surveys.

The team sorted the words from the feedback into three different categories;
•	short_comments
•	mid_length_comments
•	long_comments

The team wants to find comments that are not short and come from social media. The output should include 'feedback_id,' 'feedback_text,' 'source_channel,' and a calculated category.

DataFrame: customer_feedback
feedback_id: int
feedback_text: varchar
source_channel: varchar
comment_category: varchar
"""

# Import your libraries
import pandas as pd

# Start writing code
customer_feedback_fltrd = customer_feedback[(customer_feedback['comment_category']!='short_comments')&(customer_feedback['source_channel']=='social_media')]

customer_feedback_fltrd = customer_feedback_fltrd.drop_duplicates(subset=['feedback_id'])
customer_feedback_fltrd
