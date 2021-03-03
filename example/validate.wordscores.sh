#!/usr/bin/env zsh
~/uni_stuff/postdoc/marian-dev/build/marian-scorer -m model_2emb/model.npz -v model_2emb/vocab.rand.yml -t verify.4 -o verify.4.scores --word-scores
paste verify.4 verify.4.scores | sort -n -k5 | convert_to_probs.py > verify.4.2emb.wordscores
rm verify.4.word.scores

~/uni_stuff/postdoc/marian-dev/build/marian-scorer -m model_2emb.8k/model.npz -v model_2emb.8k/vocab.rand.yml -t verify.4 -o verify.4.scores --word-scores
paste verify.4 verify.4.scores | sort -n -k5 | convert_to_probs.py > verify.4.2emb.8k.wordscores
rm verify.4.word.scores


~/uni_stuff/postdoc/marian-dev/build/marian-scorer -m model_16emb/model.npz -v model_16emb/vocab.rand.yml -t verify.4 -o verify.4.scores --word-scores
paste verify.4 verify.4.scores | sort -n -k5 | convert_to_probs.py > verify.4.16emb.wordscores
rm verify.4.scores

~/uni_stuff/postdoc/marian-dev/build/marian-scorer -m model_16emb.2k/model.npz -v model_16emb.2k/vocab.rand.yml -t verify.4 -o verify.4.scores --word-scores
paste verify.4 verify.4.scores | sort -n -k5 | convert_to_probs.py > verify.4.16emb.2k.wordscores
rm verify.4.scores

~/uni_stuff/postdoc/marian-dev/build/marian-scorer -m model_16emb.8k/model.npz -v model_16emb.8k/vocab.rand.yml -t verify.4 -o verify.4.scores --word-scores
paste verify.4 verify.4.scores | sort -n -k5 | convert_to_probs.py > verify.4.16emb.8k.wordscores
rm verify.4.word.scores
