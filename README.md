# Tokenizers
- Tokenizer is a mechanism that converts text into numerical representation (tokens)
- The "science" in it is finding a good way to represent pieces of text as numbers, how to best split words
- What happens after splitting? How do we assign the numerical values?


## Types of Tokenizers

1. Word-Level Tokenizers:

Split text into words based on spaces and punctuation.
Example: "I am learning NLP." -> ["I", "am", "learning", "NLP", "."]

2. Character-Level Tokenizers:
 
Split text into individual characters.
Example: "NLP" -> ["N", "L", "P"]

3. Subword-Level Tokenizers:

Split text into subwords or morphemes, handling unknown words better and reducing vocabulary size.
Common methods:
Byte Pair Encoding (BPE): Iteratively merges the most frequent pairs of characters or subwords.
WordPiece: Similar to BPE but used in models like BERT.
SentencePiece: Unsupervised tokenization method that can handle both BPE and unigram models.

4. N-Gram Tokenizers:

Split text into contiguous sequences of n items (words or characters).
Example: For n=2, "I am learning NLP" -> ["I am", "am learning", "learning NLP"]

5. Whitespace Tokenizers:

Split text based on whitespace only.
Example: "I am learning NLP." -> ["I", "am", "learning", "NLP."]

## Most Common Tokenizers
The most common tokenizers in modern NLP are subword-level tokenizers because they strike a balance between handling unknown words and keeping the vocabulary size manageable. Among these, BPE, WordPiece, and SentencePiece are widely used in popular models.

## Tokenizers and (Chat)GPT
GPT Models (Generative Pre-trained Transformers), such as GPT-2 and GPT-3, use Byte Pair Encoding (BPE) for tokenization. Here's a bit more detail about how BPE works and why it is used in GPT models:
