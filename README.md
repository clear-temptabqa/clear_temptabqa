## Directory Structure
```
├── data/                                 # Directory for dataset
│   └── temptabqa_v2/
│       ├── qapairs/
│       │   ├── combined_data/
│       │   │   └── all_annotated_data.json
│       │   ├── dev-set/
│       │   │   ├── dev-set.csv
│       │   │   └── dev-set.json
│       │   ├── head-set/
│       │   │   ├── head-set.csv
│       │   │   └── head-set.json
│       │   └── tail-set/
│       │       ├── tail-set.csv
│       │       └── tail.set.json
│       └── tables/
│           ├── html/
│           │   ├── 0.html
│           │   ├── 1.html
│           │   └── ...
│           ├── json/
│           │   ├── 0.json
│           │   ├── 1.json
│           │   └── ...
│           ├── kg/
│           │   ├── 0.json
│           │   ├── 1.json
│           │   └── ...
│           └── table_category.csv
├── models/                               # Directory for model scripts
│   ├── gemini.py
│   ├── gpt.py
│   ├── llama.py
│   └── palm.py
├── prompts/                              # Directory for prompt scripts
│   ├── chain_of_thought.py
│   ├── clear.py
│   ├── faithful_cot.py
│   ├── program_of_thoughts.py
│   ├── question_decomposition.py
│   └── table_evidence_extraction.py
├── README.md                             # Project README file
└── script.py                             # Script to run models and prompts       
```


## Running the models and prompts

Run the script using the following command:

`python script.py --model <model_name> --prompt <prompt_name> --split <dataset_split>`
Replace `<model_name>`, `<prompt_name>`, and `<dataset_split>` with the desired values.

**model**: The model function to call. Choices include gpt3, gpt4, gemini, llama, palm.

*prompt*: The prompt function to call. Choices include few_shot_cot, zero_shot_cot, clear, few_shot_faithful_cot, zero_shot_faithful_cot, few_shot_pot, zero_shot_pot, question_decomposition, evidence_extraction.

**split**: The dataset split to run on. Choices include dev, train, head, tail.

Example command:

`python script.py --model gpt3 --prompt few_shot_cot --split dev`

### Output
The script will generate an output.csv file in the project directory. The CSV file will contain the following columns:

* id: The question ID.

* question: The question text.

* answer: The answer text.

* category: The question category.

* table_id: The table ID.

* output: The model's output.