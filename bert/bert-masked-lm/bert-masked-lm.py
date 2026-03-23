import numpy as np
from typing import Tuple

def apply_mlm_mask(
    token_ids: np.ndarray,
    vocab_size: int,
    mask_token_id: int = 103,
    mask_prob: float = 0.15,
    seed: int = None
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Apply BERT's MLM masking strategy.
    """
    if seed is not None:
        np.random.seed(seed)
    
    # YOUR CODE HERE
    mask_token_ids = token_ids.copy()
    labels = np.full(token_ids.shape, -100)

    mask_indices = np.random.rand(*token_ids.shape) < mask_prob
    labels[mask_indices] = token_ids[mask_indices]

    indice_chosen = np.where(mask_indices)

    for r, c in zip(*indice_chosen):
        prob = np.random.rand()

        if prob < 0.8:
            mask_token_ids[r, c] = mask_token_id
        elif prob < 0.9:
            mask_token_ids[r, c] = np.random.randint(0, vocab_size)
        else:
            pass
    return mask_token_ids, labels, mask_indices
    pass

class MLMHead:
    """Masked LM prediction head."""
    
    def __init__(self, hidden_size: int, vocab_size: int):
        self.hidden_size = hidden_size
        self.vocab_size = vocab_size
        self.W = np.random.randn(hidden_size, vocab_size) * 0.02
        self.b = np.zeros(vocab_size)
    
    def forward(self, hidden_states: np.ndarray) -> np.ndarray:
        """
        Predict token probabilities.
        """
        # YOUR CODE HERE
        logits = np.dot(hidden_states, self.W) + self.b
        return logits

