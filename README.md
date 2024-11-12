# Tech Spec Analysis with LLMs

<img src="https://img.shields.io/badge/AI-Code%20Assist-EB9FDA"></a>

## Description
This project is a Python-based application that uses the SAP Generative AI Hub SDK to interact with OpenAI's GPT-4o model for threat modeling and tech spec analysis. The application performs risk classification, rapid risk assessment (RRA), and security review using best practices. For a POC, sample spec of best practices are stored under `best_practices` directory against which review is perfomred.

The project can also run Threat Model analysis on a uploaded image. The project uses the OpenAI vision API to provide analysis based on the STRIDE methodology.
https://platform.openai.com/docs/guides/vision

The project was developed to explore the opportunities how we can integrate LLM's as part of AppSec activities in SDLC


## Features
- **File Upload**: Upload tech spec documents in PDF format.
- **Risk Classification**: Classify risks based on the content of the tech spec.
- **Rapid Risk Assessment (RRA)**: Perform rapid risk assessment using Mozilla’s RRA guide.
- **Security Review**: Conduct a security review and provide citations from best practices.


## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/tech-spec-analysis.git
    cd tech-spec-analysis
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **For Tech Spec Analysis Run the application**:
    ```sh
    streamlit run main.py
    ```

2. **Upload a tech spec PDF**: Use the file uploader in the Streamlit app to upload your tech spec document.

3. **View Analysis Results**: The application will display the risk classification, rapid risk assessment, and security review results.

4. **For Threat modelling Analysis Run the application**:
    ```sh
    streamlit run main1.py
    ```
5. **Upload a Data Flow Diagram**: Use the file uploader in the Streamlit app to upload your DFD diagram.

6. **View Analysis Results**: The application will display the Threat Type, Scenario, Potential Impact and Component.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License.

## Disclaimer
This project was developed with assistance from Large Language Models (LLMs) GPT4o. While efforts have been made to ensure quality and accuracy, please review and validate the code according to your specific needs. 