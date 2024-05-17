def long_to_short(text):
  """
  This function transforms a long variation (author names separated by hyphens)
  into a short variation (using only the first letters of each author's last name).

  Args:
      text: A string containing the long variation.

  Returns:
      A string containing the short variation.
  """
  # Split the text by hyphens, ensuring uppercase first letters for each part.
  words = [word.capitalize() for word in text.split("-")]
  # Create the short variation by joining the first letters of each word.
  short_variation = "".join([word[0] for word in words])
  return short_variation

# Get user input
text = input()

# Call the function and print the result
short_text = long_to_short(text)
print(short_text)
