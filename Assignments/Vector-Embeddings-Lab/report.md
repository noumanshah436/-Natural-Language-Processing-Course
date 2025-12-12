# CBOW vs BERT — Comparison Report

## Dataset
- Tiny Shakespeare / Game of Thrones subset (describe size, e.g., 15,000 tokens; vocab size: XXXX)

## Part 1 (CBOW)
- Implementation details: window=2, D=50, epochs=5, learning rate=0.05.
- Embeddings saved to cbow_embeddings.npy.

## Part 2 (BERT)
- Used bert-base-uncased from HuggingFace.
- Extracted token-level and approximated word-level embeddings.

## Part 3 (Comparison)
### Polysemy example: 'bank'
- CBOW embedding is identical across contexts.
- BERT contextual embeddings for finance vs river senses have cosine similarity = <insert value from run>.
- PCA plot (bank_bert_pca.png) shows separation of senses.

### Downstream classification (finance vs nature)
- Classifier using CBOW-averaged embeddings:
  - Accuracy: X.XX
  - Precision / Recall / F1: ...
- Classifier using BERT CLS embeddings:
  - Accuracy: Y.YY
  - Precision / Recall / F1: ...

### Findings
- BERT provides different vectors for the same word in different contexts — helps disambiguation.
- CBOW is cheaper to train but fails at polysemous word disambiguation.
- For sentence-level classification, BERT outperforms simple averaged CBOW representations.

### Conclusion & Future Work
- Increase CBOW epochs / corpus size.
- Try skip-gram for rare words.
- Fine-tune BERT on the domain for even better performance.
