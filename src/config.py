import transformers
import pathlib
MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
DEVICE = 'cpu'

MAIN_PATH = pathlib.Path(__file__).parents[1]
INPUT_PATH = MAIN_PATH / "input"
BERT_PATH = INPUT_PATH / "bert_base_uncased"
TRAINING_FILE = INPUT_PATH / "imdb.csv"

TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH,
    do_lower_case=True
)
