from collections import Counter, defaultdict
import re

def get_stats(vocab):
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

def learn_bpe(vocab, num_merges):
    merges = []
    explanations = []
    for i in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        vocab = merge_vocab(best, vocab)
        merges.append(best)
        explanations.append(f'Merge {i + 1}: {best}')
    return merges, vocab, explanations

def apply_bpe(text, merges):
    vocab = {' '.join(pair): ''.join(pair) for pair in merges}
    tokens = text.split()
    for i, token in enumerate(tokens):
        subtokens = list(token)
        while len(subtokens) > 1:
            pair = ' '.join(subtokens[:2])
            if pair in vocab:
                subtokens = [vocab[pair]] + subtokens[2:]
            else:
                break
        tokens[i] = ' '.join(subtokens)
    return ' '.join(tokens)

def tokenize_to_ids(text, vocab):
    token_to_id = {token: idx for idx, token in enumerate(vocab.keys())}
    tokens = text.split()
    token_ids = []
    for token in tokens:
        sub_tokens = token.split()
        for sub_token in sub_tokens:
            if sub_token in token_to_id:
                token_ids.append(token_to_id[sub_token])
            else:
                token_ids.append(token_to_id.get('UNK', -1))  # Using -1 for unknown tokens
    return token_ids

if __name__ == '__main__':
    # Take custom sentence input from the user
    input_sentence = input("Enter a sentence to tokenize: ").strip()
    
    # Build the initial vocabulary from the input sentence
    vocab = Counter()
    for word in input_sentence.split():
        token = ' '.join(word)
        vocab[token] += 1

    # Learn BPE merges
    num_merges = 10
    merges, learned_vocab, explanations = learn_bpe(vocab, num_merges)

    # Apply BPE to the input sentence
    tokenized_sentence = apply_bpe(input_sentence, merges)
    
    # Convert tokenized sentence to token IDs
    token_ids = tokenize_to_ids(tokenized_sentence, learned_vocab)
    
    # Print results
    print(f'Tokenized Sentence: {tokenized_sentence}')
    print(f'Token IDs: {token_ids}')
    
    # Print explanations
    print("\nExplanation of the BPE Tokenization Process:")
    print("Step-by-Step Process")
    print("Initial Vocabulary:\n")
    
    initial_tokens = list(vocab.keys())
    print(f"Characters and initial tokens: {initial_tokens}\n")
    
    print("Frequency Analysis:\n")
    for token, freq in vocab.items():
        print(f"{token}: {freq}")
    
    print("\nIterative Merging:\n")
    for explanation in explanations:
        print(explanation)
    
    print("\nFinal Vocabulary (Example):\n")
    final_vocab = list(learned_vocab.keys())
    for i, token in enumerate(final_vocab):
        print(f"{token} -> {i}")
