# Example marian configs and training

### Training

```bash
cd model_2emb
/path/to/marian -c config.yml
```

### Force decoding (Also known as scoring)
Look at `validate.wordscores.sh`

### Additional scripts
`dump_emb.py` Dumps the embedding layer of a model + the vocabulary ordering

`normalise_emb_layer.py` Given a model, renormalise the embedding layer. One can later perform fine tuning using the `embedding-fix-trg: true` option in the marian config to prevent the emebddings from being trained further.
