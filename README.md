# Genotype

Genotype is a Python-based project designed to analyze genetic data, estimate genotypes, and predict disease possibilities. This project was created during high school, and the accompanying `.xlsx` files are in Turkish as a result.

# Inspiration

I initially came up with the idea while solving biology questions in high school. The code is designed to solve the following types of family tree genotype, phenotype questions

![phpWsFDiT](https://github.com/user-attachments/assets/1b5c6d5c-bf05-45ad-a3a6-34a33f4ffb20)


## Features

1. **Data Parsing**:
   - Reads genetic data from an Excel file (`1.xlsx`) containing the following sheets:
     - **Sheet 1**: Individual data with fields:
       - `name`: Name of the person
       - `dad_id`: ID of the father
       - `mom_id`: ID of the mother
       - `genotype`: Known genetic information
       - `fenotype`: Phenotypic traits
       - `id`: Unique identifier for each person
       - `sex`: Gender of the person (`E` for male, `K` for female)
     - **Sheet 2**: Specific genes and their characteristics.
     - **Sheet 3**: Disease-related phenotypes linked to genes.

2. **Genotype Analysis**:
   - Matches genetic data across generations to estimate unknown genotypes.
   - Uses parent-child relationships to refine genetic information and reduce errors.

3. **Disease Prediction**:
   - Cross-references individual genotypes with disease-related phenotypes to predict potential health risks.
   - Estimates disease probabilities for individuals and their potential offspring.

4. **File Processing**:
   - Outputs detailed reports in text files for:
     - Individual genetic data
     - Disease predictions
     - Phenotype probabilities for potential offspring

## Usage

1. **Prepare the Excel File**:
   - Ensure the Excel file (`1.xlsx`) contains the required sheets and fields as described above.

2. **Run the Program**:
   - Execute `Genotype.py` in a Python environment to process the data.

3. **Outputs**:
   - Processed reports are saved in the `Reports` directory.
   - Disease probabilities and genetic data are detailed in the output files.

## Project Context

This project was developed in high school as a personal exploration into genetics and programming. The code is written in Python and utilizes the `openpyxl` library for Excel processing. While the dataset and some comments are in Turkish, the logic is generalizable for other languages and datasets.

## Dependencies

- Python 3.x
- Required Python libraries:
  - `openpyxl`

## Limitations

- The dataset is in Turkish, as it was originally created in a high school environment.
- The project may require modifications to adapt to different datasets or languages.

## Acknowledgments

This project was an early step in learning Python and exploring genetics, serving as a foundation for more advanced programming projects.
