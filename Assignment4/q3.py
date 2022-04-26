compressed_text_size = 148
dictionary_size = 25
original_text_size = 240

print(f"Compressed text size: {compressed_text_size} characters\n"
      f"Dictionary size: {dictionary_size} characters\n"
      f"Total: {compressed_text_size + dictionary_size} characters\n"
      f"Original text size: {original_text_size} characters\n"
      f"Compression: {round(100 - ((compressed_text_size + dictionary_size) / original_text_size * 100), 2)}%")
