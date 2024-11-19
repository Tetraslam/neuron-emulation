# Sapientia Research: Neuron Emulation Suite

Welcome to the repository for Sapientia Research's Neuron Emulation explorations! This repository will serve as a collaborative space for documenting our research, experiments, and progress as we work toward building a general-purpose biocomputing architecture. Our primary goal is to explore and develop tools for neuron emulation, which will lay the foundation for our future innovations in biocomputing.

---

## Project Objectives

1. **Explore Existing Paradigms**: Study existing neuron simulation frameworks and paradigms, identifying their strengths, limitations, and potential areas for improvement.
2. **Design Novel Emulation Paradigms**: Build our own neuron emulation framework tailored for general-purpose biocomputing applications.
3. **Develop a Suite of Tools**: Create a comprehensive neuron emulation suite that is modular, scalable, and user-friendly, aimed at accelerating research and development for our startup and the wider community.

---

## Repository Structure

Here's a breakdown of the repository structure to help us organize our work:

```
├── docs/                      # Documentation, including findings, summaries, and notes
├── research/                  # Research-related files and references
│   ├── existing_paradigms/    # Notes, analysis, and experiments with existing frameworks
│   ├── custom_designs/        # Prototypes and designs for our own emulation framework
├── tools/                     # Scripts, utilities, and other tools developed during the project
├── experiments/               # Code and results for neuron simulation experiments
├── data/                      # Datasets, configurations, and simulation inputs/outputs
└── README.md                  # This README file
```
---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Tetraslam/neuron-emulation.git
cd neuron-emulation
```

### 2. Setup Environment

First, create and activate a Python virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate

# Activate virtual environment (Linux/Mac)
source venv/bin/activate
```

Next, install NEURON manually from [their website](https://www.neuron.yale.edu/neuron/download). After installation, install the remaining dependencies:
```bash
pip install -r requirements.txt
```

The repository includes pre-commit hooks for code quality. Install them with:
```bash
pip install pre-commit
pre-commit install
```

Note: The repository is configured to ignore virtual environments, cache files, and experiment outputs. Large datasets and experiment results should be stored elsewhere and not committed to version control. Consider using [DVC](https://dvc.org/) for managing large data files if needed.

### 3. Start a New Experiment

To begin a new experiment:
1. Copy the experiment template:
```bash
cp experiments/template/experiment_template.py experiments/your_experiment_name.py
```
2. Modify the experiment configuration and implementation in your new file
3. Run your experiment:
```bash
python experiments/your_experiment_name.py
```

Your results will be automatically logged and tracked using Weights & Biases.

### 4. Workflow Overview

#### Phase 1: Explore Existing Paradigms
- Document findings in `docs/` under `existing_paradigms/`.
- Write test scripts for experiments in `experiments/`.

#### Phase 2: Design Our Own Emulation Paradigm
- Use `custom_designs/` to propose, prototype, and refine our framework.
- Collaborate through the `tools/` directory for shared utilities.

---

## Documentation Guidelines

- **Write Clear Notes**: Use Markdown files in `docs/` to summarize findings and ideas.
- **Comment Code Thoroughly**: Always comment your code in `experiments/` and `tools/` to make it easy to follow.
- **Version Control**: Use Git branches for major updates. Commit frequently with descriptive messages.
- **Use Issues for Tasks**: Track our ongoing tasks, questions, and challenges using the repository's Issues feature.

---

## Contributing

1. Create a branch for your work:
   ```bash
   git checkout -b <your-branch-name>
   ```
2. Add and commit your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```
3. Push your branch and create a pull request:
   ```bash
   git push origin <your-branch-name>
   ```
4. Review each other’s work before merging to `main`.

---

## Next Steps

### First Task: Explore Existing Paradigms
- Research popular neuron simulation frameworks like NEURON, NEST, and Brian2.
- Experiment with small simulations and document results in `existing_paradigms/`.

### Future Milestones
1. Complete a thorough review of existing paradigms.
2. Develop a prototype for our custom neuron emulation framework.
3. Create modular tools for ease of simulation and experimentation.

---

## Knowledge Sharing

We’re building this suite to empower not just ourselves, but potentially others in the biocomputing community. Let’s document our journey thoroughly, share insights, and stay organized to ensure that progress is continuous and efficient.

---

Happy experimenting,  
**Sapientia Research Team**
